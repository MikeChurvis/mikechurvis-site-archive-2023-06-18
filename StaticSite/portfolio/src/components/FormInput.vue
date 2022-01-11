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

<template>
  <label
    :for="attrs.id"
    :class="{ 'visually-hidden': !attrs.standaloneLabel }"
    class="form-control-label"
  >
    {{ attrs.label }}
  </label>

  <!-- regression bug in chrome version 40+: 
    input[type=email] will not update its visual appearance
    when its value is trimmed. This is a known issue:
    https://bugs.chromium.org/p/chromium/issues/detail?id=423785
  
    For now, we'll fall back on [type=text] for email inputs.
  -->
  <input
    v-if="type !== 'textarea'"
    v-model.trim="_data"
    :type="type !== 'email' ? type : 'text'"
    :placeholder="attrs.standaloneLabel ? attrs.placeholder ?? '' : attrs.label"
    v-bind="attrs"
    :class="{ 'is-invalid': error.length > 0 }"
    class="form-control"
  />
  <textarea
    v-else
    v-model.trim="_data"
    :placeholder="attrs.standaloneLabel ? attrs.placeholder ?? '' : attrs.label"
    v-bind="attrs"
    :class="{ 'is-invalid': error.length > 0 }"
    class="form-control"
  />

  <div class="invalid-feedback">{{ error }}</div>
</template>