import { describe, it, cy, expect } from 'local-cypress'


describe('The Contact Form', () => {

  it('Can be accessed by scrolling to the Contact section of the Landing Page.', () => {
    cy.visit('#contact')
    cy.get('#contact-form').should('be.visible')
  })


  it('Requests configuration data from the API, and shows a Loading placeholder while it waits for a response.', () => {
    cy.interceptContactFormConfigRequest()

    cy.visit('#contact')
    cy.get('#contact-form .loading-state').should('be.visible')
  })


  it('Displays an Error placeholder when the API does not respond with OK to a request for config data.', () => {
    cy.interceptContactFormConfigRequest({
      forceNetworkError: true
    })

    cy.visit('#contact')
    cy.get('#contact-form .error-state').should('be.visible')
  })


  it('Displays an Error placeholder when the API responds with invalid config data.', () => {
    cy.interceptContactFormConfigRequest({
      statusCode: 200,
      body: {
        foo: "bar"
      }
    })

    cy.visit('#contact')
    cy.get('#contact-form .error-state').should('be.visible')
  })


  it('Displays the contact form\'s input fields when the API responds with valid config data.', () => {
    cy.interceptContactFormConfigRequest({
      statusCode: 200,
      fixture: 'contact-form-config-response.json'
    })

    cy.visit('#contact')
    cy.get('#contact-form fieldset').should('be.visible')
  })
})



describe('The Contact Form (given valid config data)', () => {
  beforeEach(() => {
    cy.interceptContactFormConfigRequest({
      statusCode: 200,
      fixture: 'contact-form-config-response.json'
    }).as('configResponse')
    cy.visit('#contact')
    cy.wait('@configResponse')

  })


  it('Has fields for name, organization, email, and message, all of which are visible and focusable.', () => {
    for (const field of ['name', 'organization', 'email', 'message']) {
      cy.get(`#contact-form__${field}`)
        .should('be.visible')
        .click()
        .should('be.focused')
    }
  })


  it('Shows validation text under each required field when the user focuses and then un-focuses the field.', () => {
    for (const requiredField of ['name', 'email', 'message']) {
      const fieldId = `#contact-form__${requiredField}`
      const fieldNameRegExp = new RegExp(requiredField, 'i')

      cy.get(fieldId)
        .focus()
        .blur()

      cy.get(`[data-validates="${fieldId}"]`).should((validationLabel) => {
        expect(validationLabel.val()).to.match(fieldNameRegExp)
      })
    }
  })
})