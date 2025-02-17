import pytest
import sys
import os

# Add the src directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from smtp_email_sender import send_email

def test_send_email_invalid_credentials():
    """Test sending email with invalid credentials."""
    result = send_email(
        sender_email='invalid_email@example.com', 
        sender_password='wrong_password', 
        recipient_email='test@example.com', 
        subject='Test Subject', 
        body='Test Body'
    )
    assert result == False

def test_send_email_invalid_recipient():
    """Test sending email with invalid recipient."""
    result = send_email(
        sender_email='valid_email@gmail.com', 
        sender_password='correct_password', 
        recipient_email='invalid_recipient', 
        subject='Test Subject', 
        body='Test Body'
    )
    assert result == False

def test_send_email_empty_params():
    """Test sending email with empty parameters."""
    with pytest.raises(TypeError):
        send_email(
            sender_email='', 
            sender_password='', 
            recipient_email='', 
            subject='', 
            body=''
        )

def test_send_email_wrong_server():
    """Test sending email with incorrect SMTP server."""
    result = send_email(
        sender_email='valid_email@gmail.com', 
        sender_password='correct_password', 
        recipient_email='test@example.com', 
        subject='Test Subject', 
        body='Test Body', 
        smtp_server='non_existent_server.com'
    )
    assert result == False