# Emailer

## Purpose

**What does it do?**
- It sends emails.

**How does it do it?**
- Gmail API
- Huey + Redis (asynchronous task queue)

**Why do I need it?**
- To notify myself and a few select others when someone uses my website contact form.
- To separate concerns.
- To future-proof the API.

## Structure

The ContactFormEntry model has a `notify_admin_status` and `notify_admin_status_detail` field.

Emailer has a `tasks` module with all of the functions it needs to run.

