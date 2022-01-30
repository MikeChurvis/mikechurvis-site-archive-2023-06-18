<script setup lang="ts">

import { ref, reactive, withDefaults } from "vue"
import FormInput from "@/components/FormInput.vue"
import {
  validateName,
  validateCompany,
  validateEmail,
  validateMessageContent,
} from "@/scripts/contact-form/validation"
import { FormData, FormState } from "@/scripts/contact-form/types"

// PROPERTIES ////

const props = withDefaults(defineProps<{
  target: string
  origin?: string
}>(), {
  origin: 'http://localhost:3000/'
})

// DATA ////

const formState = ref(FormState.ReadyForInput)

const form: FormData = reactive({
  name: {
    value: ref(""),
    error: ref(""),
    maxlength: ref(120),
  },
  company: {
    value: ref(""),
    error: ref(""),
    maxlength: ref(180),
  },
  email: {
    value: ref(""),
    error: ref(""),
    maxlength: ref(320),
  },
  messageContent: {
    value: ref(""),
    error: ref(""),
    minlength: ref(20),
    maxlength: ref(1000),
  },
})

// METHODS ////

async function submitForm(): Promise<void> {
  formState.value = FormState.SubmissionPending

  const allFieldsAreValid = [
    validateName(form),
    validateCompany(form),
    validateEmail(form),
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

    if (!responseBody.hasOwnProperty("validation_errors")) {
      console.warn("Invalid response from server. Response body:")
      console.warn(responseBody)
      formState.value = FormState.Error
      return;
    }

    displayServerValidationErrorsInForm(responseBody.validation_errors)
    formState.value = FormState.ReadyForInput
    return
  }

  formState.value = FormState.Success
}

function displayServerValidationErrorsInForm(errors: any): void {
  for (const field in errors) {
    // errors: { 'field': ['error1', 'error2', ...], ... }
    form[field].error = errors[field][0]
  }
}

</script>


<template>
  <div v-if="formState === FormState.Success" class="p-5 alert alert-success text-center">
    <h1 class="mx-auto mb-3">Message Sent</h1>I'll reply to you via email as soon as I can.
    <br />Thanks for stopping by!
  </div>

  <div v-else-if="formState === FormState.Error" class="p-5 alert alert-warning text-center">
    <h1 class="mx-auto mb-3">Error</h1>Something went wrong on our end.
    <br />Please try again later.
  </div>

  <fieldset v-else v-bind:disabled="formState !== FormState.ReadyForInput">
    <div class="row g-2">
      <div class="col-12">
        <FormInput
          type="text"
          v-model:data="form.name.value"
          v-model:error="form.name.error"
          v-on:blur="validateName(form)"
          v-bind="{
            id: 'contact-form-name',
            label: 'Name',
            maxlength: form.name.maxlength,
          }"
        />
      </div>

      <div class="col-12">
        <FormInput
          type="text"
          v-model:data="form.company.value"
          v-model:error="form.company.error"
          v-on:blur="validateCompany(form)"
          v-bind="{
            id: 'contact-form-company',
            label: 'Company (optional)',
            maxlength: form.company.maxlength,
          }"
        />
      </div>

      <div class="col-12">
        <FormInput
          type="email"
          v-model:data="form.email.value"
          v-model:error="form.email.error"
          v-on:blur="validateEmail(form)"
          v-bind="{ id: 'contact-form-email', label: 'Email' }"
        />
      </div>

      <div class="col-12">
        <FormInput
          type="textarea"
          v-model:data="form.messageContent.value"
          v-model:error="form.messageContent.error"
          v-on:blur="validateMessageContent(form)"
          v-bind="{
            id: 'contact-form-messagecontent',
            label: 'Message',
            minlength: form.messageContent.minlength,
            maxlength: form.messageContent.maxlength,
            rows: 4,
          }"
        />
      </div>

      <div class="col-12">
        <button
          v-on:click="submitForm()"
          v-bind:class="
            formState === FormState.ReadyForInput
              ? 'btn-primary'
              : 'btn-secondary'
          "
          class="btn btn-lg"
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