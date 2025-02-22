import pytest
import ftplib
from unittest.mock import patch, MagicMock
from src.ftp_connection import establish_ftp_connection

def test_establish_ftp_connection_success():
    """Test successful FTP connection"""
    with patch('ftplib.FTP') as mock_ftp:
        # Create a mock FTP instance
        mock_ftp_instance = MagicMock()
        mock_ftp.return_value = mock_ftp_instance
        
        # Call the function with test credentials
        result = establish_ftp_connection(
            host='test.host.com', 
            username='testuser', 
            password='testpass'
        )
        
        # Verify connection methods were called
        assert result is not None
        mock_ftp_instance.connect.assert_called_once_with(host='test.host.com', port=21)
        mock_ftp_instance.login.assert_called_once_with(user='testuser', passwd='testpass')

def test_establish_ftp_connection_missing_parameters():
    """Test raising ValueError for missing parameters"""
    with pytest.raises(ValueError):
        establish_ftp_connection(host='', username='', password='')
    
    with pytest.raises(ValueError):
        establish_ftp_connection(host='test.host.com', username='', password='')

def test_establish_ftp_connection_connection_error():
    """Test handling of FTP connection errors"""
    with patch('ftplib.FTP') as mock_ftp:
        # Simulate connection error
        mock_ftp.side_effect = ftplib.all_errors
        
        result = establish_ftp_connection(
            host='test.host.com', 
            username='testuser', 
            password='testpass'
        )
        
        # Verify the function returns None on connection error
        assert result is None

def test_establish_ftp_connection_custom_port():
    """Test connection with custom port"""
    with patch('ftplib.FTP') as mock_ftp:
        mock_ftp_instance = MagicMock()
        mock_ftp.return_value = mock_ftp_instance
        
        result = establish_ftp_connection(
            host='test.host.com', 
            username='testuser', 
            password='testpass', 
            port=2121
        )
        
        assert result is not None
        mock_ftp_instance.connect.assert_called_once_with(host='test.host.com', port=2121)