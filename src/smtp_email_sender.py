import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email_validator import validate_email, EmailNotValidError

def send_email(sender_email, sender_password, recipient_email, subject, body, 
               smtp_server='smtp.gmail.com', smtp_port=587):
    """
    Send an email using SMTP with optional TLS encryption.

    Args:
        sender_email (str): Email address of the sender
        sender_password (str): Password for the sender's email account
        recipient_email (str): Email address of the recipient
        subject (str): Subject line of the email
        body (str): Body text of the email
        smtp_server (str, optional): SMTP server address. Defaults to Gmail.
        smtp_port (int, optional): SMTP server port. Defaults to 587 (TLS).

    Returns:
        bool: True if email sent successfully, False otherwise

    Raises:
        ValueError: If email validation fails or required parameters are missing
    """
    # Validate input parameters
    if not all([sender_email, sender_password, recipient_email, subject, body]):
        raise ValueError("All email parameters must be provided")

    try:
        # Validate sender and recipient email addresses
        validate_email(sender_email)
        validate_email(recipient_email)
    except EmailNotValidError as e:
        raise ValueError(f"Invalid email address: {str(e)}")

    try:
        # Create message container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach body to the message
        msg.attach(MIMEText(body, 'plain'))

        # Create SMTP session
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Start TLS for security
            server.starttls()
            
            # Login to the server
            server.login(sender_email, sender_password)
            
            # Send email
            server.send_message(msg)
        
        return True

    except smtplib.SMTPException as e:
        # Log or handle SMTP specific errors
        print(f"SMTP error occurred: {str(e)}")
        return False
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {str(e)}")
        return False