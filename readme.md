# ColdContactXLSX - Cold Email Automation for Job Seekers (Personalized)

## Overview

This project automates the process of sending cold emails from a job seeker (you) to recruiters. It utilizes common email address patterns to generate potential email addresses for recruiters based on their first name, last name, and company name. The goal is to save you time and effort by streamlining the process of reaching out to recruiters for potential job opportunities.

## Quick Start

### Step 1: Prepare Data

1. **Open Excel Spreadsheet**: Open an Excel spreadsheet (e.g., Microsoft Excel, Google Sheets) on your computer. Use VS Code extension if you dont have either.

2. **LinkedIn Search**: Visit LinkedIn (www.linkedin.com) and search for the recruiters or employees by company name. Often, you can find their profiles with their first and last names listed. Use google Chrome extension like to email address of LinkedIn users.

3. **Record Information**: Record the first name and last name of the recruiters or employees found on LinkedIn in your Excel spreadsheet. This will ensure that you have accurate data to use in the email generation process. In the spreadsheet, create columns for "First Name," "Last Name," "Email,", "Company Name" and "Desingation" Enter the relevant information for each recruiter or employee in the respective rows. If the recruiter or employee's email address is available, enter it in the "Email" column. If not, leave the "Email" column blank.

### Step 2.: Update Environment Variables

1. **Create .env File**: Create a new text file on your computer and rename it to `.env` (make sure it doesn't have a `.txt` extension).

2. **Enter Email Credentials**: Open the `.env` file with a text editor (e.g., Notepad, TextEdit) and enter your email credentials in the following format:

   ```plaintext
    EMAIL_USERNAME=example@example.com
    EMAIL_PASSWORD='<Password>'

    YOUR_NAME='<Your name>'
    POSITION='<Position you are apply for>'
    LINK='Any link (github/linked) you wanna send with email'

    SUBJECT='<Email Subject>'
    RESUME='<Resume PDF Path/Location of your disk>'
   ```

   Adjust all the variables in .env according for your self.

   **Gmail Password might not work** 
   Step to Follow (Gmail)
   1. Google Account -> Manage Your Account
   2. Go to Security tab/option
   3. Enable 2-Step Verification 
   4. After enabling, under 2-step verification option itself, Generate App Password 
   5. Use App Password here, instead of email password.


### Step 3: Install the dependency and Run the code
    ``` 
    pip install -r requirements.txt
    python main.py 
    ```

## How It Helped Me Save Time

As a job seeker, I used to spend over 3 hours every day sending cold emails to recruiters in various companies. However, this manual process was time-consuming and often led to fatigue and burnout. With the implementation of this cold email automation project:

## Features

- **Email Address Generation**: The project automatically generates potential email addresses for recruiters based on common patterns, saving you the hassle of manually guessing email addresses.

- **Personalized Cold Emails**: You can send personalized cold emails to recruiters using a predefined email template. The emails contain relevant information, such as your name, target company, designation and a customized message.

- **Attachment Support**: The project supports attaching files, such as resumes, to the cold emails, allowing you to provide additional information to recruiters.

- **Bulk Email Sending:** The project supports sending bulk emails to multiple recruiters simultaneously, allowing you to reach out to a large number of potential employers with minimal effort.

- **Scheduled Email Delivery**: Schedule email delivery for a specific time, allowing you to reach recipients at the most convenient time for them.

- **Batch Processing**: Emails are sent in batches, allowing for smoother processing and reducing the risk of errors or timeouts when sending a large number of emails.

- **Retry Logic**: In case of any errors encountered during email sending, the project includes a retry mechanism. It will attempt to resend the email for a maximum of 3 times before logging an error message if it fails.

- **Follow-Up Emails**: Send follow-up emails to recruiters who have not responded to your initial email, increasing your chances of getting a response.

### Additional Tips

- **Review Email Drafts**: Before running the script, review the email drafts in the `email_template.txt` file to ensure they convey your message effectively.


## TODO

1. **Automate Data Capture:**
   - **Chrome Extension**: Develop a Chrome extension to automate the capture of recruiter and company details from LinkedIn profiles.
  
2. **Integration with OpenAI:**
   - **Dynamic Email Templates**: Integrate with OpenAI to dynamically generate personalized email templates for each recruiter based on their profile and company information.

3. **Streamline Process:**
   - **Eliminate Manual Entry**: Remove the need for manual data entry by seamlessly extracting information from LinkedIn profiles using the Chrome extension.

4. **Enhance User Experience:**
   - **Simplify Setup**: Provide a user-friendly setup process for integrating the Chrome extension with the ColdContactXLSX project.

5. **Maintain Data Privacy:**
   - **Ensure Compliance**: Ensure that the Chrome extension and data processing methods comply with privacy regulations to protect user and recruiter data.


## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.