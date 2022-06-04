<script setup lang="ts">

import { withDefaults, computed, useAttrs } from "vue"
import { FormInputType } from "@component:contact-form/types"
import { generateRandomId } from "@script:utils";

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
  (e: 'input', event: Event): void
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
  <textarea
    v-if="type == 'textarea'"
    v-model.trim="fieldValue"
    v-bind="attrs"
    :id="props.id"
    :placeholder="label"
    :class="{ 'is-invalid': error.length > 0 }"
    class="form-control"
    @blur="emit('blur', $event)"
    @input="emit('input', $event)"
  ></textarea>
  <input
    v-else
    v-model.trim="fieldValue"
    v-bind="attrs"
    :id="props.id"
    :type="type == 'email' ? 'text' : type"
    :placeholder="label"
    :class="{ 'is-invalid': error.length > 0 }"
    class="form-control"
    autocomplete="off"
    @blur="emit('blur', $event)"
    @input="emit('input', $event)"
  />

  <!-- 
    An <input> reserves its space when empty. I use it as a
    validation label to prevent the form from suddenly resizing
    when error text appears.

    This is an important accessibility concern, especially for
    people who prefer reduced UI motion for medical reasons.
  -->
  <input
    :data-validates="`#${props.id}`"
    readonly
    disabled
    tabindex="-1"
    class="invalid-feedback form-control-plaintext p-0 mx-0 mt-0"
    :value="error"
  />
</template>


