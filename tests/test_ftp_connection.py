import pytest
import ftplib
from src.ftp_connection import establish_ftp_connection

def test_establish_ftp_connection_success(mocker):
    # Mock the FTP connection to simulate a successful connection
    mock_ftp = mocker.Mock(spec=ftplib.FTP)
    mocker.patch('ftplib.FTP', return_value=mock_ftp)

    connection = establish_ftp_connection(
        host='test.example.com', 
        username='testuser', 
        password='testpass'
    )
    
    assert connection is not None
    connection.connect.assert_called_once_with(host='test.example.com', port=21)
    connection.login.assert_called_once_with(user='testuser', passwd='testpass')

def test_establish_ftp_connection_missing_parameters():
    with pytest.raises(ValueError, match="Host, username, and password are required"):
        establish_ftp_connection(host='', username='', password='')

def test_establish_ftp_connection_ftp_error(mocker):
    # Simulate an FTP connection error
    mocker.patch('ftplib.FTP.connect', side_effect=ftplib.all_errors("Connection failed"))
    
    with pytest.raises(ftplib.all_errors):
        establish_ftp_connection(
            host='error.example.com', 
            username='testuser', 
            password='testpass'
        )

def test_establish_ftp_connection_custom_port():
    # Mock the FTP connection
    mock_ftp = mocker.Mock(spec=ftplib.FTP)
    mocker.patch('ftplib.FTP', return_value=mock_ftp)

    connection = establish_ftp_connection(
        host='test.example.com', 
        username='testuser', 
        password='testpass',
        port=2121
    )
    
    connection.connect.assert_called_once_with(host='test.example.com', port=2121)