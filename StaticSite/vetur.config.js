// vetur.config.js
/** @type {import('vls').VeturConfig} */
module.exports = {
    settings: {
      "vetur.useWorkspaceDependencies": true,
      "vetur.experimental.templateInterpolationService": false,
    },
    projects: [
      {
        root: './portfolio',
        package: './package.json',
        tsconfig: './tsconfig.json',
        snippetFolder: './.vscode/vetur/snippets',
        globalComponents: [
          './src/components/**/*.vue'
        ]
      }
    ]
  }