declare namespace Cypress {
  interface Chainable<Subject = any> {
    interceptContactFormConfigRequest(
      response?: import('cypress/types/net-stubbing').StaticResponse
        | import('cypress/types/net-stubbing').HttpResponseInterceptor
    ): Chainable<null>
  }
}