# Migrate frontend to PNPM

- [x] remove package-lock.json
- [x] pnpm install
- [x] make sure the site launches in dev
- [x] Upgrade astro to 1.0

# Frontend: refactor ENV dependency out of Contact Form.

- [x] Decouple the form component from external variables.
- [x] Add injectable debug config
- [x] Refactor component hierarchy to use `<Suspense>` so that async components awaiting the config promise don't break the page.

# Move shared config to backend

- [ ] Writeup the new API endpoints
- [ ] Create MailingList app
- [ ] Add config GET endpoint to ContactForm app
- [ ] Add caching to config endpoint

# Flatten frontend project directory

- [x] Portfolio/frontend/portfolio -> Portfolio/client

# Flatten backend project directory

# Migrate backend dev environment from a live container to a VirtualEnv

# Decontainerize Nginx

# Convert django webserver to ASGI

# Build a frontend test suite

# Build a backend test suite

# Build an end-to-end test suite

# Frontend: accessibility pass

- [ ] keyboard accessibility spectest
- [ ] keyboard accessibility implementation

# Contact form: turn placeholders into actual labels