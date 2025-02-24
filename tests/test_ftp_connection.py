import pytest
import socket
import ftplib
from unittest.mock import patch, MagicMock
from src.ftp_connection import establish_ftp_connection

def test_establish_ftp_connection_without_auth():
    with patch('ftplib.FTP') as mock_ftp:
        # Mock successful connection
        mock_ftp_instance = MagicMock()
        mock_ftp.return_value = mock_ftp_instance
        
        connection = establish_ftp_connection('example.com')
        
        assert connection == mock_ftp_instance
        mock_ftp.assert_called_once_with(timeout=30)
        mock_ftp_instance.connect.assert_called_once_with(host='example.com', port=21)

def test_establish_ftp_connection_with_auth():
    with patch('ftplib.FTP') as mock_ftp:
        # Mock successful connection with authentication
        mock_ftp_instance = MagicMock()
        mock_ftp.return_value = mock_ftp_instance
        
        connection = establish_ftp_connection('example.com', 'user', 'pass')
        
        assert connection == mock_ftp_instance
        mock_ftp.assert_called_once_with(timeout=30)
        mock_ftp_instance.connect.assert_called_once_with(host='example.com', port=21)
        mock_ftp_instance.login.assert_called_once_with(user='user', passwd='pass')

def test_establish_ftp_connection_invalid_host():
    with pytest.raises(ValueError, match="Host must be a non-empty string"):
        establish_ftp_connection('')
    
    with pytest.raises(ValueError, match="Host must be a non-empty string"):
        establish_ftp_connection(None)

def test_establish_ftp_connection_incomplete_credentials():
    with pytest.raises(ValueError, match="Both username and password must be provided for authentication"):
        establish_ftp_connection('example.com', username='user')
    
    with pytest.raises(ValueError, match="Both username and password must be provided for authentication"):
        establish_ftp_connection('example.com', password='pass')

def test_establish_ftp_connection_host_resolution_error():
    with patch('socket.create_connection', side_effect=socket.gaierror):
        with pytest.raises(ConnectionError, match="Could not resolve host"):
            establish_ftp_connection('nonexistent.host')

def test_establish_ftp_connection_timeout():
    with patch('socket.create_connection', side_effect=socket.timeout):
        with pytest.raises(ConnectionError, match="Connection to"):
            establish_ftp_connection('slow.host')

def test_establish_ftp_connection_ftp_error():
    with patch('ftplib.FTP') as mock_ftp:
        mock_ftp_instance = MagicMock()
        mock_ftp.return_value = mock_ftp_instance
        
        mock_ftp_instance.connect.side_effect = ftplib.error_perm("Authentication failed")
        
        with pytest.raises(ConnectionError, match="FTP connection error"):
            establish_ftp_connection('example.com', 'user', 'wrongpass')