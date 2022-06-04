import { describe, it, cy, expect } from 'local-cypress'


describe('The Navbar', () => {
  beforeEach(() => {
    cy.visit('/')
  })


  it('Sticks to the top of the page and is always visible no matter the scroll position.', () => {
    cy.get('#navbar').should('be.visible')
    cy.window().scrollTo('bottom')
    cy.get('#navbar').should('be.visible')
  })


  it('Has nav links that when clicked scroll to their respective position on the page. The nav link enters an active visual state when clicked.', () => {
    for (const navLinkContent of ['Home', 'About', 'Skills', 'Contact']) {
      cy.get('a.nav-link').contains(navLinkContent)
        .click()
        .should('have.class', 'active')
        .invoke('attr', 'href')
        .then(href => {
          cy.get(href).should('be.visible')
        })
    }
  })
  
  
  it('Automatically activates the appropriate nav link when its respective section is in view.', () => {
    cy.get('a.nav-link').each((navLink) => {
      const href = navLink.attr('href')
      cy.get(href).scrollIntoView()
      cy.get(`a.nav-link[href="${href}"]`).should('have.class', 'active')
    })
  })
})
