# IT Setup Guide — New Hire Day 1

Welcome. This walks you through your first day's IT setup.

## Hardware (delivered to you before start date)
- MacBook Pro 14" M3 (16GB / 512GB standard; 32GB available on request for ML/data roles)
- External 27" monitor
- Apple Magic Keyboard + Magic Mouse OR Logitech MX equivalents
- USB-C hub
- Webcam (Logitech C920)

If anything's missing or damaged: open a ticket at help.[redacted].com or message #it-support.

## First boot
1. Power on, complete macOS setup wizard. Use your work email (firstname.lastname@[redacted].com).
2. When prompted for an admin account, use the credentials in your welcome email.
3. The MDM (Jamf) profile installs automatically. Approve all prompts.

## Required installs (auto-pushed via Jamf, takes ~30 min)
- Slack
- Zoom
- 1Password (your vault is invited; check your email)
- Okta Verify
- Notion
- Linear
- AnyConnect VPN
- Google Chrome (with managed profile)

## Account setup (do in this order)
1. **Okta:** complete MFA setup with Okta Verify on your phone
2. **Email/calendar:** sign in to Google Workspace via Okta SSO
3. **Slack:** sign in via SSO. Join #general, #announcements, your team channel, #social
4. **1Password:** accept vault invite, transfer over from personal manager if any
5. **Notion:** SSO sign-in, browse the "New Hire" home page
6. **Linear:** SSO sign-in, your team's project will appear

## Engineering-specific
If you're in engineering, you'll get additional accesses:
- GitHub: invitation will land within 24h of start date
- AWS: provisioned via Okta SSO, role-based access
- Internal dev environment: see the engineering onboarding doc in Notion
- VPN: required for staging/prod access

## Common issues
- **Okta MFA stuck:** restart Okta Verify, request reset in #it-support
- **VPN won't connect:** check that you're on Okta-protected SSID at office; for remote, try the AnyConnect "lite" profile
- **Can't find a tool:** check the Software Catalog in Notion

## Phone / Mobile
- Slack on phone: install, sign in via SSO
- 1Password on phone: install, complete the QR-code setup with your laptop
- Okta Verify on phone: required (it's your MFA)

## What if I want a different setup?
- Linux on the laptop: not supported, sorry. We standardize on macOS for MDM/security.
- Mechanical keyboard / different mouse: bring your own, BYOD-friendly
- Standing desk / better chair: claim against your WFH setup allowance

## Help
- Real-time: #it-support on Slack
- Tickets: help.[redacted].com
- In-office: IT desk on the 4th floor, weekday 10-7
