export { FormState }
export type { FormData, FormInputType, FormConfig }

enum FormState {
  Loading,
  Ready,
  FatalError,
  Sending,
  Success
}

type FieldWithValidation = {
  value: string
  error: string
}

type FormConfig = {
  nameMaxLength: number
  organizationMaxLength: number
  emailMaxLength: number
  emailRegex: string
  messageMinLength: number
  messageMaxLength: number
}

interface FormData {
  name: FieldWithValidation
  organization: FieldWithValidation
  email: FieldWithValidation
  message: FieldWithValidation
}


type FormInputType = "textarea" | "text" | "number" | "email"

