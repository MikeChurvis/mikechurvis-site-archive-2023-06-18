<script lang="ts">
import { defineComponent } from "vue";
import FormInput from "@/components/FormInput.vue";
import {
  validateName,
  validateCompany,
  validateEmail,
  validateMessageContent,
} from "@/scripts/contact-form/validation";

enum FormState {
  ReadyForInput = "ready",
  SubmissionPending = "pending",
  Success = "success",
  Error = "error",
}

export default defineComponent({
  name: "ContactForm",
  components: { FormInput },
  data() {
    return {
      FormState, // allows the FormState type to be used in the markup.

      formState: FormState.ReadyForInput,

      form: {
        name: {
          value: "",
          error: "",
          maxlength: 120,
        },
        company: {
          value: "",
          error: "",
          maxlength: 180,
        },
        email: {
          value: "",
          error: "",
          maxlength: 320,
        },
        messageContent: {
          value: "",
          error: "",
          minlength: 20,
          maxlength: 1000,
        },
      },
    };
  },
  props: {
    target: {
      type: String,
      required: true,
    },
  },
  methods: {
    validateName,
    validateCompany,
    validateEmail,
    validateMessageContent,
    submitForm: async function (): Promise<void> {
      this.formState = FormState.SubmissionPending;

      const allFieldsAreValid = [
        this.validateName(),
        this.validateCompany(),
        this.validateEmail(),
        this.validateMessageContent(),
      ].every((fieldIsValid) => fieldIsValid);

      if (!allFieldsAreValid) {
        this.formState = FormState.ReadyForInput;
        return;
      }

      const formData = {
        name: this.form.name.value,
        company: this.form.company.value,
        email: this.form.email.value,
        messageContent: this.form.messageContent.value,
      };

      let response: Response;

      try {
        response = await fetch(this.target, {
          method: "POST",
          headers: {
            "Access-Control-Allow-Origin": origin,
          },
          credentials: "same-origin",
          body: JSON.stringify(formData),
        });
      } catch (networkError) {
        this.formState = FormState.Error;
        console.warn(networkError);
        return;
      }

      if (!response.ok) {
        const responseBody = await response.json();

        if (!responseBody.hasOwnProperty("validation_errors")) {
          console.warn("Invalid response from server. Response body:");
          console.warn(responseBody);
          this.formState = FormState.Error;
          return;
        }

        this.reflectServerValidationErrors(responseBody.validation_errors);
        this.formState = FormState.ReadyForInput;
        return;
      }

      this.formState = FormState.Success;
    },
    reflectServerValidation: function (errors: any): void {
      for (const field in errors) {
        // errors: { 'field': ['error1', 'error2', ...], ... }
        this.form[field].error = errors[field][0];
      }
    },
  },
});
</script>


<template>
  <div
    v-if="formState === FormState.Success"
    class="p-5 alert alert-success text-center"
  >
    <h1 class="mx-auto mb-3">Message Sent</h1>

    I'll reply to you via email as soon as I can.
    <br />
    Thanks for stopping by!
  </div>

  <div
    v-else-if="formState === FormState.Error"
    class="p-5 alert alert-warning text-center"
  >
    <h1 class="mx-auto mb-3">Error</h1>

    Something went wrong on our end.
    <br />
    Please try again later.
  </div>

  <fieldset v-else v-bind:disabled="formState !== FormState.ReadyForInput">
    <div class="row g-2">
      <div class="col-12">
        <FormInput
          type="text"
          v-model:data="form.name.value"
          v-model:error="form.name.error"
          v-on:blur="validateName()"
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
          v-on:blur="validateCompany()"
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
          v-on:blur="validateEmail()"
          v-bind="{ id: 'contact-form-email', label: 'Email' }"
        />
      </div>

      <div class="col-12">
        <FormInput
          type="textarea"
          v-model:data="form.messageContent.value"
          v-model:error="form.messageContent.error"
          v-on:blur="validateContent()"
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
            formState === FormState.ReadyForInput ? "Submit" : "Submitting..."
          }}
        </button>
      </div>
    </div>
  </fieldset>
</template>