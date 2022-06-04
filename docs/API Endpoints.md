# Contact Form Flow

On page load:
1. GET contact form parameters from API.
2. If parameter GET fails, show.
3. On blur, validate individual field.
4. On submit, await Client Validation.
	1. On Client Validation fail, show form errors. Go to Step 2.
	2. On Client Validation success, POST form data to API. 
5. Await API Validation.
	1. On API Validation fail, show form errors. Go to Step 2.
	2. On API Validation success, show successful submit.

# API Endpoints

`GET /contact/config`
`POST /contact`
