export { FormData, FormState, FormInputType }

type FieldWithValidation = {
  value: string
  error: string
}
type HasMinLength = { minlength: number }
type HasMaxLength = { maxlength: number }

interface FormData {
  name: FieldWithValidation & HasMaxLength
  company: FieldWithValidation & HasMaxLength
  email: FieldWithValidation & HasMaxLength
  messageContent: FieldWithValidation & HasMaxLength & HasMinLength
}

enum FormState {
  ReadyForInput = "ready",
  SubmissionPending = "pending",
  Success = "success",
  Error = "error",
}

type FormInputType = "textarea" | "text" | "number" | "email"