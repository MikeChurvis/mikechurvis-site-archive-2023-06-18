import json
from http import HTTPStatus

from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from .models import Message, MessageForm
from .tasks import queue_send_message_as_email


@csrf_exempt
def submit_contact_form(request: HttpRequest) -> JsonResponse:
    if request.method != 'POST':
        return JsonResponse({'http_error': 'Only POST method is allowed.'}, status=HTTPStatus.METHOD_NOT_ALLOWED)
    
    request_data = json.loads(request.body)
    
    message = MessageForm(request_data)
    
    if message.is_valid():
        print('message valid')
        
        if not request_data.get('dry_run'):
            saved_message = message.save()
            print(f'message (id:{saved_message.id}) saved')
            queue_send_message_as_email.delay(saved_message.id)
            print(f'message (id:{saved_message.id}) email queued')
        else:
            print('DRY RUN: message intentionally not saved')
        
        response = JsonResponse({'success': True})
    else:
        print(request_data, dict(message.errors))
        response = JsonResponse({'validation_error': dict(message.errors)}, status=HTTPStatus.BAD_REQUEST)
    
    return response