

import tkinter as tk
from tkinter import ttk
from email_data import SUBSCRIPTIONS, BILLING_FREQUENCIES, NOTE_INPUTS
from button_funcs import copy_email_to_clipboard, clear_form, generate_email, update_amount_field


class EmailUI:
    """Handles UI layout for the Email Generator"""
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Greenix Customer Loyalty Email Generator")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        self.root.configure(bg="#000000")

        inputs_frame = ttk.Frame(root)
        inputs_frame.pack(pady=10)

        ttk.Label(inputs_frame, text="Customer First Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = ttk.Entry(inputs_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(inputs_frame, text="Account ID:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.id_entry = ttk.Entry(inputs_frame)
        self.id_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(inputs_frame, text="Subscription:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.subscription_dropdown = ttk.Combobox(inputs_frame, values=SUBSCRIPTIONS)
        self.subscription_dropdown.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(inputs_frame, text="Next Service(MM/DD/YYYY):").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.next_service_entry = ttk.Entry(inputs_frame)
        self.next_service_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(inputs_frame, text="Billing Frequency:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.billing_dropdown = ttk.Combobox(inputs_frame, values=BILLING_FREQUENCIES)
        self.billing_dropdown.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        ttk.Label(inputs_frame, text="Rate:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
        self.rate_entry = ttk.Entry(inputs_frame)
        self.rate_entry.grid(row=1, column=3, padx=5, pady=5, sticky="w")

        # Giveaway Discount Dropdown
        ttk.Label(inputs_frame, text="Giveaway Discount:").grid(row=7, column=0, padx=5, pady=5, sticky="e")
        self.giveaway_dropdown = ttk.Combobox(inputs_frame, values=["0-6%", "6-8%", "8-10%", "10+"])
        self.giveaway_dropdown.grid(row=7, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(inputs_frame, text="Custom Note:").grid(row=2, column=2, padx=5, pady=5, sticky="e")
        self.custom_note = ttk.Combobox(inputs_frame, values=NOTE_INPUTS)
        self.custom_note.grid(row=2, column=3, padx=5, pady=5, sticky="w")
        
        # Follow-up
        self.followup_bool = tk.BooleanVar(value=False)
        self.followup_checkbox = ttk.Checkbutton(inputs_frame, text="Follow Up", variable=self.followup_bool)
        self.followup_checkbox.grid(row=6, column=1, padx=5, pady=5, sticky="w")

        # Amount Label & Entry (Initially Hidden)
        self.amount_label = ttk.Label(inputs_frame, text="Amount:")
        self.amount_entry = ttk.Entry(inputs_frame)
        self.amount_label.grid(row=3, column=2, padx=5, pady=5, sticky="e")
        self.amount_entry.grid(row=3, column=3, padx=5, pady=5, sticky="w")
        self.amount_label.grid_remove()
        self.amount_entry.grid_remove()

        # Bind event to update_amount_field
        self.custom_note.bind("<<ComboboxSelected>>", lambda *_: update_amount_field(self))

        """Buttons"""
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10)

        self.generate_button = ttk.Button(button_frame, text="Generate Email", command=self.controller.generate_email)
        self.generate_button.grid(row=0, column=0, padx=5)

        self.copy_button = ttk.Button(button_frame, text="Copy Email", command=self.controller.copy_email)
        self.copy_button.grid(row=0, column=1, padx=5)

        self.clear_button = ttk.Button(button_frame, text="Clear Form", command=self.controller.clear_form)
        self.clear_button.grid(row=0, column=2, padx=5)

        """Email Display"""
        self.email_display = tk.Text(root, height=30, width=70, state=tk.DISABLED)
        self.email_display.pack(pady=(0, 40))

class EmailController:
    """Handles logic and events for the Email Generator"""
    def __init__(self, root):
        self.ui = EmailUI(root, self)

    def generate_email(self):
        generate_email(self.ui)

    def copy_email(self):
        copy_email_to_clipboard(self.ui)

    def clear_form(self):
        clear_form(self.ui)
    
    print("Running controller")


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = EmailController(root)
    root.mainloop()