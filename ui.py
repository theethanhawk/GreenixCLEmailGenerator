import tkinter as tk
from tkinter import ttk
from email_data import SUBSCRIPTIONS, BILLING_FREQUENCIES
from button_funcs import copy_email_to_clipboard, clear_form, generate_email

class EmailGenerator:
    """Class that models the full Email Generator UI"""
    def __init__(self, root):
        self.root = root
        self.root.title("Greenix Customer Loyalty Email Generator")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        self.root.configure(bg="#49A864")

        # User inputs
        # Frame to hold input boxes
        inputs_frame = ttk.Frame(root)
        inputs_frame.pack(pady=10)

        # Labels and input fields using grid layout
        ttk.Label(inputs_frame, text="Customer First Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = ttk.Entry(inputs_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(inputs_frame, text="Subscription:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.subscription_dropdown = ttk.Combobox(inputs_frame, values=SUBSCRIPTIONS)
        self.subscription_dropdown.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(inputs_frame, text="Next Service Date (MM/DD/YYYY):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.next_service_entry = ttk.Entry(inputs_frame)
        self.next_service_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(inputs_frame, text="Billing Frequency:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.billing_dropdown = ttk.Combobox(inputs_frame, values=BILLING_FREQUENCIES)
        self.billing_dropdown.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        ttk.Label(inputs_frame, text="Rate:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
        self.rate_entry = ttk.Entry(inputs_frame)
        self.rate_entry.grid(row=1, column=3, padx=5, pady=5, sticky="w")

        # Buttons
        # Create a frame to hold the buttons (inside the root window)
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10)  # Add some spacing above the buttons

        # Create the buttons inside the frame using grid layout
        generate_button = ttk.Button(button_frame, text="Generate Email", command=lambda: generate_email(self))
        generate_button.grid(row=0, column=0, padx=5)  # Left button

        copy_button = ttk.Button(button_frame, text="Copy Email", command=lambda: copy_email_to_clipboard(self))
        copy_button.grid(row=0, column=1, padx=5)  # Middle button

        clear_button = ttk.Button(button_frame, text="Clear Form", command=lambda: clear_form(self))
        clear_button.grid(row=0, column=2, padx=5)  # Right button

        inputs_frame.configure(style="Custom.TFrame")
        button_frame.configure(style="Custom.TFrame")

        style = ttk.Style()
        style.configure("Custom.TFrame", background="#49A864") 

        # Email Display
        self.email_display = tk.Text(
            root, 
            height=30, 
            width=70, 
            state=tk.DISABLED
        )
        self.email_display.pack(pady=(0, 40))

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = EmailGenerator(root)
    root.mainloop()
