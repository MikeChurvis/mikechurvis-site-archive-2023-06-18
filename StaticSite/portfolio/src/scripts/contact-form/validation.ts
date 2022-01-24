const errorMsg = {
  required: (fieldName) => `${fieldName} is required.`,
  tooLong: (fieldName, length) =>
    `${fieldName} can't be longer than ${length} characters.`,
  tooShort: (fieldName, length) =>
    `${fieldName} must be at least ${length} characters long.`,
  badEmail: () => "Please enter a valid email address.",
};

function validateName(): boolean {
  if (this.form.name.value.length === 0) {
    this.form.name.error = errorMsg.required("Name");
    return false;
  }

  if (this.form.name.value.length > this.form.name.maxlength) {
    this.form.name.error = errorMsg.tooLong(
      "Name",
      this.form.name.maxlength
    );
    return false;
  }

  return true;
}

function validateCompany(): boolean {
  if (this.form.company.value.length > this.form.company.maxlength) {
    this.form.company.error = errorMsg.tooLong(
      "Company name",
      this.form.company.maxlength
    );
    return false;
  }

  return true;
}

function validateEmail(): boolean {
  const emailRegexp = /[^@]+@[^.]+\..*/;

  if (this.form.email.value.length === 0) {
    this.form.email.error = errorMsg.required("Email address");
    return false;
  }

  if (this.form.email.value.length > this.form.email.maxlength) {
    this.form.email.error = errorMsg.tooLong(
      "Email address",
      this.form.email.maxlength
    );
    return false;
  }

  if (!emailRegexp.test(this.form.email.value)) {
    this.form.email.error = errorMsg.badEmail();
    return false;
  }

  return true;
}

function validateContent(): boolean {
  if (this.form.content.value.length < this.form.content.minlength) {
    this.form.content.error = errorMsg.tooShort(
      "Message content",
      this.form.content.minlength
    );
    return false;
  }

  if (this.form.content.value.length > this.form.content.maxlength) {
    this.form.content = errorMsg.tooLong(
      "Message content",
      this.form.content.maxlength
    );
    return false;
  }

  return true;
}

export { validateName, validateCompany, validateEmail, validateContent }