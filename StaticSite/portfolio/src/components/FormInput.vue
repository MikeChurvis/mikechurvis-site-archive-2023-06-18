<script setup lang="ts">

import { withDefaults, computed, useAttrs } from "vue"
import { FormInputType } from "@/scripts/contact-form/types"
import { generateRandomId } from "@/scripts/utils";

// ATTRIBUTES ////

const props = withDefaults(defineProps<{
  type: FormInputType
  label: string
  value?: any
  error?: string
  id?: string
}>(), {
  type: "text",
  // value: "",
  error: "",
  id: generateRandomId(),
})

const attrs = useAttrs()

// EMITTED EVENTS ////

const emit = defineEmits<{
  (e: 'update:value', newValue: any): void
  (e: 'update:error', newError: string): void
  (e: 'blur', event: FocusEvent): void
}>()

// COMPUTED VALUES ////

const fieldValue = computed({
  get: () => props.value,
  set: (newValue) => {
    emit('update:value', newValue)
    emit('update:error', "") // Reset validation on input.
  }
})

</script>


<style>
textarea.form-control {
  resize: vertical;
  min-height: 7em;
}
</style>


<template>
  <label v-bind:for="id" class="form-control-label visually-hidden">{{ label }}</label>

  <!-- 
    REGRESSION BUG in Chromium version 40+: 
    
    input[type=email] will not update its visual appearance
    when its value is trimmed. This is a known issue:
    https://bugs.chromium.org/p/chromium/issues/detail?id=423785
  
    For now we'll fall back on [type=text] for email inputs.
    Our custom email field validation overrides the browser
    default behavior anyway.
  -->
  <input
    v-if="type !== 'textarea'"
    v-model.trim="fieldValue"
    v-on:blur="emit('blur', $event)"
    v-bind:type="type !== 'email' ? type : 'text'"
    v-bind:placeholder="label"
    v-bind:class="{ 'is-invalid': error.length > 0 }"
    v-bind="attrs"
    class="form-control"
    autocomplete="off"
  />
  <textarea
    v-else
    v-model.trim="fieldValue"
    v-on:blur="emit('blur', $event)"
    v-bind:placeholder="label"
    v-bind:class="{ 'is-invalid': error.length > 0 }"
    v-bind="attrs"
    class="form-control"
  ></textarea>

  <input
    readonly
    disabled
    tabindex="-1"
    class="invalid-feedback form-control-plaintext p-0 mx-0 mt-0"
    v-bind:value="error"
  />
</template>


