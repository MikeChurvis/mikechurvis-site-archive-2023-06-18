<script lang="ts">
import { defineComponent, PropType } from "vue";

type InputAttributeType = "textarea" | "text" | "number" | "email";
type InputAttributeDictionary = {
  [Type in InputAttributeType]?: any;
};

export default defineComponent({
  name: "FormInput",
  props: {
    data: { type: null },
    type: {
      type: String as PropType<InputAttributeType>,
      required: true,
    },
    error: {
      type: String,
      default: "",
    },
  },
  emits: ["update:data", "update:error"],
  inheritAttrs: false,
  computed: {
    _data: {
      get() {
        return this.data;
      },
      set(value) {
        this.$emit("update:data", value);
        this.$emit("update:error", ""); // reset validation on input
      },
    },
    attrs() {
      const commonAttrNames = [
        "id",
        "name",
        "ref",
        "label",
        "standaloneLabel",
        "placeholder",
      ];

      const typeSpecificAttrNames: InputAttributeDictionary = {
        textarea: ["minlength", "maxlength", "rows"],
        text: ["minlength", "maxlength"],
      };

      const allAttrNames = new Set([
        ...commonAttrNames,
        ...(typeSpecificAttrNames[this.type] ?? []),
      ]);

      const applicableAttrNames = new Set(
        Array.from(allAttrNames).filter((attrName) =>
          this.$attrs.hasOwnProperty(attrName)
        )
      );

      let applicableAttrs = {};

      applicableAttrNames.forEach((attrName) => {
        applicableAttrs[attrName] = this.$attrs[attrName];
      });

      return applicableAttrs;
    },
  },
});
</script>


<style>
textarea.form-control {
  resize:vertical;
  min-height: 7em;
}
</style>




<template>
  <label
    v-bind:for="attrs.id"
    v-bind:class="{ 'visually-hidden': !attrs.standaloneLabel }"
    class="form-control-label"
  >
    {{ attrs.label }}
  </label>

  <!-- regression bug in chrome version 40+: 
    input[type=email] will not update its visual appearance
    when its value is trimmed. This is a known issue:
    https://bugs.chromium.org/p/chromium/issues/detail?id=423785
  
    For now, we'll fall back on [type=text] for email inputs.
    We have custom email field validation, so the browser
    default behavior has no effect either way.
  -->
  <input
    v-if="type !== 'textarea'"
    v-model.trim="_data"
    v-bind:type="type !== 'email' ? type : 'text'"
    v-bind:placeholder="attrs.standaloneLabel ? attrs.placeholder ?? '' : attrs.label"
    v-bind="attrs"
    v-bind:class="{ 'is-invalid': error.length > 0 }"
    class="form-control"
    autocomplete="off"
  />
  <textarea
    v-else
    v-model.trim="_data"
    v-bind:placeholder="attrs.standaloneLabel ? attrs.placeholder ?? '' : attrs.label"
    v-bind="attrs"
    v-bind:class="{ 'is-invalid': error.length > 0 }"
    class="form-control"
  />

  <input 
    readonly
    disabled 
    tabindex="-1"
    class="invalid-feedback form-control-plaintext p-0 mx-0 mt-0" 
    v-bind:value="error" 
  />
</template>


