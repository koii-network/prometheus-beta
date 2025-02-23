import pytest
from unittest.mock import patch
from src.email_sender import send_email

# Mock credentials - replace with your own for actual testing
MOCK_SENDER_EMAIL = "test.sender@example.com"
MOCK_SENDER_PASSWORD = "mock_password"
MOCK_RECIPIENT_EMAIL = "test.recipient@example.com"

def test_send_email_parameter_validation():
    """Test parameter validation in send_email function"""
    # Test missing parameters
    with pytest.raises(ValueError, match="All parameters must be provided"):
        send_email("", "password", "recipient@test.com", "Subject", "Body")
    
    with pytest.raises(ValueError, match="Invalid sender email address"):
        send_email("invalid_email", "password", "recipient@test.com", "Subject", "Body")
    
    with pytest.raises(ValueError, match="Invalid recipient email address"):
        send_email("sender@test.com", "password", "invalid_email", "Subject", "Body")

@patch('smtplib.SMTP')
def test_send_email_successful_sending(mock_smtp):
    """Test successful email sending with mocked SMTP"""
    result = send_email(
        MOCK_SENDER_EMAIL, 
        MOCK_SENDER_PASSWORD, 
        MOCK_RECIPIENT_EMAIL, 
        "Test Subject", 
        "Test Body"
    )
    assert result is True
    
    # Verify SMTP methods were called correctly
    mock_smtp.return_value.__enter__.return_value.starttls.assert_called_once()
    mock_smtp.return_value.__enter__.return_value.login.assert_called_once_with(
        MOCK_SENDER_EMAIL, MOCK_SENDER_PASSWORD
    )
    mock_smtp.return_value.__enter__.return_value.send_message.assert_called_once()

@patch('smtplib.SMTP')
def test_send_email_authentication_failure(mock_smtp):
    """Test handling of authentication failure"""
    mock_smtp.return_value.__enter__.return_value.login.side_effect = smtplib.SMTPAuthenticationError(
        code=535, msg="Authentication failed"
    )
    
    with pytest.raises(ValueError, match="Authentication failed"):
        send_email(
            MOCK_SENDER_EMAIL, 
            "wrong_password", 
            MOCK_RECIPIENT_EMAIL, 
            "Test Subject", 
            "Test Body"
        )

@patch('smtplib.SMTP')
def test_send_email_smtp_exception(mock_smtp):
    """Test handling of SMTP exceptions"""
    mock_smtp.return_value.__enter__.return_value.send_message.side_effect = smtplib.SMTPException(
        "SMTP Error"
    )
    
    with pytest.raises(RuntimeError, match="SMTP error occurred"):
        send_email(
            MOCK_SENDER_EMAIL, 
            MOCK_SENDER_PASSWORD, 
            MOCK_RECIPIENT_EMAIL, 
            "Test Subject", 
            "Test Body"
        )