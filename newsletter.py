from dotenv import load_dotenv
from email import EmailMessage
import os

#Load secrets from .env
load_dotenv()
gmail_address = os.getenv("GMAIL_ADDRESS")
gmail_password = os.getenv("GMAIL_PASSWORD")

#Create the email
email = EmailMessage()

# Subject line of the email
email["Subject"] = "Automated newsletter with Python & Github Actions"
# Sender of the email
email["From"] = gmail_address

# Add HTML content to the email
email.add_alternative(f"""\
<html>
<head></head>
<body>
    <p>Brought to you by <b>Sleep1ng-Giant</b></p>
</body>
</html>
""", subtype="html")
#TODO Add file passthrough

# Add plaintext alternative as fallback option
email.set_content("Brought to you by Sleep1ng-Giant")
