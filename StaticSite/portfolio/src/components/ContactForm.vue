<script lang="ts">
import { defineComponent } from "vue";
import FormInput from "@components/FormInput.vue";
import { postContactFormDataFactory } from "@scripts/contact-form";

const FormState = {
  ReadyForInput: "ready",
  SubmissionPending: "pending",
  Success: "success",
} as const;

export default defineComponent({
  name: "ContactForm",
  components: { FormInput },
  data() {
    return {
      FormState,
      formState: FormState.ReadyForInput,
      formDef: {
        name: {
          maxlength: 120,
        },
        company: {
          maxlength: 180,
        },
        email: {
          maxlength: 320,
        },
        content: {
          minlength: 20,
          maxlength: 1000,
        },
      },
      formData: {
        name: "",
        company: "",
        email: "",
        content: "",
      },
      errors: {
        name: "",
        company: "",
        email: "",
        content: "",
      },
      postFormData: postContactFormDataFactory(
        { ...this.$props }.target // spread-copy disables reactivity
      ),
    };
  },
  props: {
    target: { type: String, required: true },
  },
  methods: {
    submitForm: async function (): Promise<void> {
      this.formState = FormState.SubmissionPending;

      this.doClientValidation();

      if (Object.values(this.errors).some((err: string) => err.length > 0)) {
        this.formState = FormState.ReadyForInput;
        return;
      }

      const response = await this.postFormData(this.formData);

      if (response.ok) {
        this.formState = FormState.Success;
        return;
      }

      const responseBody = await response.json();

      this.reflectServerValidation(responseBody.errors);

      this.formState = FormState.ReadyForInput;
    },
    reflectServerValidation: function (responseErrors: object): void {
      for (const field in responseErrors) {
        this.errors[field] = responseErrors[field][0];
      }
    },
    doClientValidation: function (): void {
      const name = this.formData.name.trim();
      const company = this.formData.company.trim();
      const email = this.formData.email.trim();
      const content = this.formData.content.trim();

      this.formData.name = name;
      this.formData.company = company;
      this.formData.email = email;
      this.formData.content = content;

      const emailRegexp = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

      const errorMsg = {
        required: () => "This field is required.",
        badEmail: () => "Please enter a valid email address.",
        tooShort: (length: number) =>
          `Must contain at least ${length} characters.`,
        tooLong: (length: number) =>
          `May contain no more than ${length} characters.`,
      };

      if (name.length === 0) {
        this.errors.name = errorMsg.required();
      } else if (name.length > this.formDef.name.maxlength) {
        this.errors.name = errorMsg.tooLong(this.formDef.name.maxlength);
      }

      if (company.length > this.formDef.company.maxlength) {
        this.errors.company = errorMsg.tooLong(this.formDef.name.maxlength);
      }

      if (email.length === 0) {
        this.errors.email = errorMsg.required();
      } else if (email.length > this.formDef.email.maxlength) {
        this.errors.email = errorMsg.tooLong(this.formDef.email.maxlength);
      } else if (!emailRegexp.test(email)) {
        this.errors.email = errorMsg.badEmail();
      }

      if (content.length < this.formDef.content.minlength) {
        this.errors.content = errorMsg.tooShort(this.formDef.content.minlength);
      } else if (content.length > this.formDef.content.maxlength) {
        this.errors.content = errorMsg.tooLong(this.formDef.content.maxlength);
      }
    },
  },
});
</script>


<template>
  <div class="container-fluid">
    <div
      v-if="this.formState === this.FormState.Success"
      class="p-5 alert alert-success"
    >
      <h1 class="mx-auto text-center">Message Sent</h1>
    </div>

    <fieldset
      v-else
      v-bind:disabled="this.formState !== this.FormState.ReadyForInput"
    >
      <div class="row g-2">
        <div class="col-12">
          <form-input
            type="text"
            v-model:data="formData.name"
            v-model:error="errors.name"
            v-bind="{ id: 'contact-form-name', label: 'Name' }"
          />
        </div>

        <div class="col-12">
          <form-input
            type="text"
            v-model:data="formData.company"
            v-model:error="errors.company"
            v-bind="{
              id: 'contact-form-company',
              label: 'Company (optional)',
            }"
          />
        </div>

        <div class="col-12">
          <form-input
            type="email"
            v-model:data="formData.email"
            v-model:error="errors.email"
            v-bind="{ id: 'contact-form-email', label: 'Email' }"
          />
        </div>

        <div class="col-12">
          <form-input
            type="textarea"
            v-model:data="formData.content"
            v-model:error="errors.content"
            v-bind="{
              id: 'contact-form-content',
              label: 'Message',
              minlength: 20,
              maxlength: 1000,
              rows: 4,
            }"
          />
        </div>

        <div class="col-12">
          <button
            v-on:click="submitForm()"
            v-bind:class="
              this.formState === this.FormState.ReadyForInput
                ? 'btn-primary'
                : 'btn-secondary'
            "
            class="btn btn-lg"
          >
            <div
              v-if="this.formState !== this.FormState.ReadyForInput"
              class="spinner-border spinner-border-sm"
              role="status"
            ></div>
            {{
              this.formState === this.FormState.ReadyForInput
                ? "Submit"
                : "Submitting..."
            }}
          </button>
        </div>
      </div>
    </fieldset>
  </div>
</template>