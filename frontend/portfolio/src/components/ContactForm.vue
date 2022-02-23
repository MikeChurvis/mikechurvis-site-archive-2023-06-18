<script setup lang="ts">

import { ref, reactive, withDefaults } from "vue"
import FormInput from "@/components/FormInput.vue"
import {
  validateName,
  validateCompany,
  validateEmail,
  validateMessageContent,
} from "@/scripts/contact-form/validators"
import {
  cleanNameFieldInput,
  cleanCompanyFieldInput,
  cleanEmailFieldInput,
} from "@/scripts/contact-form/field-input-cleaners"
import { FormData, FormState } from "@/scripts/contact-form/types"

// ATTRIBUTES ////

const props = withDefaults(defineProps<{
  target: string
  origin?: string
  overrides?: {
    name?: {
      maxlength?: number
    },
    company?: {
      maxlength?: number
    },
    email?: {
      maxlength?: number,
      regex?: string
    },
    messagecontent?: {
      minlength?: number,
      maxlength?: number
    }
  }
}>(), {
  origin: 'http://localhost:3000/'
})

// DATA ////

const formState = ref(FormState.ReadyForInput)

const form: FormData = reactive({
  name: {
    value: "",
    error: "",
    maxlength: props.overrides?.name?.maxlength ?? 120,
  },
  company: {
    value: "",
    error: "",
    maxlength: props.overrides?.company?.maxlength ?? 180,
  },
  email: {
    value: "",
    error: "",
    maxlength: props.overrides?.company?.maxlength ?? 320,
  },
  messageContent: {
    value: "",
    error: "",
    minlength: props.overrides?.messagecontent?.minlength ?? 20,
    maxlength: props.overrides?.messagecontent?.maxlength ?? 1000,
  },
})

// METHODS ////

/** 
 * Validates all fields and sends the form data to the server. 
 */
async function submitForm(): Promise<void> {
  formState.value = FormState.SubmissionPending

  const allFieldsAreValid = [
    validateName(form),
    validateCompany(form),
    validateEmail(form, props.overrides?.email?.regex),
    validateMessageContent(form),
  ].every((fieldIsValid) => fieldIsValid)

  if (!allFieldsAreValid) {
    formState.value = FormState.ReadyForInput
    return
  }

  const formValues = {
    name: form.name.value,
    company: form.company.value,
    email: form.email.value,
    messageContent: form.messageContent.value,
  }

  let response: Response

  try {
    response = await fetch(props.target, {
      method: "POST",
      headers: {
        "Access-Control-Allow-Origin": props.origin,
      },
      credentials: "same-origin",
      body: JSON.stringify(formValues),
    })
  } catch (networkError) {
    formState.value = FormState.Error
    console.warn(networkError)
    return
  }

  if (!response.ok) {
    const responseBody = await response.json()

    if (!responseBody.hasOwnProperty("errors")) {
      console.warn("Invalid response from server. Response body:")
      console.warn(responseBody)
      formState.value = FormState.Error
      return
    }

    displayServerValidationErrorsInForm(responseBody.errors)
    formState.value = FormState.ReadyForInput
    return
  }

  formState.value = FormState.Success
}

/** 
 * Populates field validation labels with their respective error text. 
 */
function displayServerValidationErrorsInForm(errors: any): void {
  for (const field in errors) {
    // errors: { 'field': ['error1', 'error2', ...], ... }
    form[field].error = errors[field][0]
  }
}

</script>


<template>
  <div v-if="formState === FormState.Success" class="p-5 alert alert-success text-center">
    <h1 class="mx-auto mb-3">Message Sent</h1>
    <span>I'll reply to you via email as soon as I can.</span>
    <br />
    <span>Thanks for stopping by!</span>
  </div>

  <div v-else-if="formState === FormState.Error" class="p-5 alert alert-warning text-center">
    <h1 class="mx-auto mb-3">Error</h1>
    <span>Something went wrong on our end.</span>
    <br />
    <span>Please try again later.</span>
  </div>

  <fieldset v-else :disabled="formState !== FormState.ReadyForInput">
    <div class="row g-2">
      <div class="col-12">
        <FormInput
          type="text"
          v-model:value="form.name.value"
          v-model:error="form.name.error"
          id="contact-form-name"
          label="Name"
          :maxlength="form.name.maxlength"
          @blur="validateName(form)"
          @input="cleanNameFieldInput"
        />
      </div>

      <div class="col-12">
        <FormInput
          label="Company (optional)"
          type="text"
          id="contact-form-company"
          v-model:value="form.company.value"
          v-model:error="form.company.error"
          :maxlength="form.company.maxlength"
          @blur="validateCompany(form)"
          @input="cleanCompanyFieldInput"
        />
      </div>

      <div class="col-12">
        <FormInput
          label="Email"
          type="email"
          id="contact-form-email"
          v-model:value="form.email.value"
          v-model:error="form.email.error"
          :maxlength="form.email.maxlength"
          @blur="validateEmail(form)"
          @input="cleanEmailFieldInput"
        />
      </div>

      <div class="col-12">
        <FormInput
          label="Message"
          type="textarea"
          id="contact-form-messagecontent"
          v-model:value="form.messageContent.value"
          v-model:error="form.messageContent.error"
          :minlength="form.messageContent.minlength"
          :maxlength="form.messageContent.maxlength"
          :rows="4"
          @blur="validateMessageContent(form)"
        />
      </div>

      <div class="col-12">
        <button
          @click="submitForm()"
          :class="
            formState === FormState.ReadyForInput
              ? 'btn-primary'
              : 'btn-secondary'
          "
          class="btn btn-lg w-100 mt-1"
        >
          <div
            v-if="formState !== FormState.ReadyForInput"
            class="spinner-border spinner-border-sm"
            role="status"
          ></div>
          {{
            formState === FormState.ReadyForInput
              ? "Submit"
              : "Submitting..."
          }}
        </button>
      </div>
    </div>
  </fieldset>
</template>