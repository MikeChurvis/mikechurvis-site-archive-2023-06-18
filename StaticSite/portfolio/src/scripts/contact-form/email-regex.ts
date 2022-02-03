/** 
 * LOCAL-PART DEFINITION
 * 
 * At least one "word" consisting of at least one alphanumeric/underscore/hyphen/plus character.
 * 
 * Periods may be used, but with the following restrictions: 
 * - can't be first
 * - can't be last
 * - can't be consecutive
 * 
 * Max length of local-part: 64 characters.
 * */

let word = "[a-zA-Z0-9_+-]+"
let localPart = String.raw`((${word}\.)*${word}){1,64}`

/**
 * DOMAIN NAME DEFINITION
 * 
 * At least one "label" consisting of at least one but no more than 63 alphanumeric characters, each ending in a single period. 
 * 
 * Hyphens may be used in labels, but with the following restrictions:
 * - can't be first
 * - can't be last
 * 
 * After all labels, a "top-level domain" consisting of at least one alphanumeric character, but cannot be entirely numeric.
 * 
 * Max length of the whole domain name: 255 characters.
 */

let alphanumWithHyphen = "([a-zA-Z0-9]+-)*[a-zA-Z0-9]+"

let label = String.raw`${alphanumWithHyphen}{1,63}\.`
let topLevelDomain = String.raw`((${alphanumWithHyphen})*[a-zA-Z](${alphanumWithHyphen})*){1,63}`

let domainName = String.raw`((${label})+(${topLevelDomain})){1,255}`

let emailAddress = String.raw`^(${localPart})@(${domainName})$`
let emailAddressRegExp = new RegExp(emailAddress)

export { emailAddressRegExp }