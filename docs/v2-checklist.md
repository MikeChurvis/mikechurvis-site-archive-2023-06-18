# Migrate frontend to PNPM

- [x] remove package-lock.json
- [x] pnpm install
- [x] make sure the site launches in dev
- [x] Upgrade astro to 1.0

# Frontend: refactor ENV dependency out of Contact Form.

- [x] Decouple the form component from external variables.
- [x] Add injectable debug config
- [x] Refactor component hierarchy to use `<Suspense>` so that async components awaiting the config promise don't break the page.

# Flatten frontend project directory

- [x] Portfolio/frontend/portfolio -> Portfolio/client

# Build a frontend test suite

- [x] Install Cypress
- [x] Make an end-to-end test for the contact form feature (describe-specify syntax, intercept API calls)

# Flatten backend project directory

- [x] Portfolio/frontend/portfolio -> Portfolio/api
- [x] Make the django project a first-order member of the ./api folder
- [x] De-dockerize Nginx.conf.

# Migrate backend dev environment from a live container to a VirtualEnv

# Move shared config to backend

- [ ] Writeup the new API endpoints
- [ ] Create MailingList app
- [ ] Add config GET endpoint to ContactForm app
- [ ] Add caching to config endpoint

# Convert django webserver to ASGI

- [ ] Determine if this is actually necessary

# Build a backend test suite

- [ ] Install pytest and config it for django

# Build an end-to-end test suite for the front page

# Frontend: accessibility pass

- [ ] keyboard accessibility spectest
- [ ] keyboard accessibility implementation

# Contact form: turn placeholders into actual labels