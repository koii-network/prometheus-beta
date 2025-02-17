import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from email_sender import send_email

def test_send_email_invalid_inputs():
    # Test missing parameters
    with pytest.raises(ValueError):
        send_email('', '', '', '', '')
    
    with pytest.raises(ValueError):
        send_email(None, None, None, None, None)

def test_send_email_mock_smtp(mocker):
    # Mock the SMTP server to avoid actually sending emails during testing
    mock_smtp = mocker.patch('smtplib.SMTP')
    mock_login = mock_smtp.return_value.__enter__.return_value.login
    mock_send = mock_smtp.return_value.__enter__.return_value.send_message
    
    # Simulate successful email sending
    result = send_email(
        sender_email='test@example.com', 
        sender_password='password123', 
        recipient_email='recipient@example.com', 
        subject='Test Subject', 
        body='Test Body'
    )
    
    # Verify method calls
    assert result == True
    mock_login.assert_called_once()
    mock_send.assert_called_once()

def test_send_email_smtp_exception(mocker):
    # Simulate SMTP exception
    mocker.patch('smtplib.SMTP', side_effect=smtplib.SMTPException("SMTP Error"))
    
    result = send_email(
        sender_email='test@example.com', 
        sender_password='password123', 
        recipient_email='recipient@example.com', 
        subject='Test Subject', 
        body='Test Body'
    )
    
    assert result == False

def test_send_email_custom_smtp_server():
    # Test with custom SMTP server and port
    result = send_email(
        sender_email='test@example.com', 
        sender_password='password123', 
        recipient_email='recipient@example.com', 
        subject='Test Subject', 
        body='Test Body',
        smtp_server='smtp.customserver.com',
        smtp_port=465
    )
    
    # Since we're mocking, this should always return True
    assert result == True