import os
import pytest
import requests
import requests_mock
from src.download_file import download_file

def test_download_file_with_url():
    # Setup a mock URL and content
    test_url = 'https://example.com/testfile.txt'
    test_content = b'Hello, World!'
    
    # Use requests_mock to simulate file download
    with requests_mock.Mocker() as m:
        m.get(test_url, content=test_content)
        
        # Download the file
        downloaded_path = download_file(test_url)
        
        # Verify file was downloaded
        assert os.path.exists(downloaded_path)
        
        # Check file content
        with open(downloaded_path, 'rb') as f:
            assert f.read() == test_content
        
        # Clean up
        os.remove(downloaded_path)

def test_download_file_with_custom_destination():
    # Setup a mock URL and content
    test_url = 'https://example.com/testfile.txt'
    test_content = b'Hello, World!'
    test_destination = 'test_downloads/custom_file.txt'
    
    # Use requests_mock to simulate file download
    with requests_mock.Mocker() as m:
        m.get(test_url, content=test_content)
        
        # Download the file to a custom destination
        downloaded_path = download_file(test_url, test_destination)
        
        # Verify file was downloaded to correct location
        assert downloaded_path == test_destination
        assert os.path.exists(downloaded_path)
        
        # Check file content
        with open(downloaded_path, 'rb') as f:
            assert f.read() == test_content
        
        # Clean up
        os.remove(downloaded_path)
        os.rmdir('test_downloads')

def test_download_file_invalid_url():
    # Test invalid URL scenarios
    with pytest.raises(ValueError):
        download_file('')
    
    with pytest.raises(ValueError):
        download_file(None)

def test_download_file_network_error():
    # Simulate a network error
    test_url = 'https://example.com/nonexistent.txt'
    
    with requests_mock.Mocker() as m:
        m.get(test_url, status_code=404)
        
        with pytest.raises(RuntimeError):
            download_file(test_url)