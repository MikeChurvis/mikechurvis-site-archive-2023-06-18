# Skill Grid

## Todo List

### Icons for the Grid

- [x] Django
- [x] Vue
- [x] Tailwind

- [x] Pytest
- [x] Vitest
- [x] Cypress

- [x] Python
- [x] TypeScript
- [x] CSS

- [x] Mobile-First Design
- [x] Accessibility-First Design
- [x] Behavior-Driven Development
- [x] 12-Factor App Methodology
- [x] Continuous Integration / Delivery

- [x] VS Code
- [x] PyCharm
- [x] Docker
- [x] DigitalOcean
- [x] Astro
- [x] Nginx


aaaee
bbbee
cccee
ddddd


### Logos for the Description Card

- [x] Django
- [x] Vue
- [x] Tailwind
- [x] Astro
- [x] Cypress
- [x] Pytest
- [x] Python
- [x] TypeScript
- [x] CSS
- [x] 12-Factor Methodology
- [x] VS Code
- [x] PyCharm
- [x] Docker
- [x] GitHub Pages
- [x] Nginx

### Descriptions

Frameworks
- Django
	- A batteries-included framework for writing web apps in Python. I used it to create this portfolio's API.
- Vue 3
	- A Javascript framework for building frontend UIs. I use it for components that require interactivity or state, like this interactive skill grid and the contact form at the bottom of the page.
- TailwindCSS
	- A utility-first CSS framework known for its ease of composition and customization. Its inline, no-fluff nature make it great for styling components. 

Test Frameworks
- Cypress
	- A Javascript test framework for cross-browser End-to-End integration tests. I use it to automate UX testing and to facilitate Behavior-Driven Development.
- Pytest
	- A Python test framework with an idiomatic writing style and detailed debug info. I use it for both unit and integration tests of the Django API.
- Vitest
	- A Javascript test framework I use for frontend unit tests. I use it because it's fast, integrates seamlessly with my build engine, and has the same Chai assertion library as Cypress.

Languages
- Python
	- A popular high-level interpreted language with a library for just about everything. I use it through the Django framework to write my site's API.
- TypeScript
	- A superset of Javascript created by Microsoft that offers static typing and robust code analysis. I use it to write tests and logic for my site's frontend.
- CSS
	- Cascading Style Sheets. No introduction necessary; if it's on the web and it's visible, odds are it's styled with CSS. I use it via the TailwindCSS framework to style my site.

Practices
- Mobile-First Design
	- A design philosophy that develops the mobile device user experience first, then progressively expands the layout and feature set to accomodate larger screens and richer modes of interface. In practice I've found that Mobile-First Design helps me create a lean, content-focused, accessible user experience on all platforms, not just mobile ones.
- Accessibility-First Design
	- I built this site from the ground up with semantic HTML5 tags, ARIA attributes, high-contrast color schemes, automated keyboard accessibility testing, and manual screen reader testing. Why? Because over 8.1 million Americans have severely impaired vision, forcing 7.3 million of them to rely on screen readers to access the web. A mere 10% of websites are fully accessible to the visually impaired; by adhering to the Web Content Accessibility Guidelines (WCAG 2.0), I guarantee that my site will always be one of them.
- Behavior-Driven Development (BDD)
	- A type of Test-Driven Development that promotes writing component and end-to-end tests as human-readable behavior specifications. I practice this with Cypress's BDD assertion API; every component and site feature has a corresponding specification file (*.spec.ts) wherein all tests are written as near-plain-english behavior stories. And, just like in TDD, I tend to write these behavior specs first, then develop the feature until it satisfies them.
- 12-Factor Methodology
	- A set of twelve high-level guidelines for developing Software-as-a-Service (SaaS). I've found that even small JAMstack apps like this website share many structural similarities with larger SaaS projects, thus I adhere to 12-Factor wherever its guidelines apply.
- Continuous Integration & Deployment (CI/CD)
	- Continuous Integration (CI) is the practice of merging changes back into the main branch as often as possible, and running automated tests to make sure those changes don't break anything. Continuous Deployment (CD) is an extension of CI that immediately put those changes into production with little-to-no user input. I practice both through the GitHub Actions CI server. I have a CI workflow for each test runner, a workflow for deploying the site frontend to GitHub Pages, and a workflow for deploying the site API to a DigitalOcean server.

Tooling
- VS Code
	- A fast, extensible code editor developed by Microsoft. It is the centerpiece of my frontend development environment.
- PyCharm
	- A powerful IDE built specifically for development in the Python ecosystem. I use it as my backend development environment.
- Docker
	- An app containerization engine that I use to make my backend portable and scalable.
- Nginx
	- A multi-function web server software that I use as a reverse proxy for my backend API.
- Astro
	- A Static Site Generator with integrations for many popular JS UI frameworks. I use it as a scaffold for small, targeted Vue components; this minimizes page size, load times, and improves SEO, while preserving the interactivity and dev experience afforded by Vue.