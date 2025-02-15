import pytest
import ftplib
from unittest.mock import patch, MagicMock
from src.ftp_connection import establish_ftp_connection

def test_establish_ftp_connection_success():
    """Test successful FTP connection"""
    with patch('ftplib.FTP') as mock_ftp:
        # Mock the FTP connection methods
        mock_ftp_instance = MagicMock()
        mock_ftp.return_value = mock_ftp_instance

        # Call the function with test credentials
        result = establish_ftp_connection('test.host', 'testuser', 'testpass')
        
        # Verify connection methods were called
        mock_ftp.assert_called_once()
        mock_ftp_instance.connect.assert_called_once_with(host='test.host', port=21)
        mock_ftp_instance.login.assert_called_once_with(user='testuser', passwd='testpass')
        assert result == mock_ftp_instance

def test_establish_ftp_connection_missing_parameters():
    """Test function raises ValueError for missing parameters"""
    with pytest.raises(ValueError, match="Host, username, and password are required"):
        establish_ftp_connection('', 'user', 'pass')
    
    with pytest.raises(ValueError, match="Host, username, and password are required"):
        establish_ftp_connection('host', '', 'pass')
    
    with pytest.raises(ValueError, match="Host, username, and password are required"):
        establish_ftp_connection('host', 'user', '')

def test_establish_ftp_connection_connection_error():
    """Test connection error handling"""
    with patch('ftplib.FTP') as mock_ftp:
        # Simulate connection error
        mock_ftp.side_effect = ftplib.all_errors("Connection failed")
        
        with pytest.raises(ConnectionError, match="FTP connection failed"):
            establish_ftp_connection('invalid.host', 'user', 'pass')

def test_establish_ftp_connection_hostname_error():
    """Test hostname resolution error"""
    with patch('socket.gaierror', new=Exception):
        with patch('ftplib.FTP') as mock_ftp:
            mock_ftp.side_effect = socket.gaierror
            
            with pytest.raises(ConnectionError, match="Could not resolve hostname"):
                establish_ftp_connection('non.existent.host', 'user', 'pass')

def test_establish_ftp_connection_custom_port():
    """Test connection with custom port"""
    with patch('ftplib.FTP') as mock_ftp:
        mock_ftp_instance = MagicMock()
        mock_ftp.return_value = mock_ftp_instance

        result = establish_ftp_connection('test.host', 'testuser', 'testpass', port=2121)
        
        mock_ftp_instance.connect.assert_called_once_with(host='test.host', port=2121)
        assert result == mock_ftp_instance