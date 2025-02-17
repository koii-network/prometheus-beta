import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email: str, 
               sender_password: str, 
               recipient_email: str, 
               subject: str, 
               body: str, 
               smtp_server: str = 'smtp.gmail.com', 
               smtp_port: int = 587) -> bool:
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
    """
    try:
        # Create message container
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        
        # Attach body to the message
        message.attach(MIMEText(body, 'plain'))
        
        # Create SMTP session
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Start TLS for security
            server.starttls()
            
            # Login to the server
            server.login(sender_email, sender_password)
            
            # Send email
            server.send_message(message)
        
        return True
    
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
        return False
    except Exception as e:
        print(f"An error occurred while sending email: {e}")
        return False