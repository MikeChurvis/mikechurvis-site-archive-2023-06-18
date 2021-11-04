<template>
  <form id="contact-form">
    <h1>{{ this.message }}</h1>
    <div class="row g-2">
      <div class="col-12 col-lg-5">
        <input
          required
          type="text"
          name="name"
          placeholder="Name"
          id="ct-form-name"
          class="form-control"
          autocomplete="off"
        />
        <label for="ct-form-name" class="visually-hidden">Name</label>
      </div>
      <div class="col-12 col-lg-7">
        <input
          type="text"
          name="company"
          placeholder="Company (optional)"
          id="ct-form-name"
          class="form-control"
          autocomplete="off"
        />
        <label for="ct-form-name" class="visually-hidden">Company</label>
      </div>
      <div class="col-12">
        <input
          required
          type="email"
          name="email"
          placeholder="Email"
          id="ct-form-email"
          class="form-control"
          autocomplete="off"
        />
        <label for="ct-form-email" class="visually-hidden">Email</label>
      </div>
      <div class="col-12">
        <textarea
          required
          name="message"
          placeholder="Message"
          id="ct-form-message"
          class="form-control"
        ></textarea>
        <label for="ct-form-message" class="visually-hidden">Message</label>
      </div>
      <div class="col-12">
        <button
          type="submit"
          class="btn btn-primary btn-lg"
          minlength="20"
          maxlength="1000"
        >
          Send
        </button>
      </div>
    </div>
  </form>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "ContactForm",
  data() {
    return {
      message: import.meta.env.VITE_HELLO_WORLD,
    };
  },
  methods: {
    onSubmit() {},
    onInvalid() {},
  },
});
</script>