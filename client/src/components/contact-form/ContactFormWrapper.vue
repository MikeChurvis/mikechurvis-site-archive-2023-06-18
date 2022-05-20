<script setup lang="ts">
import { onErrorCaptured, ref } from 'vue'
import ContactForm from './ContactForm.vue'
import ErrorState from './ErrorState.vue'
import LoadingState from './LoadingState.vue'
import type { FormConfig } from './types'

const props = defineProps<{
  apiRootUrl: string
}>()

const formEncounteredFatalError = ref(false)

onErrorCaptured((error) => {
  formEncounteredFatalError.value = true
  console.error(error)
  return false  // Stops error propagation here.
})

// const debugConfig: FormConfig = {
//   nameMaxLength: 100,
//   organizationMaxLength: 100,
//   emailMaxLength: 320,
//   emailRegex: '',
//   messageMinLength: 0,
//   messageMaxLength: 500
// }

</script>


<template>
  <div id="contact-form">
    <ErrorState v-if="formEncounteredFatalError" message="The server could not be reached at this time." />
    <Suspense>
      <ContactForm :api-root-url="props.apiRootUrl" />
      <template #fallback>
        <div>
          <LoadingState />
        </div>
      </template>
    </Suspense>
  </div>
</template>

