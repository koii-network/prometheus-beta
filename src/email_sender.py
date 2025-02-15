import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient, subject, body, 
               smtp_server='smtp.gmail.com', smtp_port=587):
    """
    Send an email using SMTP.
    
    Args:
        sender_email (str): Email address of the sender
        sender_password (str): Password for the sender's email account
        recipient (str): Email address of the recipient
        subject (str): Subject of the email
        body (str): Body text of the email
        smtp_server (str, optional): SMTP server address. Defaults to Gmail's SMTP server.
        smtp_port (int, optional): SMTP server port. Defaults to 587 (TLS).
    
    Returns:
        bool: True if email sent successfully, False otherwise
    
    Raises:
        ValueError: If any required arguments are missing or invalid
        smtplib.SMTPException: For SMTP-related errors
    """
    # Validate inputs
    if not all([sender_email, sender_password, recipient, subject, body]):
        raise ValueError("All email parameters must be provided")
    
    try:
        # Create message container
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient
        message['Subject'] = subject
        
        # Attach body to the email
        message.attach(MIMEText(body, 'plain'))
        
        # Establish a secure session with Gmail's outgoing SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Enable security
            
            # Login to the server
            server.login(sender_email, sender_password)
            
            # Send email
            server.send_message(message)
        
        return True
    
    except smtplib.SMTPAuthenticationError:
        # Handle authentication failures
        return False
    except smtplib.SMTPException as e:
        # Handle other SMTP-related errors
        raise
    except Exception as e:
        # Catch any other unexpected errors
        raise