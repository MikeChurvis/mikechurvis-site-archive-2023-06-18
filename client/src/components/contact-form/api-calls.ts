import type { FormConfig, FormData } from './types'

export { generateFormAPIMethods }


/**
 * A setup function for the methods that interact with the API.
 *
 * @param apiRootUrl The API host URL, plus any base directory from which the API is served. 
 * All fetch() calls target endpoints relative to this URL.
 */
function generateFormAPIMethods(apiRootUrl: string) {

  /**
   * Fetches configuration data from the API. 
   */
  async function getFormConfig(): Promise<FormConfig> {
    const response = await fetch(`${apiRootUrl}/contact/config`)

    if (!response.ok) {
      throw Error(`Server responded with ${response.status}: ${response.statusText}`)
    }

    const responseData = await response.json()
    const {
      nameMaxLength,
      organizationMaxLength,
      emailMaxLength,
      emailRegex,
      messageMinLength,
      messageMaxLength
    } = responseData
    
    const formConfig: FormConfig = {
      nameMaxLength,
      organizationMaxLength,
      emailMaxLength,
      emailRegex,
      messageMinLength,
      messageMaxLength
    }

    const undefinedConfigProps = Object.keys(formConfig).filter(property => formConfig[property] === undefined)

    if (undefinedConfigProps.length) {
      throw Error(`API sent invalid config to contact form. Undefined props: ${undefinedConfigProps.join()}`)
    }

    return formConfig
  }


  /** 
   * Sends the contact form data to the server and awaits the response.
   * 
   * If the response is 200 (OK), then the submission was successful and the promise resolves to true.
   * 
   * If the response is 422 (Unprocessable Entity), then the submission was invalid due to a validation error.
   * Each field's error label is populated with its validation error message. The promise resolves to false.
   * 
   * If any other error is received, this function will throw its own Error containing the server response status.
   * The promise is rejected.
   */
  async function postFormData(formData: FormData): Promise<boolean> {

    const formDataValues = {}

    for (const field in formData) {
      formDataValues[field] = formData[field].value
    }

    const response = await fetch(`${apiRootUrl}/contact/`, {
      method: 'POST',
      mode: 'cors',
      headers: { "Access-Control-Allow-Origin": apiRootUrl },
      credentials: "same-origin",
      body: JSON.stringify(formDataValues),
    })

    if (response.ok) {
      return true
    } else if (response.status === 422) {
      const responseData = await response.json()

      for (const fieldWithError in responseData) {
        formData[fieldWithError].error = responseData[fieldWithError][0]
      }

      return false
    }

    throw Error(`Server responded with ${response.status}: ${response.statusText}`)
  }


  return { getFormConfig, postFormData }
}
