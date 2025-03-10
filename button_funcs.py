

# Button functions

import tkinter as tk
from tkinter import messagebox
import pyperclip
from jinja2 import Template
from email_data import EMAIL_TEMPLATES, CUSTOM_NOTE

def generate_email(app):
    """Generate a formatted email based on form input and display it in the text box."""
    
    # Retrieve user input from UI
    name = app.name_entry.get()
    subscription = app.subscription_dropdown.get()
    billing_schedule = app.billing_dropdown.get()
    next_service = app.next_service_entry.get()
    rate = app.rate_entry.get()
    note_in = app.custom_note.get()
    amount = app.amount_entry.get()

    # Get the appropriate note content
    note_value = CUSTOM_NOTE.get(note_in, CUSTOM_NOTE["None"])
    note_template = Template(note_value)

    # Use amount_entry to autofill the custom note
    note = note_template.render(
        amount=amount
    )

    # Get the appropriate email template
    template_text = EMAIL_TEMPLATES.get(subscription, EMAIL_TEMPLATES["default"])
    template = Template(template_text)

    # Generate the email with user input values
    email_text = template.render(
        name=name,
        subscription=subscription,
        billing_schedule=billing_schedule,
        next_service=next_service,
        rate=rate,
        notes=note
    )

    # Update the Tkinter text display
    app.email_display.config(state=tk.NORMAL)  # Enable text box
    app.email_display.delete("1.0", tk.END)  # Clear previous content
    app.email_display.insert(tk.END, email_text)  # Insert new email
    # app.email_display.config(state=tk.DISABLED)  # Disable editing

def copy_email_to_clipboard(app):
    """Copy the generated email to clipboard or warning message."""
    email_text = app.email_display.get("1.0", tk.END).strip()
    if email_text:
        pyperclip.copy(email_text)
    else:
        messagebox.showwarning("No Email", "Generate an email first before copying.")

def clear_form(app):
    """Clears all input fields and resets selections."""
    app.name_entry.delete(0, tk.END)
    app.subscription_dropdown.set("")
    app.billing_dropdown.set("")
    app.rate_entry.delete(0, tk.END)
    app.next_service_entry.delete(0, tk.END)
    app.email_display.config(state=tk.NORMAL)
    app.email_display.delete("1.0", tk.END)
    app.email_display.config(state=tk.DISABLED)
    app.custom_note.set("")


def update_amount_field(email_generator):
    """Show or hide the 'Amount' input field based on the custom note selection."""
    if email_generator.custom_note.get().lower() == "none":
        email_generator.amount_label.grid_remove()
        email_generator.amount_entry.grid_remove()
    else:
        email_generator.amount_label.grid()
        email_generator.amount_entry.grid()