import smtplib
import validate_email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body, 
               smtp_server='smtp.gmail.com', smtp_port=587):
    """
    Send an email using SMTP.

    Args:
        sender_email (str): Email address of the sender
        sender_password (str): Password for the sender's email account
        recipient_email (str): Email address of the recipient
        subject (str): Subject line of the email
        body (str): Body text of the email
        smtp_server (str, optional): SMTP server address. Defaults to Gmail's.
        smtp_port (int, optional): SMTP server port. Defaults to 587.

    Returns:
        bool: True if email sent successfully, False otherwise

    Raises:
        ValueError: If email addresses are invalid or if required parameters are missing
    """
    # Validate input parameters
    if not sender_email or not sender_password or not recipient_email or not subject or not body:
        raise ValueError("All parameters must be provided and non-empty")

    # Validate email addresses
    if not validate_email.validate_email(sender_email):
        raise ValueError(f"Invalid sender email address: {sender_email}")
    
    if not validate_email.validate_email(recipient_email):
        raise ValueError(f"Invalid recipient email address: {recipient_email}")

    try:
        # Create message container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach body to message
        msg.attach(MIMEText(body, 'plain'))

        # Establish a secure session with Gmail's outgoing SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Enable security
            # Login to server
            server.login(sender_email, sender_password)
            
            # Send email
            server.send_message(msg)

        return True

    except smtplib.SMTPAuthenticationError:
        raise ValueError("Authentication failed. Check email and password.")
    except smtplib.SMTPException as e:
        raise RuntimeError(f"SMTP error occurred: {str(e)}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error sending email: {str(e)}")