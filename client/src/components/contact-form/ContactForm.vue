<script setup lang="ts">
import { ref } from "vue"
import type { Ref } from "vue"

import FormInput from "@component:FormInput.vue"
import ErrorState from "./ErrorState.vue"

import { generateFormAPIMethods } from "./api-calls"
import { generateValidators } from "./validators"
import { FormState } from "./types"
import type { FormData, FormConfig } from "./types"
import { cleanNameFieldInput, cleanOrganizationFieldInput, cleanEmailFieldInput } from "./field-input-cleaners"
import SuccessState from "./SuccessState.vue"


// COMPONENT DATA ////

const props = defineProps<{
  apiRootUrl: string
  debugConfig?: FormConfig
}>()

const formState = ref(FormState.Loading)
const formAPI = generateFormAPIMethods(props.apiRootUrl)
const formConfig = props.debugConfig ?? (await formAPI.getFormConfig())
const formValidators = generateValidators(formConfig)
const formData: Ref<FormData> = ref({
  name: {
    value: "",
    error: "",
  },
  organization: {
    value: "",
    error: "",
  },
  email: {
    value: "",
    error: "",
  },
  message: {
    value: "",
    error: "",
  },
})

formState.value = FormState.Ready


// METHODS ////

/** 
 * Validates all fields and sends the form data to the server. 
 */
async function submitForm(): Promise<void> {
  formState.value = FormState.Sending

  let allFieldsAreValid = [
    formValidators.validateName(formData.value),
    formValidators.validateOrganization(formData.value),
    formValidators.validateEmail(formData.value),
    formValidators.validateMessage(formData.value),
  ].every((fieldIsValid) => fieldIsValid)

  if (!allFieldsAreValid) {
    formState.value = FormState.Ready
    return
  }

  try {
    allFieldsAreValid = await formAPI.postFormData(formData.value)
  } catch (networkError) {
    formState.value = FormState.FatalError
    console.error(networkError)
    return
  }

  if (!allFieldsAreValid) {
    formState.value = FormState.Ready
    return
  }

  formState.value = FormState.Success
}
</script>


<template>
  <SuccessState v-if="formState === FormState.Success" />
  <ErrorState v-if="formState === FormState.FatalError" />

  <fieldset v-else :disabled="formState !== FormState.Ready">
    <div class="row g-2">
      <div class="col-12">
        <FormInput
          type="text"
          v-model:value="formData.name.value"
          v-model:error="formData.name.error"
          id="contact-form-name"
          label="Name"
          :maxlength="formConfig.nameMaxLength"
          @blur="formValidators.validateName(formData)"
          @input="cleanNameFieldInput"
        />
      </div>

      <div class="col-12">
        <FormInput
          label="Organization (optional)"
          type="text"
          id="contact-form-organization"
          v-model:value="formData.organization.value"
          v-model:error="formData.organization.error"
          :maxlength="formConfig.organizationMaxLength"
          @blur="formValidators.validateOrganization(formData)"
          @input="cleanOrganizationFieldInput"
        />
      </div>

      <div class="col-12">
        <FormInput
          label="Email"
          type="email"
          id="contact-form-email"
          v-model:value="formData.email.value"
          v-model:error="formData.email.error"
          :maxlength="formConfig.emailMaxLength"
          @blur="formValidators.validateEmail(formData)"
          @input="cleanEmailFieldInput"
        />
      </div>

      <div class="col-12">
        <FormInput
          label="Message"
          type="textarea"
          id="contact-form-message"
          v-model:value="formData.message.value"
          v-model:error="formData.message.error"
          :minlength="formConfig.messageMinLength"
          :maxlength="formConfig.messageMaxLength"
          :rows="4"
          @blur="formValidators.validateMessage(formData)"
        />
      </div>

      <div class="col-12">
        <button
          @click="submitForm()"
          :class="
            formState === FormState.Ready
              ? 'btn-primary'
              : 'btn-secondary'
          "
          class="btn btn-lg w-100 mt-1"
        >
          <div
            v-if="formState !== FormState.Ready"
            class="spinner-border spinner-border-sm"
            role="status"
          ></div>
          {{
            formState === FormState.Ready
              ? "Submit"
              : "Submitting..."
          }}
        </button>
      </div>
    </div>
  </fieldset>
</template>