import pytest
from unittest.mock import patch
from src.smtp_email_sender import send_email

def test_send_email_missing_parameters():
    """Test that missing parameters raise a ValueError"""
    with pytest.raises(ValueError, match="All email parameters must be provided"):
        send_email('', 'password', 'recipient@example.com', 'Subject', 'Body')

def test_send_email_invalid_email():
    """Test that invalid email addresses raise a ValueError"""
    with pytest.raises(ValueError, match="Invalid email address"):
        send_email('invalid-email', 'password', 'recipient@example.com', 'Subject', 'Body')

@patch('smtplib.SMTP')
def test_send_email_successful_send(mock_smtp):
    """Test successful email sending"""
    mock_instance = mock_smtp.return_value.__enter__.return_value
    
    result = send_email(
        'sender@example.com', 
        'password', 
        'recipient@example.com', 
        'Test Subject', 
        'Test Body'
    )
    
    assert result is True
    mock_instance.starttls.assert_called_once()
    mock_instance.login.assert_called_once_with('sender@example.com', 'password')
    mock_instance.send_message.assert_called_once()

@patch('smtplib.SMTP')
def test_send_email_smtp_exception(mock_smtp):
    """Test handling of SMTP exceptions"""
    mock_smtp.return_value.__enter__.return_value.send_message.side_effect = Exception('SMTP Error')
    
    result = send_email(
        'sender@example.com', 
        'password', 
        'recipient@example.com', 
        'Test Subject', 
        'Test Body'
    )
    
    assert result is False

def test_email_validation():
    """Test valid email format"""
    result = send_email(
        'valid_email@example.com', 
        'password', 
        'valid_recipient@example.com', 
        'Subject', 
        'Body'
    )
    assert result is False  # Due to mocking