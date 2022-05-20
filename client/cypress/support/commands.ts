import type { HttpResponseInterceptor, StaticResponse } from "cypress/types/net-stubbing"
import { Cypress, cy } from "local-cypress"




Cypress.Commands.add(
  'interceptContactFormConfigRequest',
  (response: StaticResponse | HttpResponseInterceptor = {}) => {
    
    cy.intercept('GET', `${Cypress.env('apiRootUrl')}/contact/config`, (request) => { request.reply(response) })
  }
)