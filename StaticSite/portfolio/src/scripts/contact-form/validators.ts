export {
  validateName,
  validateCompany,
  validateEmail,
  validateMessageContent,
}

import { FormData } from "./types"

const errorMsg = {
  required: (fieldName) => `${fieldName} is required.`,
  tooLong: (fieldName, length) =>
    `${fieldName} can't be longer than ${length} characters.`,
  tooShort: (fieldName, length) =>
    `${fieldName} must be at least ${length} characters long.`,
  badEmail: () => "Please enter a valid email address.",
}

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

  if (form.name.value.length > form.name.maxlength) {
    form.name.error = errorMsg.tooLong(
      "Name",
      form.name.maxlength
    )
    return false
  }

  return true
}

/** Returns true if the company field is all of the following:
 * - shorter than maxlength
 * 
 * Otherwise, returns false and sets the field's validation label.
 * */
function validateCompany(form: FormData): boolean {
  if (form.company.value.length > form.company.maxlength) {
    form.company.error = errorMsg.tooLong(
      "Company name",
      form.company.maxlength
    )
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
  const emailRegexp = /[^@]+@[^.]+\..*/

  if (form.email.value.length === 0) {
    form.email.error = errorMsg.required("Email address")
    return false
  }

  if (form.email.value.length > form.email.maxlength) {
    form.email.error = errorMsg.tooLong(
      "Email address",
      form.email.maxlength
    )
    return false
  }

  if (!emailRegexp.test(form.email.value)) {
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
function validateMessageContent(form: FormData): boolean {
  if (form.messageContent.value.length < form.messageContent.minlength) {
    form.messageContent.error = errorMsg.tooShort(
      "Message content",
      form.messageContent.minlength
    )
    return false
  }

  if (form.messageContent.value.length > form.messageContent.maxlength) {
    form.messageContent.error = errorMsg.tooLong(
      "Message content",
      form.messageContent.maxlength
    )
    return false
  }

  return true
}

