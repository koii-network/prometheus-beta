import pytest
import ftplib
from src.ftp_connection import establish_ftp_connection

class MockFTP:
    def __init__(self, host=None, port=None):
        self.host = host
        self.port = port
    
    def connect(self, host, port):
        self.host = host
        self.port = port
    
    def login(self, user, passwd):
        if user == "valid_user" and passwd == "valid_pass":
            return
        raise ftplib.error_perm("Authentication failed")

def test_successful_connection(monkeypatch):
    # Mock successful FTP connection
    monkeypatch.setattr(ftplib, 'FTP', MockFTP)
    
    connection, error = establish_ftp_connection(
        host="example.com", 
        username="valid_user", 
        password="valid_pass"
    )
    
    assert connection is not None
    assert error is None
    assert connection.host == "example.com"
    assert connection.port == 21

def test_missing_parameters():
    # Test with missing parameters
    connection, error = establish_ftp_connection(
        host="", 
        username="user", 
        password=""
    )
    
    assert connection is None
    assert "Missing required connection parameters" in error

def test_authentication_failure(monkeypatch):
    # Mock authentication failure
    monkeypatch.setattr(ftplib, 'FTP', MockFTP)
    
    connection, error = establish_ftp_connection(
        host="example.com", 
        username="invalid_user", 
        password="wrong_pass"
    )
    
    assert connection is None
    assert "FTP Connection Error" in error

def test_connection_with_custom_port(monkeypatch):
    # Test connection with custom port
    monkeypatch.setattr(ftplib, 'FTP', MockFTP)
    
    connection, error = establish_ftp_connection(
        host="example.com", 
        username="valid_user", 
        password="valid_pass",
        port=2121
    )
    
    assert connection is not None
    assert error is None
    assert connection.host == "example.com"
    assert connection.port == 2121