import { defineConfig } from 'astro/config'
import vue from '@astrojs/vue'
// import { astroImageTools } from 'astro-imagetools'

export default defineConfig({
  integrations: [
    vue(),
    // astroImageTools,
  ],
  packageOptions: {
    types: true,
  },
  site: "https://mikechurvis.com",
})
