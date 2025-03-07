import tkinter as tk
from tkinter import ttk
from email_data import SUBSCRIPTIONS, BILLING_FREQUENCIES, NOTE_INPUTS
from button_funcs import copy_email_to_clipboard, generate_email


class EmailUI:
    """Handles UI layout for the Email Generator"""
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Greenix Customer Loyalty Email Generator")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        self.root.configure(bg="#000000")

        """Primary Section"""
        self.primary_frame = ttk.Frame(root)
        self.primary_frame.pack(pady=10)

        ttk.Label(self.primary_frame, text="Customer First Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = ttk.Entry(self.primary_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(self.primary_frame, text="Account ID:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.id_entry = ttk.Entry(self.primary_frame)
        self.id_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(self.primary_frame, text="Subscription Amount:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.subscription_amount_entry = ttk.Entry(self.primary_frame)
        self.subscription_amount_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.create_forms_button = ttk.Button(self.primary_frame, text="Create Forms", command=self.create_subscription_forms)
        self.create_forms_button.grid(row=3, column=0, columnspan=2, pady=10)

        """Dynamic Forms Section (Initially Hidden)"""
        self.forms_frame = ttk.Frame(root)
        self.forms_frame.pack(pady=10, padx=10, fill="x")

        self.forms = []  # Store created forms

        """Buttons"""
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10)

        self.generate_button = ttk.Button(button_frame, text="Generate Email", command=self.controller.generate_email, state=tk.DISABLED)
        self.generate_button.grid(row=0, column=0, padx=5)

        self.copy_button = ttk.Button(button_frame, text="Copy Email", command=self.controller.copy_email, state=tk.DISABLED)
        self.copy_button.grid(row=0, column=1, padx=5)

        self.clear_button = ttk.Button(button_frame, text="Return to Primary Section", command=self.clear_forms, state=tk.DISABLED)
        self.clear_button.grid(row=0, column=2, padx=5)

        """Email Display"""
        self.email_display = tk.Text(root, height=30, width=70, state=tk.DISABLED)
        self.email_display.pack(pady=(0, 40))

    def create_subscription_forms(self):
        """Creates subscription forms based on the number entered in Subscription Amount."""
        try:
            num_forms = int(self.subscription_amount_entry.get())
            if num_forms <= 0:
                raise ValueError
        except ValueError:
            return  # Do nothing if the input is invalid

        # Clear existing forms
        for form in self.forms:
            form["frame"].destroy()
        self.forms.clear()

        # Create new forms
        for i in range(num_forms):
            self.forms.append(self.create_form(self.forms_frame))

        # Show the buttons now that forms exist
        self.generate_button.config(state=tk.NORMAL)
        self.copy_button.config(state=tk.NORMAL)
        self.clear_button.config(state=tk.NORMAL)

    def create_form(self, parent):
        """Creates a single subscription form and returns it as a dictionary."""
        frame = ttk.Frame(parent)
        frame.pack(pady=10, padx=10, fill="x")

        form = {
            "frame": frame,
            "subscription": self.add_label_combobox(frame, "Subscription:", 0, 0, SUBSCRIPTIONS),
            "next_service": self.add_label_entry(frame, "Next Service (MM/DD/YYYY):", 1, 0),
            "billing": self.add_label_combobox(frame, "Billing Frequency:", 2, 0, BILLING_FREQUENCIES),
            "rate": self.add_label_entry(frame, "Rate:", 3, 0),
            "note": self.add_label_combobox(frame, "Custom Note:", 4, 0, NOTE_INPUTS),
        }

        return form

    def clear_forms(self):
        """Clears all subscription forms and returns to the primary section."""
        for form in self.forms:
            form["frame"].destroy()
        self.forms.clear()
        self.generate_button.config(state=tk.DISABLED)
        self.copy_button.config(state=tk.DISABLED)
        self.clear_button.config(state=tk.DISABLED)


class EmailController:
    """Handles logic and events for the Email Generator"""
    def __init__(self, root):
        self.ui = EmailUI(root, self)

    def generate_email(self):
        generate_email(self.ui)

    def copy_email(self):
        copy_email_to_clipboard(self.ui)

    def clear_form(self):
        self.ui.clear_forms()


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = EmailController(root)
    root.mainloop()





# import tkinter as tk
# from tkinter import ttk
# from email_data import SUBSCRIPTIONS, BILLING_FREQUENCIES, NOTE_INPUTS
# from button_funcs import copy_email_to_clipboard, clear_form, generate_email, update_amount_field

# """Add to Email/Account inputs UI"""
#         # [x] - Name
#         # [x] - Account ID
#         # [x] - Subscription
#         # [x] - Saved bool
#         # [x] - Renew bool
#         # [x] - ROR bool
#         # [x] - Cancel bool
#         # [x] - Noted bool
#         # [x] - Emailed bool
#         # [ ] - Give away 6%, 8%, 10%, more
#         # [x] - Follow up bool
#         # [ ] - If Follow up add notes input
#         # [ ] - Option for additional subscription form

# class EmailUI:
#     """Handles UI layout for the Email Generator"""
#     def __init__(self, root, controller):
#         self.root = root
#         self.controller = controller
#         self.root.title("Greenix Customer Loyalty Email Generator")
#         self.root.geometry("800x600")
#         self.root.resizable(True, True)
#         self.root.configure(bg="#000000")

#         inputs_frame = ttk.Frame(root)
#         inputs_frame.pack(pady=10)

#         ttk.Label(inputs_frame, text="Customer First Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
#         self.name_entry = ttk.Entry(inputs_frame)
#         self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

#         ttk.Label(inputs_frame, text="Account ID:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
#         self.id_entry = ttk.Entry(inputs_frame)
#         self.id_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

#         ttk.Label(inputs_frame, text="Subscription:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
#         self.subscription_dropdown = ttk.Combobox(inputs_frame, values=SUBSCRIPTIONS)
#         self.subscription_dropdown.grid(row=2, column=1, padx=5, pady=5, sticky="w")

#         ttk.Label(inputs_frame, text="Next Service(MM/DD/YYYY):").grid(row=3, column=0, padx=5, pady=5, sticky="e")
#         self.next_service_entry = ttk.Entry(inputs_frame)
#         self.next_service_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

#         ttk.Label(inputs_frame, text="Billing Frequency:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
#         self.billing_dropdown = ttk.Combobox(inputs_frame, values=BILLING_FREQUENCIES)
#         self.billing_dropdown.grid(row=0, column=3, padx=5, pady=5, sticky="w")

#         ttk.Label(inputs_frame, text="Rate:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
#         self.rate_entry = ttk.Entry(inputs_frame)
#         self.rate_entry.grid(row=1, column=3, padx=5, pady=5, sticky="w")

#         # Giveaway Discount Dropdown
#         ttk.Label(inputs_frame, text="Giveaway Discount:").grid(row=7, column=0, padx=5, pady=5, sticky="e")
#         self.giveaway_dropdown = ttk.Combobox(inputs_frame, values=["0-6%", "6-8%", "8-10%", "10+"])
#         self.giveaway_dropdown.grid(row=7, column=1, padx=5, pady=5, sticky="w")

#         ttk.Label(inputs_frame, text="Custom Note:").grid(row=2, column=2, padx=5, pady=5, sticky="e")
#         self.custom_note = ttk.Combobox(inputs_frame, values=NOTE_INPUTS)
#         self.custom_note.grid(row=2, column=3, padx=5, pady=5, sticky="w")

#         # [ ] - Give away 6%, 8%, 10%, more
#         # [x] - Follow up bool
#         # [ ] - If Follow up add notes input
#         # [ ] - Option for additional subscription form
        
#         # Follow-up
#         self.followup_bool = tk.BooleanVar(value=False)
#         self.followup_checkbox = ttk.Checkbutton(inputs_frame, text="Follow Up", variable=self.followup_bool)
#         self.followup_checkbox.grid(row=6, column=1, padx=5, pady=5, sticky="w")

#         # Amount Label & Entry (Initially Hidden)
#         self.amount_label = ttk.Label(inputs_frame, text="Amount:")
#         self.amount_entry = ttk.Entry(inputs_frame)
#         self.amount_label.grid(row=3, column=2, padx=5, pady=5, sticky="e")
#         self.amount_entry.grid(row=3, column=3, padx=5, pady=5, sticky="w")
#         self.amount_label.grid_remove()
#         self.amount_entry.grid_remove()

#         # Bind event to update_amount_field
#         self.custom_note.bind("<<ComboboxSelected>>", lambda *_: update_amount_field(self))

#         """Buttons"""
#         button_frame = ttk.Frame(root)
#         button_frame.pack(pady=10)

#         self.generate_button = ttk.Button(button_frame, text="Generate Email", command=self.controller.generate_email)
#         self.generate_button.grid(row=0, column=0, padx=5)

#         self.copy_button = ttk.Button(button_frame, text="Copy Email", command=self.controller.copy_email)
#         self.copy_button.grid(row=0, column=1, padx=5)

#         self.clear_button = ttk.Button(button_frame, text="Clear Form", command=self.controller.clear_form)
#         self.clear_button.grid(row=0, column=2, padx=5)

#         """Email Display"""
#         self.email_display = tk.Text(root, height=30, width=70, state=tk.DISABLED)
#         self.email_display.pack(pady=(0, 40))

# class EmailController:
#     """Handles logic and events for the Email Generator"""
#     def __init__(self, root):
#         self.ui = EmailUI(root, self)

#     def generate_email(self):
#         generate_email(self.ui)

#     def copy_email(self):
#         copy_email_to_clipboard(self.ui)

#     def clear_form(self):
#         clear_form(self.ui)
    
#     print("Running controller")


# # Run the app
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = EmailController(root)
#     root.mainloop()
