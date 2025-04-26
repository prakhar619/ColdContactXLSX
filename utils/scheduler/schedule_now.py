# scheduler/schedule_now.py

import logging
import time
import os 

from utils.data_utils.generate_email_address import generate_email_address
from utils.email_utils.email_sender import send_email
from utils.email_utils.email_manager import load_email_settings, read_email_template, read_excel_data

logger = logging.getLogger(__name__)
MAX_RETRIES = 3

def send_emails_now(batch_size=10):
    """
    Sends emails immediately.

    Args:
        batch_size (int): Number of emails to send in each batch.
    """
    sender_email, sender_password = load_email_settings()
    email_template = read_email_template()
    data = read_excel_data()

    # Split the data into batches
    for i in range(0, len(data), batch_size):
        batch = data[i:i + batch_size]

        for row in batch:
            retries = 0
            while retries < MAX_RETRIES:
                try:
                    first_name, last_name, email, company_name, designation = row
                    recipient_emails = generate_email_address(first_name, last_name, email, company_name)
                    subject_part = os.getenv("SUBJECT")
                    position = os.getenv("POSITION")
                    your_name = os.getenv("YOUR_NAME")
                    link = os.getenv("LINK")
                    
                    # Build email body
                    def build_message(recipient_email):
                        return email_template.format(
                            FIRST_NAME=first_name,
                            LAST_NAME=last_name,
                            EMAIL=recipient_email,
                            COMPANY_NAME=company_name,
                            POSITION=position,
                            YOUR_NAME=your_name,
                            LINK=link,
                            DESIGNATION=designation if designation else "esteemed employee"
                        )
                    
                    # Handle single or multiple emails
                    if isinstance(recipient_emails, (list, tuple)):
                        for recipient_email in recipient_emails:
                            subject = f"{subject_part} at {company_name}"
                            message = build_message(recipient_email)
                            send_email(sender_email, sender_password, recipient_email, subject, message, company_name)
                            logger.info(f"Email sent successfully to {recipient_email}")
                    elif recipient_emails:
                        subject = f"{subject_part} at {company_name}"
                        message = build_message(recipient_emails)
                        send_email(sender_email, sender_password, recipient_emails, subject, message, company_name)
                        logger.info(f"Email sent successfully to {recipient_emails}")
                        print(f"Email sent successfully to {recipient_emails}")
                    break  # Email sent successfully, exit retry loop

                except Exception as e:
                    logger.error(f"Error sending email to {email}: {e}")
                    retries += 1
                    logger.info(f"Retrying... ({retries}/{MAX_RETRIES})")
                    time.sleep(10)

            if retries == MAX_RETRIES:
                logger.error(f"Max retries reached. Failed to send email to {email}.")
