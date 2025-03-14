"""This file is for storing data used in email generation."""

# List of subscriptions types
SUBSCRIPTIONS = [
    "Pest Control", 
    "Rodent Baiting",
    "Rodent Baiting 60 Day", 
    "Mosquito Reduction",
    "Tick, Flea, Mosquito",
    "GG Basic",
    "GG Select PC/RB",
    "GG Select PC/TFMx4",
    "GG Select PC/TFMx7",
    "GG Essential PC/RB/TFMx4",
    "GG Premier PC/RB/TFMx7",
    "Cancellation"
    ]

# Billing frequency types
BILLING_FREQUENCIES = [
    "monthly",
    "per-service",
    "Annually"
]

NOTE_INPUTS = [
    "None",
    "Refund",
    "Cancel Refund",
    "Coupon"
]

CUSTOM_NOTE = {
    "None":"""\
""",
    "Refund":"""\
This is a confirmation we are processing the refund for the amount ${{ amount }}. Refunds will take 7-10 business days.\n
""",
    "Cancel Refund":"""\
This is also a confirmation that we are processing the refund for the amount ${{ amount }}. Refunds will take 7-10 business days.\n
""",
    "Coupon":"""\
This is also a confirmation that a onetime coupon has been added to your account for the amount of ${{ amount }}.\n
"""
}


EMAIL_TEMPLATES = {
# Pest Control
    "Pest Control": """
Hello {{ name.title() }}!

Thank you for your continued business! \
We are excited for your next {{ subscription }} service scheduled for {{ next_service }} \
at the {{ billing_schedule }} rate of ${{ rate }}. {{ subscription }} services will \
continue every 90 days. 
{{ notes }}Please remember to call us in between regular services with any questions, or to \
schedule any free re-services that may be needed. We appreciate you, and are excited to \
continue providing you with a pest-free home!

Team Greenix
844-233-7378
""",

# Rodent Baiting
    "Rodent Baiting": """
Hello {{ name.title() }}!

Thank you for your continued business! \
We are excited for your next {{ subscription }} service scheduled for {{ next_service }} \
at the {{ billing_schedule }} rate of ${{ rate }}. {{ subscription }} services will \
continue every 90 days. 
{{ notes }}Please remember to call us in between regular services with any questions, or to \
schedule any free re-services that may be needed. We appreciate you, and are excited to \
continue providing you with a pest-free home!

Team Greenix
844-233-7378
""",

# Rodent Baiting 60 Day
    "Rodent Baiting 60 Day": """
Hello {{ name.title() }}!

Thank you for your continued business! \
We are excited for your next Rodent Baiting service scheduled for {{ next_service }} \
at the {{ billing_schedule }} rate of ${{ rate }}. Rodent Baiting services will \
continue every 60 days. 
{{ notes }}Please remember to call us in between regular services with any questions, or to \
schedule any free re-services that may be needed. We appreciate you, and are excited to \
continue providing you with a pest-free home!

Team Greenix
844-233-7378
""",

# Mosquito Reduction
    "Mosquito Reduction": """
Hello {{ name.title() }}!

Thank you for your continued business! \
We are excited for your next {{ subscription }} service scheduled for {{ next_service }} \
at the {{ billing_schedule }} rate of ${{ rate }}. {{ subscription }} services will \
continue every 30 days between April and October. 
{{ notes }}Please remember to call us in between regular services with any questions, or to \
schedule any free re-services that may be needed. We appreciate you, and are excited to \
continue providing you with a pest-free home!

Team Greenix
844-233-7378
""",

# Tick, Flea, Mosquito
    "Tick, Flea, Mosquito": """
Hello {{ name.title() }}!

Thank you for your continued business! \
We are excited for your next {{ subscription }} service scheduled for {{ next_service }} \
at the {{ billing_schedule }} rate of ${{ rate }}. {{ subscription }} services will \
continue every 30 days between April and October. 
{{ notes }}Please remember to call us in between regular services with any questions, or to \
schedule any free re-services that may be needed. We appreciate you, and are excited to \
continue providing you with a pest-free home!

Team Greenix
844-233-7378
""",

# GG Basic
    "GG Basic": """
Hello {{ name.title() }}!

Thank you for your continued business! \
We are excited for your next {{ subscription }} service scheduled for {{ next_service }} \
at the {{ billing_schedule }} rate of ${{ rate }}. {{ subscription }} services will \
continue every 90 days. 
{{ notes }}Please remember to call us in between regular services with any questions, or to \
schedule any free re-services that may be needed. We appreciate you, and are excited to \
continue providing you with a pest-free home!

Team Greenix
844-233-7378
""",

# GG Select PC/RB
    "GG Select PC/RB": """
Hello {{ name.title() }}!

Thank you for your continued business with our GreenGuard Select Plan, \
including Pest Control and Rodent Baiting services! We are excited for your \
next GreenGuard Select service scheduled for {{ next_service }} at the \
{{ billing_schedule }} rate of ${{ rate }}. Your GreenGuard Select Pest \
Control and Rodent Baiting services will continue afterwards every 90 days. 
{{ notes }}Please remember to call us in between regular services with any questions, or to \
schedule any free re-services that may be needed. We appreciate you, and are excited to \
continue providing you with a pest-free home!

Team Greenix
844-233-7378
""",

# GG Select PC/TFMx4
    "GG Select PC/TFMx4": """
Hello {{ name.title() }}!

Thank you for your continued business with our GreenGuard Select Plan, \
including Pest Control and Tick, Flea, Mosquito services! We are excited \
for your next GreenGuard Select Pest Control service scheduled for \
{{ next_service }} at the {{ billing_schedule }} rate of ${{ rate }}. The \
GreenGuard Select Pest Control services will continue every 90 days, with \
Tick, Flea, Mosquito services every 45 days between April and October. 
{{ notes }}Please remember to call us in between regular services with any questions, or to \
schedule any free re-services that may be needed. We appreciate you, and are excited to \
continue providing you with a pest-free home!

Team Greenix
844-233-7378
""",

# GG Select PC/TFMx7
    "GG Select PC/TFMx7": """
Hello {{ name.title() }}!

Thank you for your continued business with our GreenGuard Select Plan, \
including Pest Control and Tick, Flea, Mosquito services! We are excited \
for your next GreenGuard Select Pest Control service scheduled for \
{{ next_service }} at the {{ billing_schedule }} rate of ${{ rate }}. The \
GreenGuard Select Pest Control services will continue every 90 days, with \
Tick, Flea, Mosquito services every 30 days between April and October. 
{{ notes }}Please remember to call us in between regular services with any questions, or to \
schedule any free re-services that may be needed. We appreciate you, and are excited to \
continue providing you with a pest-free home!

Team Greenix
844-233-7378
""",

# GG Essential PC/RB/TFMx4
    "GG Essential PC/RB/TFMx4": """
Hello {{ name.title() }}!

Thank you for your continued business with our GreenGuard Essential Plan, \
including Pest Control, Rodent Baiting, and Tick, Flea, Mosquito services! \
We are excited for your next GreenGuard Essential service scheduled for \
{{ next_service }} at the {{ billing_schedule }} rate of ${{ rate }}. \
GreenGuard Essential Pest Control and Rodent Baiting services will continue \
every 90 days, with Tick, Flea, Mosquito services every 45 days between \
April and October. 
{{ notes }}Please remember to call us in between regular services with any questions, or to \
schedule any free re-services that may be needed. We appreciate you, and are excited to \
continue providing you with a pest-free home!

Team Greenix
844-233-7378
""",

# GG Premier PC/RB/TFMx7
    "GG Premier PC/RB/TFMx7": """
Hello {{ name.title() }}!

Thank you for your continued business with our GreenGuard Premier Plan, \
including Pest Control, Rodent Baiting, and Tick, Flea, Mosquito services! \
We are excited for your next GreenGuard Premier service scheduled for \
{{ next_service }} at the {{ billing_schedule }} rate of ${{ rate }}. \
GreenGuard Premier Pest Control and Rodent Baiting services will continue \
every 90 days, with Tick, Flea, Mosquito services every 30 days between \
April and October. 
{{ notes }}Please remember to call us in between regular services with any questions, or to \
schedule any free re-services that may be needed. We appreciate you, and are excited to \
continue providing you with a pest-free home!

Team Greenix
844-233-7378
""",

# Cancellation
    "Cancellation": """
Hello {{name.title()}},

This is confirmation that your Greenix services have been cancelled. {{ notes }}\
We are sorry to see you go, but remember you can always call back and get your services reinstated. \
Thank you for using Greenix for your pest control needs and please consider us for the future!

Team Greenix

844-233-7378
""",

# Default template for other service types
    "default": """
Select a template!
"""
}