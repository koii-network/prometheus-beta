import os
import pytest
import requests
import responses
from src.file_downloader import download_file

@pytest.fixture
def mock_download_dir():
    """Create a temporary downloads directory for testing."""
    os.makedirs('downloads', exist_ok=True)
    yield
    # Clean up downloads directory after tests
    for file in os.listdir('downloads'):
        os.remove(os.path.join('downloads', file))
    os.rmdir('downloads')

@responses.activate
def test_download_file_default_destination(mock_download_dir):
    """Test downloading a file with default destination."""
    # Mock the URL and response
    test_url = 'https://example.com/test.txt'
    test_content = b'Hello, World!'
    responses.add(responses.GET, test_url, body=test_content, status=200)

    # Download the file
    downloaded_path = download_file(test_url)
    
    # Verify file was downloaded correctly
    assert os.path.exists(downloaded_path)
    with open(downloaded_path, 'rb') as f:
        assert f.read() == test_content

@responses.activate
def test_download_file_custom_destination(mock_download_dir):
    """Test downloading a file with a custom destination."""
    test_url = 'https://example.com/sample.pdf'
    test_content = b'PDF content here'
    custom_path = 'downloads/custom_file.pdf'
    
    responses.add(responses.GET, test_url, body=test_content, status=200)

    # Download the file to a custom location
    downloaded_path = download_file(test_url, custom_path)
    
    # Verify file was downloaded correctly
    assert downloaded_path == custom_path
    assert os.path.exists(custom_path)
    with open(custom_path, 'rb') as f:
        assert f.read() == test_content

def test_download_file_invalid_url():
    """Test handling of invalid URL."""
    with pytest.raises(ValueError):
        download_file('')
    
    with pytest.raises(ValueError):
        download_file(None)

@responses.activate
def test_download_file_network_error():
    """Test handling of network-related errors."""
    test_url = 'https://example.com/nonexistent.txt'
    
    # Simulate a network error
    responses.add(responses.GET, test_url, body=requests.exceptions.RequestException())
    
    with pytest.raises(requests.RequestException):
        download_file(test_url)

# Make sure to update requirements.txt with test dependencies