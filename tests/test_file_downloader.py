import os
import pytest
import requests
import responses
from src.file_downloader import download_file

@pytest.fixture
def clean_downloads_dir():
    """Ensure downloads directory is clean before tests"""
    os.makedirs('downloads', exist_ok=True)
    for file in os.listdir('downloads'):
        os.remove(os.path.join('downloads', file))

@responses.activate
def test_download_file_default_destination(clean_downloads_dir):
    """Test downloading file with default destination"""
    # Mock URL and file content
    test_url = 'https://example.com/test_file.txt'
    test_content = b'Hello, World!'
    responses.add(responses.GET, test_url, body=test_content, status=200)
    
    # Download file
    downloaded_path = download_file(test_url)
    
    # Verify file was downloaded correctly
    assert os.path.exists(downloaded_path)
    with open(downloaded_path, 'rb') as f:
        assert f.read() == test_content
    assert downloaded_path.endswith('test_file.txt')

@responses.activate
def test_download_file_custom_destination(clean_downloads_dir, tmp_path):
    """Test downloading file with custom destination"""
    # Mock URL and file content
    test_url = 'https://example.com/another_file.pdf'
    test_content = b'PDF Content'
    responses.add(responses.GET, test_url, body=test_content, status=200)
    
    # Custom destination
    custom_path = os.path.join(tmp_path, 'custom_download.pdf')
    
    # Download file
    downloaded_path = download_file(test_url, custom_path)
    
    # Verify file was downloaded correctly
    assert downloaded_path == custom_path
    assert os.path.exists(downloaded_path)
    with open(downloaded_path, 'rb') as f:
        assert f.read() == test_content

def test_download_file_invalid_url():
    """Test handling of invalid URL"""
    with pytest.raises(ValueError):
        download_file('')
    
    with pytest.raises(ValueError):
        download_file(None)

@responses.activate
def test_download_file_network_error():
    """Test handling of network errors"""
    test_url = 'https://example.com/nonexistent_file.txt'
    responses.add(responses.GET, test_url, status=404)
    
    with pytest.raises(requests.RequestException):
        download_file(test_url)