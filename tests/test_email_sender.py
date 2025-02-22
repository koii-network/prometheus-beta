import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from email_sender import send_email

def test_send_email_invalid_inputs():
    # Test with missing parameters
    with pytest.raises(ValueError):
        send_email('', '', '', '', '')
    
    with pytest.raises(ValueError):
        send_email(None, None, None, None, None)

def test_send_email_incorrect_credentials(mocker):
    # Mock the SMTP server to simulate authentication failure
    mocker.patch('smtplib.SMTP.login', side_effect=smtplib.SMTPAuthenticationError(534, 'Authentication failed'))
    
    result = send_email(
        'invalid_email@example.com', 
        'wrong_password', 
        'recipient@example.com', 
        'Test Subject', 
        'Test Body'
    )
    
    assert result is False

def test_send_email_happy_path(mocker):
    # Mock the SMTP server to simulate successful email sending
    mock_server = mocker.patch('smtplib.SMTP')
    mock_instance = mock_server.return_value
    
    result = send_email(
        'sender@example.com', 
        'correct_password', 
        'recipient@example.com', 
        'Test Subject', 
        'Test Body'
    )
    
    assert result is True
    # Verify that key SMTP methods were called
    mock_instance.starttls.assert_called_once()
    mock_instance.login.assert_called_once()
    mock_instance.send_message.assert_called_once()
    mock_instance.quit.assert_called_once()