import pytest
import ftplib
import socket
from unittest.mock import patch, MagicMock
from src.ftp_connection import establish_ftp_connection

class MockFTP:
    def __init__(self, *args, **kwargs):
        pass
    
    def connect(self, host, port):
        pass
    
    def login(self, user, passwd):
        pass

def test_successful_ftp_connection():
    with patch('ftplib.FTP', MockFTP):
        with patch.object(MockFTP, 'connect') as mock_connect, \
             patch.object(MockFTP, 'login') as mock_login:
            connection = establish_ftp_connection('test.server.com', 'user', 'pass')
            assert connection is not None
            mock_connect.assert_called_once_with(host='test.server.com', port=21)
            mock_login.assert_called_once_with(user='user', passwd='pass')

def test_empty_host_raises_error():
    with pytest.raises(ValueError, match="Host, username, and password must be provided"):
        establish_ftp_connection('', 'user', 'pass')

def test_empty_username_raises_error():
    with pytest.raises(ValueError, match="Host, username, and password must be provided"):
        establish_ftp_connection('test.server.com', '', 'pass')

def test_empty_password_raises_error():
    with pytest.raises(ValueError, match="Host, username, and password must be provided"):
        establish_ftp_connection('test.server.com', 'user', '')

def test_connection_refused():
    with patch('ftplib.FTP') as mock_ftp:
        mock_ftp.side_effect = socket.error("Connection refused")
        with pytest.raises(ConnectionRefusedError):
            establish_ftp_connection('invalid.server.com', 'user', 'pass')

def test_authentication_failure():
    with patch('ftplib.FTP') as mock_ftp:
        mock_instance = mock_ftp.return_value
        mock_instance.login.side_effect = ftplib.error_perm("Authentication failed")
        with pytest.raises(ConnectionRefusedError, match="Authentication failed"):
            establish_ftp_connection('test.server.com', 'user', 'wrongpass')

def test_connection_timeout():
    with patch('ftplib.FTP') as mock_ftp:
        mock_ftp.side_effect = socket.timeout("Connection timed out")
        with pytest.raises(socket.timeout):
            establish_ftp_connection('slow.server.com', 'user', 'pass', timeout=1)