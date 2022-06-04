export { cleanNameFieldInput, cleanOrganizationFieldInput, cleanEmailFieldInput }


function cleanNameFieldInput(event: InputEvent): void {
  const nameField = event.target as HTMLInputElement

  let cleanedName = nameField.value
    .replace(/\s/g, " ")    // Standardize all whitespace to spaces.
    .replace(/\s\s+/g, " ") // Prevent more than one consecutive space.
    .replace(/^\s+/g, "")   // Prevent leading whitespace.

  nameField.value = cleanedName
}

function cleanOrganizationFieldInput(event: InputEvent): void {
  const companyField = event.target as HTMLInputElement

  let cleanedCompany = companyField.value
    .replace(/\s/g, " ")    // Standardize all whitespace to spaces.
    .replace(/\s\s+/g, " ") // Prevent more than one consecutive space.
    .replace(/^\s+/g, "")   // Prevent leading whitespace.

  companyField.value = cleanedCompany
}

function cleanEmailFieldInput(event: InputEvent): void {
  const emailField = event.target as HTMLInputElement

  let cleanedEmail = emailField.value
    .replace(/\s/g, "") // Prevent all whitespace.

  emailField.value = cleanedEmail
}

// function cleanMessageContentFieldInput(messageContent: string): string {

// }