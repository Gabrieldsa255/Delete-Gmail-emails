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
```
# How It Works

The main script (`delete_emails.py`) clicks two points on your screen repeatedly:

-   Select checkbox (top toolbar in Gmail)
    
-   Trash/Delete icon (top toolbar in Gmail)
    

It loops this action `REPEAT` times, so you can delete large amounts of emails faster.

----------

## Step 1 — Get Your Mouse Coordinates (X/Y)

Before running the deletion script, you must capture the correct coordinates for your screen.

### Option A: Live coordinates (real-time)

Run:

`python showxandy.py` 

Move your mouse over:

-   the Select checkbox
    
-   the Trash/Delete icon
    

Write down the X/Y values.

### Option B: Capture once (press ENTER)

Run:

`python showxandyent.py` 

Put the mouse over the target button and press ENTER in the terminal.  
It will print the X/Y once (this is usually more reliable).

----------

## Step 2 — Configure `delete_emails.py`

Open `delete_emails.py` and update these sections:

### 1) Set the coordinates

Find:

`SELECT_X, SELECT_Y = 124, 221  # Select checkbox (top toolbar) DELETE_X, DELETE_Y = 314, 216  # Trash/Delete icon (top toolbar)` 

Replace with your coordinates from `showxandy.py` or `showxandyent.py`.

### 2) Set how many times the script repeats

Find:

`REPEAT = 50` 

Change `50` to any number you want.

✅ This is where you control how many deletion cycles will run (Select → Delete).

Recommended:

-   Test first: `REPEAT = 3` or `REPEAT = 5`
    
-   Real cleanup: increase (`50`, `100`, `200`...)
    

### 3) Adjust delays if Gmail is slow

Find:

`WAIT_AFTER_SELECT = 1.00 WAIT_AFTER_DELETE = 1.05` 

If your browser/Gmail is slow, increase these values (e.g., `1.3–2.0`).

----------

## Step 3 — Run the Script

Open Gmail and keep the inbox/label visible

-   Keep the Gmail window in the same place (don’t move/resize)
    

Run:

`python delete_emails.py` 

During the run:

-   Don’t touch mouse/keyboard
    
-   Keep Gmail focused and visible
    

----------

## Safety / Emergency Stop

This project enables PyAutoGUI FAILSAFE:

✅ Move the mouse to the top-left corner of the screen to stop immediately.

You can also stop from the terminal with:

`Ctrl + C` 

----------

## Tips for Best Reliability

-   Keep browser zoom at 100%
    
-   Avoid resizing the browser window during execution
    

### Multi-monitor note

-   Coordinates are based on the full “virtual desktop”
    
-   Keep Gmail on the same monitor the whole time
    

### If your “Select” click doesn’t work

-   You might be clicking the small arrow next to the checkbox
    
-   Re-capture coordinates aiming at the center of the checkbox
