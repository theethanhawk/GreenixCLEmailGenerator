import tkinter as tk
from tkinter import messagebox
import pyperclip
from jinja2 import Template
from email_data import EMAIL_TEMPLATES, CUSTOM_NOTE


def generate_email(app):
    """Generate emails based on all active subscription forms."""
    all_emails = []

    name = app.name_entry.get()
    account_id = app.id_entry.get()

    for form in app.forms:
        subscription = form["subscription"].get()
        billing_schedule = form["billing"].get()
        next_service = form["next_service"].get()
        rate = form["rate"].get()
        note_in = form["note"].get()

        # Get the appropriate email template
        template_text = EMAIL_TEMPLATES.get(subscription, EMAIL_TEMPLATES["default"])
        template = Template(template_text)

        email_text = template.render(
            name=name,
            subscription=subscription,
            billing_schedule=billing_schedule,
            next_service=next_service,
            rate=rate,
            notes=note_in
        )

        all_emails.append(email_text)

    # Combine all emails into one text
    final_email_output = "\n\n---\n\n".join(all_emails)

    app.email_display.config(state=tk.NORMAL)
    app.email_display.delete("1.0", tk.END)
    app.email_display.insert(tk.END, final_email_output)
    app.email_display.config(state=tk.DISABLED)

def clear_form(app):
    """Clears all fields and resets UI."""
    app.name_entry.delete(0, tk.END)
    app.id_entry.delete(0, tk.END)
    app.subscription_amount_entry.delete(0, tk.END)

    # Clear all dynamically created forms
    for form in app.forms:
        form["frame"].destroy()
    app.forms.clear()

    # Reset buttons
    app.generate_button.config(state=tk.DISABLED)
    app.copy_button.config(state=tk.DISABLED)
    app.clear_button.config(state=tk.DISABLED)

    # Clear email display
    app.email_display.config(state=tk.NORMAL)
    app.email_display.delete("1.0", tk.END)
    app.email_display.config(state=tk.DISABLED)



def copy_email_to_clipboard(app):
    """Copy the generated email to clipboard or show a warning if empty."""
    email_text = app.email_display.get("1.0", tk.END).strip()
    if email_text:
        pyperclip.copy(email_text)
    else:
        messagebox.showwarning("No Email", "Generate an email first before copying.")

# # Button functions

# import tkinter as tk
# from tkinter import messagebox
# import pyperclip
# from jinja2 import Template
# from email_data import EMAIL_TEMPLATES, CUSTOM_NOTE

# def generate_email(app):
#     """Generate a formatted email based on form input and display it in the text box."""
    
#     # Retrieve user input from UI
#     name = app.name_entry.get()
#     subscription = app.subscription_dropdown.get()
#     billing_schedule = app.billing_dropdown.get()
#     next_service = app.next_service_entry.get()
#     rate = app.rate_entry.get()
#     note_in = app.custom_note.get()
#     amount = app.amount_entry.get()

#     # Get the appropriate note content
#     note_value = CUSTOM_NOTE.get(note_in, CUSTOM_NOTE["None"])
#     note_template = Template(note_value)

#     # Use amount_entry to autofill the custom note
#     note = note_template.render(
#         amount=amount
#     )

#     # Get the appropriate email template
#     template_text = EMAIL_TEMPLATES.get(subscription, EMAIL_TEMPLATES["default"])
#     template = Template(template_text)

#     # Generate the email with user input values
#     email_text = template.render(
#         name=name,
#         subscription=subscription,
#         billing_schedule=billing_schedule,
#         next_service=next_service,
#         rate=rate,
#         notes=note
#     )

#     # Update the Tkinter text display
#     app.email_display.config(state=tk.NORMAL)  # Enable text box
#     app.email_display.delete("1.0", tk.END)  # Clear previous content
#     app.email_display.insert(tk.END, email_text)  # Insert new email
#     # app.email_display.config(state=tk.DISABLED)  # Disable editing

# def copy_email_to_clipboard(app):
#     """Copy the generated email to clipboard or warning message."""
#     email_text = app.email_display.get("1.0", tk.END).strip()
#     if email_text:
#         pyperclip.copy(email_text)
#     else:
#         messagebox.showwarning("No Email", "Generate an email first before copying.")

# def clear_form(app):
#     """Clears all input fields and resets selections."""
#     app.name_entry.delete(0, tk.END)
#     app.subscription_dropdown.set("")
#     app.billing_dropdown.set("")
#     app.rate_entry.delete(0, tk.END)
#     app.next_service_entry.delete(0, tk.END)
#     app.email_display.config(state=tk.NORMAL)
#     app.email_display.delete("1.0", tk.END)
#     app.email_display.config(state=tk.DISABLED)
#     app.custom_note.set("")


# def update_amount_field(email_generator):
#     """Show or hide the 'Amount' input field based on the custom note selection."""
#     if email_generator.custom_note.get().lower() == "none":
#         email_generator.amount_label.grid_remove()
#         email_generator.amount_entry.grid_remove()
#     else:
#         email_generator.amount_label.grid()
#         email_generator.amount_entry.grid()
