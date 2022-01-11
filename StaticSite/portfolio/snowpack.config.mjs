export default {
  plugins: [
    '@snowpack/plugin-dotenv',
    '@snowpack/plugin-typescript',
  ],
  packageOptions: {
    types: true,
  },
  buildOptions: {
    out: "dist",
    sourcemap: true,
  },
  alias: {
    '@': './src/',
  }
}