import { FormData, FormConfig } from "./types"
export { generateValidators }


const errorMsg = {
  required: (fieldName) => `${fieldName} is required.`,
  tooLong: (fieldName, length) =>
    `${fieldName} can't be longer than ${length} characters.`,
  tooShort: (fieldName, length) =>
    `${fieldName} must be at least ${length} characters long.`,
  badEmail: () => "Please enter a valid email address.",
}


function generateValidators(formConfig: FormConfig): { [key: string]: (formData: FormData) => boolean } {


  /** Returns true if the name field is all of the following:
  * - present
  * - shorter than maxlength
  * 
  * Otherwise, returns false and sets the field's validation label.
  * */
  function validateName(form: FormData): boolean {
    if (form.name.value.length === 0) {
      form.name.error = errorMsg.required("Name")
      return false
    }

    if (form.name.value.length > formConfig.nameMaxLength) {
      form.name.error = errorMsg.tooLong("Name", formConfig.nameMaxLength)
      return false
    }

    return true
  }

  /** Returns true if the company field is all of the following:
  * - shorter than maxlength
  * 
  * Otherwise, returns false and sets the field's validation label.
  * */
  function validateOrganization(form: FormData): boolean {
    if (form.organization.value.length > formConfig.organizationMaxLength) {
      form.organization.error = errorMsg.tooLong("Organization name", formConfig.organizationMaxLength)
      return false
    }

    return true
  }
  
  /** Returns true if the name field is all of the following:
  * - present
  * - shorter than maxlength
  * - a valid email address according to the IETF*
  * 
  * Otherwise, returns false and sets the field's validation label.
  * 
  * \*see: https://tools.ietf.org/id/draft-seantek-mail-regexen-03.html#rfc.section.3.1.4
  * */
  function validateEmail(form: FormData): boolean {

    const emailRegExp = new RegExp(formConfig.emailRegex)

    if (form.email.value.length === 0) {
      form.email.error = errorMsg.required("Email address")
      return false
    }

    if (form.email.value.length > formConfig.emailMaxLength) {
      form.email.error = errorMsg.tooLong("Email address", formConfig.emailMaxLength)
      return false
    }

    if (!emailRegExp.test(form.email.value)) {
      form.email.error = errorMsg.badEmail()
      return false
    }

    return true
  }

  /** Returns true if the messageContent field is all of the following:
  * - longer than minlength
  * - shorter than maxlength
  * 
  * Otherwise, returns false and sets the field's validation label.
  * */
  function validateMessage(form: FormData): boolean {
    if (form.message.value.length < formConfig.messageMinLength) {
      form.message.error = errorMsg.tooShort("Message content", formConfig.messageMinLength)
      return false
    }

    if (form.message.value.length > formConfig.messageMaxLength) {
      form.message.error = errorMsg.tooLong("Message content", formConfig.messageMaxLength)
      return false
    }

    return true
  }
  
  
  return { validateName, validateOrganization, validateEmail, validateMessage }
}



