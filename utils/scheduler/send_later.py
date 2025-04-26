#scheduler/send_emails_at_specific_time.py

import datetime
import logging
import time
import os

from utils.data_utils.generate_email_address import generate_email_address
from utils.email_utils.email_sender import send_email
from utils.email_utils.email_manager import load_email_settings, read_email_template, read_excel_data

logger = logging.getLogger(__name__)
MAX_RETRIES = 3

def schedule_emails():
    """
    Prompts user to schedule emails for a specific time.
    """
    specific_time = input("Enter the specific time to schedule the email (HH:MM): ")
    try:
        hour, minute = map(int, specific_time.split(':'))
        if 0 <= hour < 24 and 0 <= minute < 60:
            send_emails_at_specific_time(hour, minute)
        else:
            print("Invalid time. Please enter a valid time in HH:MM format.")
    except ValueError:
        print("Invalid time format. Please enter the time in HH:MM format.")

def send_emails_at_specific_time(hour, minute, batch_size=10):
    """
    Sends emails at a specific time.

    Args:
        hour (int): Hour to send emails.
        minute (int): Minute to send emails.
        batch_size (int): Number of emails to send in each batch.
    """
    sender_email, sender_password = load_email_settings()
    email_template = read_email_template()
    data = read_excel_data()

    now = datetime.datetime.now()
    scheduled_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if scheduled_time < now:
        scheduled_time += datetime.timedelta(days=1)

    delay = (scheduled_time - now).total_seconds()
    logger.info(f"Waiting until {scheduled_time.strftime('%H:%M')} to send emails.")
    time.sleep(delay)

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
                    else:
                        logger.warning(f"No valid email address for {first_name} {last_name} at {company_name}")
                        print(f"No valid email address for {first_name} {last_name} at {company_name}")
                    break  # Email sent successfully, exit retry loop

                except Exception as e:
                    logger.error(f"Error sending email: {e}")
                    retries += 1
                    logger.info(f"Retrying... ({retries}/{MAX_RETRIES})")
                    time.sleep(10)

            if retries == MAX_RETRIES:
                logger.error(f"Max retries reached. Unable to send email to {email}.")

