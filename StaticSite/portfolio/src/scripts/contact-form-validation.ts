import { MessageDataValidatorResponse } from "./contact-form";

type InputType = HTMLInputElement | HTMLTextAreaElement;

export function validatorAlwaysValid(element: InputType) {
    element.setCustomValidity('');
    element.reportValidity();
}


export function validatorAlwaysInvalid(element: InputType) {
    element.setCustomValidity('validatorAlwaysInvalid')
    element.reportValidity();
}



export function reflectServerValidation (form: HTMLFormElement, serverValidationResponse: MessageDataValidatorResponse) {
    
}