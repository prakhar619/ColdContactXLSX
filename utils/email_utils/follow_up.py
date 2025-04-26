# email_utils/follow_up.py

"""
Module for sending follow-up emails to recipients.

This module includes functionality to load email settings, read email templates,
read recipient data from an Excel file, and send follow-up emails.

"""

import os
import logging

from utils.email_utils.email_sender import send_email
from utils.email_utils.email_manager import load_email_settings, read_email_template, read_excel_data, read_follow_up_template
from utils.data_utils.generate_email_address import generate_email_address  # Import the generate_email_address function

logger = logging.getLogger(__name__)

def send_follow_up_email():
    """
    Sends follow-up emails to recipients.

    This function loads email settings, email templates, and recipient data,
    and then iterates through each recipient to send a follow-up email.

    """
    sender_email, sender_password = load_email_settings()
    email_template = read_email_template()
    follow_up_template = read_follow_up_template()
    data = read_excel_data()

    for row in data:
        first_name, last_name, email, company_name, designation = row

        generated_emails = generate_email_address(first_name, last_name, email, company_name)

        # Iterate through generated email addresses and send follow-up emails
        subject_part = os.getenv("SUBJECT")
        position = os.getenv("POSITION")
        your_name = os.getenv("YOUR_NAME")
        link = os.getenv("LINK")
        for email in generated_emails:
            if email:
                subject = f"[Follow Up]: {subject_part} at {company_name}"
                message = follow_up_template.format(
                            FIRST_NAME=first_name,
                            LAST_NAME=last_name,
                            COMPANY_NAME=company_name,
                            POSITION=position,
                            YOUR_NAME=your_name,
                            LINK=link,
                            DESIGNATION=designation if designation else "esteemed employee")
                # Add additional string after "original email"
                original_email_info = f"\n\n--------------- ORIGINAL EMAIL ---------------\n\n" \
                                      f"\nFrom: {sender_email}\nTo: {email}\nSubject: {subject_part} at {company_name}\n\n"
                message += original_email_info
                message += email_template.format(
                            FIRST_NAME=first_name,
                            LAST_NAME=last_name,
                            COMPANY_NAME=company_name,
                            POSITION=position,
                            YOUR_NAME=your_name,
                            LINK=link,
                            DESIGNATION=designation if designation else "esteemed employee")
                send_email(sender_email, sender_password, email, subject, message, company_name)
            else:
                logger.warning("Skipping follow-up email: Unable to generate recipient email address.")
