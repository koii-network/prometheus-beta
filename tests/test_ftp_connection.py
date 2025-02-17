import pytest
import ftplib
from unittest.mock import patch, MagicMock
from src.ftp_connection import establish_ftp_connection

def test_successful_ftp_connection():
    """Test a successful FTP connection"""
    with patch('ftplib.FTP') as mock_ftp:
        mock_instance = MagicMock()
        mock_ftp.return_value = mock_instance
        
        result = establish_ftp_connection(
            host='ftp.example.com', 
            username='testuser', 
            password='testpass'
        )
        
        assert result is not None
        mock_ftp.return_value.connect.assert_called_once_with(
            host='ftp.example.com', 
            port=21
        )
        mock_ftp.return_value.login.assert_called_once_with(
            user='testuser', 
            passwd='testpass'
        )

def test_connection_failure():
    """Test FTP connection failure"""
    with patch('ftplib.FTP') as mock_ftp:
        mock_ftp.side_effect = ftplib.error_perm("Login failed")
        
        result = establish_ftp_connection(
            host='ftp.example.com', 
            username='baduser', 
            password='badpass'
        )
        
        assert result is None

def test_missing_parameters():
    """Test missing parameters raise ValueError"""
    with pytest.raises(ValueError):
        establish_ftp_connection(
            host='', 
            username='', 
            password=''
        )

def test_custom_port():
    """Test connection with a custom port"""
    with patch('ftplib.FTP') as mock_ftp:
        mock_instance = MagicMock()
        mock_ftp.return_value = mock_instance
        
        result = establish_ftp_connection(
            host='ftp.example.com', 
            username='testuser', 
            password='testpass', 
            port=2121
        )
        
        assert result is not None
        mock_ftp.return_value.connect.assert_called_once_with(
            host='ftp.example.com', 
            port=2121
        )

def test_connection_timeout():
    """Test connection with custom timeout"""
    with patch('ftplib.FTP') as mock_ftp:
        mock_instance = MagicMock()
        mock_ftp.return_value = mock_instance
        
        result = establish_ftp_connection(
            host='ftp.example.com', 
            username='testuser', 
            password='testpass', 
            timeout=10
        )
        
        assert result is not None
        mock_ftp = ftplib.FTP(timeout=10)
        assert mock_ftp.timeout == 10