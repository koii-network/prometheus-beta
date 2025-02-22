import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body, 
               smtp_server='smtp.gmail.com', smtp_port=587):
    """
    Send an email using SMTP protocol.
    
    Args:
        sender_email (str): Email address of the sender
        sender_password (str): Password for the sender's email account
        recipient_email (str): Email address of the recipient
        subject (str): Subject line of the email
        body (str): Body text of the email
        smtp_server (str, optional): SMTP server address. Defaults to Gmail's SMTP server.
        smtp_port (int, optional): SMTP server port. Defaults to 587 (TLS).
    
    Returns:
        bool: True if email sent successfully, False otherwise
    
    Raises:
        ValueError: If any required parameters are missing or invalid
    """
    # Validate input parameters
    if not all([sender_email, sender_password, recipient_email, subject, body]):
        raise ValueError("All email parameters must be provided")
    
    try:
        # Create message container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Attach the body of the message
        msg.attach(MIMEText(body, 'plain'))
        
        # Establish a secure session with Gmail's outgoing SMTP server using TLS
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        
        # Login to the server
        server.login(sender_email, sender_password)
        
        # Send email
        server.send_message(msg)
        
        # Close the connection
        server.quit()
        
        return True
    
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
        return False
    except Exception as e:
        print(f"An error occurred while sending email: {e}")
        return False