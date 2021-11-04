from django.http import JsonResponse, HttpRequest


def submit_contact_form(request: HttpRequest) -> JsonResponse:
    data = request.POST
    
    name = data.get('name')
    company = data.get('company')
    email = data.get('email')
    message = data.get('message')
    
    request_echo = str(request.GET)
    return JsonResponse({
        'greeting': 'Hi! You sent me this:',
        'your_request': request_echo,
    })