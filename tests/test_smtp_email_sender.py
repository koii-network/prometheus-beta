import pytest
import smtplib
from unittest.mock import patch
from src.smtp_email_sender import send_email

class TestEmailSender:
    def test_send_email_valid_input(self):
        # Test successful email sending
        with patch('smtplib.SMTP') as mock_smtp:
            result = send_email(
                sender_email='sender@example.com',
                sender_password='password123',
                recipient_email='recipient@example.com',
                subject='Test Subject',
                body='Test Body'
            )
            assert result is True
            mock_smtp.return_value.__enter__.return_value.starttls.assert_called_once()
            mock_smtp.return_value.__enter__.return_value.login.assert_called_once()
            mock_smtp.return_value.__enter__.return_value.send_message.assert_called_once()

    def test_send_email_missing_parameters(self):
        # Test missing parameters
        with pytest.raises(ValueError):
            send_email(
                sender_email='',
                sender_password='password123',
                recipient_email='recipient@example.com',
                subject='Test Subject',
                body='Test Body'
            )

    def test_send_email_smtp_exception(self):
        # Test SMTP sending exception
        with patch('smtplib.SMTP') as mock_smtp:
            mock_smtp.return_value.__enter__.return_value.login.side_effect = smtplib.SMTPException("Login failed")
            
            result = send_email(
                sender_email='sender@example.com',
                sender_password='password123',
                recipient_email='recipient@example.com',
                subject='Test Subject',
                body='Test Body'
            )
            assert result is False

    def test_send_email_custom_smtp_settings(self):
        # Test custom SMTP server and port
        with patch('smtplib.SMTP') as mock_smtp:
            result = send_email(
                sender_email='sender@example.com',
                sender_password='password123',
                recipient_email='recipient@example.com',
                subject='Test Subject',
                body='Test Body',
                smtp_server='custom.smtp.com',
                smtp_port=465
            )
            assert result is True
            mock_smtp.assert_called_with('custom.smtp.com', 465)