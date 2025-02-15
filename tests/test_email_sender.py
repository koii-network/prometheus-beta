import pytest
import smtplib
from src.email_sender import send_email

def test_send_email_invalid_inputs():
    # Test missing inputs
    with pytest.raises(ValueError):
        send_email('', 'pass', 'rec@example.com', 'Test', 'Body')
    
    with pytest.raises(ValueError):
        send_email('sender@example.com', '', 'rec@example.com', 'Test', 'Body')

def test_send_email_wrong_credentials(monkeypatch):
    # Simulate SMTP authentication failure
    def mock_login(self, *args):
        raise smtplib.SMTPAuthenticationError(534, 'Authentication failed')
    
    monkeypatch.setattr(smtplib.SMTP, 'login', mock_login)
    
    assert send_email(
        'invalid@example.com', 
        'wrongpassword', 
        'recipient@example.com', 
        'Test Subject', 
        'Test Body'
    ) == False

def test_send_email_successful_mock(monkeypatch):
    # Mock a successful email send
    class MockSMTP:
        def __init__(self, *args):
            pass
        
        def starttls(self):
            pass
        
        def login(self, *args):
            pass
        
        def send_message(self, msg):
            pass
        
        def __enter__(self):
            return self
        
        def __exit__(self, *args):
            pass
    
    monkeypatch.setattr(smtplib, 'SMTP', MockSMTP)
    
    result = send_email(
        'sender@example.com', 
        'password', 
        'recipient@example.com', 
        'Test Subject', 
        'Test Body'
    )
    
    assert result == True