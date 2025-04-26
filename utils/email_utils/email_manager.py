# scheduler/email_scheduler.py

"""
Module for managing email-related operations such as loading email settings, reading email templates,
and reading data from Excel files.
"""

import logging
import os

from utils.data_utils.excel_reader import read_data_from_excel
from utils.data_utils.generate_email_address import generate_email_address

logger = logging.getLogger(__name__)

def load_email_settings():
    """
    Loads email settings from environment variables.

    Returns:
        tuple: Tuple containing email username and password.
    """
    return os.getenv('EMAIL_USERNAME'), os.getenv('EMAIL_PASSWORD')

def read_email_template():
    """
    Reads the email template from a file.

    Returns:
        str: Email template.
    """
    with open('email_template/email_template.txt', 'r') as file:
        email_template = file.read()
    logger.info("Read email template.")
    return email_template

def read_follow_up_template():
    """
    Reads the follow-up email template from a file.

    Returns:
        str: Follow-up email template.
    """
    with open('email_template/follow_up_template.txt', 'r') as file:
        follow_up_template = file.read()
    logger.info("Read follow-up email template.")
    return follow_up_template

def read_excel_data():
    """
    Reads data from an Excel file.

    Returns:
        list: List of tuples containing data read from the Excel file.
    """
    excel_file = 'recruiters.xlsx'
    sheet_name = 'Sheet1'
    logger.info(f"Reading data from Excel file: '{excel_file}', sheet: '{sheet_name}'")
    return read_data_from_excel(excel_file, sheet_name)
