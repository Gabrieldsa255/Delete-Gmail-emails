# Delete-Gmail-emails (PyAutoGUI)

A small Python automation project to help you clean up a crowded Gmail inbox when you have **tons of emails** and it becomes tiring to delete them manually.

Sometimes Gmail doesn’t make it convenient to delete everything quickly (especially when you have a lot of messages), so this project automates the repetitive workflow:

1. Click **Select** (checkbox in the Gmail toolbar)
2. Click **Delete / Trash**
3. Wait a short delay (to avoid browser lag/glitches)
4. Repeat as many times as needed

> ⚠️ This project uses GUI automation (mouse clicks). It depends on your screen layout, browser zoom, and where Gmail is located on your monitor(s).  
> ✅ Always test with a small repeat count before using it on a large inbox.

---

## Repository Structure

```text
APAGAR EMAILS/
├─ delete_emails.py     # Main script: repeats Select -> Delete to remove many emails
├─ showxandy.py         # Helper: shows mouse X/Y coordinates in real-time
└─ showxandyent.py      # Helper: prints mouse X/Y once when you press ENTER
=======
# Delete-Gmail-emails
A tiny Python + PyAutoGUI bot to delete Gmail emails in bulk — perfect when your inbox is huge and you’re too lazy to click delete hundreds of times.

