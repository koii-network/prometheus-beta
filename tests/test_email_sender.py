import pytest
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.email_sender import send_email

def test_send_email_invalid_inputs():
    # Test missing inputs
    with pytest.raises(ValueError):
        send_email('', '', '', '', '')
    
    with pytest.raises(ValueError):
        send_email(None, None, None, None, None)

def test_send_email_invalid_credentials(monkeypatch):
    # Simulate authentication failure by not using real credentials
    result = send_email(
        sender_email='invalid@example.com', 
        sender_password='wrong_password', 
        recipient_email='recipient@example.com', 
        subject='Test Subject', 
        body='Test Body'
    )
    assert result is False

def test_send_email_basic_functionality(monkeypatch):
    # Mock the SMTP methods to avoid actually sending emails
    class MockSMTP:
        def __init__(self, server, port):
            self.server = server
            self.port = port
        
        def starttls(self):
            return True
        
        def login(self, email, password):
            return True
        
        def send_message(self, message):
            return True
        
        def __enter__(self):
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            return False

    # Monkeypatch the smtplib.SMTP to use our mock
    monkeypatch.setattr('smtplib.SMTP', MockSMTP)

    # Test with valid-looking (but not real) inputs
    result = send_email(
        sender_email='sender@example.com', 
        sender_password='test_password', 
        recipient_email='recipient@example.com', 
        subject='Test Subject', 
        body='Test Body'
    )
    assert result is True