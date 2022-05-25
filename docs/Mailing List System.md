# What Do I Need?

# What  Happens?

- User sends me a message through the Contact Form
- Mailer sends User a confirmation in their inbox.
- User is tracked by the email address they gave.
- A thread id is stored alongside that email address so that the Mailer will know which thread to reply to.
- I am CC'd into the Thread

Email is sent
- TO the User's email
- TO me
- BCC everyone in the MailingList with the CONTACT_FORM_BCC role

What if the User sends another message?
- As long as the User enters the same email as before in the email field, the new message will be appended...
- No, screw that. To much to track. **One contact form entry, one thread.** Simple as.
