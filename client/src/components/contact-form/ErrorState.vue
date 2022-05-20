<script setup lang="ts">
const props = defineProps<{
  message?: string
}>()
</script>

<template>
  <div class="p-5 alert alert-warning text-center error-state">
    <h1 class="mx-auto mb-3">Error</h1>
    <span v-if="message">{{ props.message }}</span>
    <span v-else>Something went wrong on our end. Please try again later.</span>
  </div>
</template>