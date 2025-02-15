import os
import pytest
import requests
import requests_mock
from src.file_downloader import download_file_from_url

@pytest.fixture
def mock_download_dir(tmp_path):
    """Create a temporary downloads directory for testing."""
    download_dir = tmp_path / 'downloads'
    download_dir.mkdir()
    return download_dir

def test_download_file_successful(mock_download_dir, requests_mock):
    """Test successful file download."""
    test_url = 'https://example.com/testfile.txt'
    test_content = b'Hello, World!'
    
    # Mock the request
    requests_mock.get(test_url, content=test_content)
    
    # Set downloads directory
    os.chdir(str(mock_download_dir.parent))
    
    # Download file
    downloaded_path = download_file_from_url(test_url)
    
    # Verify file was downloaded
    assert os.path.exists(downloaded_path)
    with open(downloaded_path, 'rb') as f:
        assert f.read() == test_content

def test_download_file_invalid_url():
    """Test handling of invalid URL."""
    with pytest.raises(ValueError):
        download_file_from_url('')
    
    with pytest.raises(ValueError):
        download_file_from_url(None)

def test_download_file_network_error(requests_mock):
    """Test handling of network errors."""
    test_url = 'https://example.com/testfile.txt'
    
    # Mock a network error
    requests_mock.get(test_url, exc=requests.ConnectionError)
    
    with pytest.raises(requests.RequestException):
        download_file_from_url(test_url)

def test_download_file_with_custom_path(mock_download_dir, requests_mock):
    """Test downloading file to a custom path."""
    test_url = 'https://example.com/testfile.txt'
    test_content = b'Custom Path Download'
    custom_path = str(mock_download_dir / 'custom_download.txt')
    
    # Mock the request
    requests_mock.get(test_url, content=test_content)
    
    # Set downloads directory
    os.chdir(str(mock_download_dir.parent))
    
    # Download file to custom path
    downloaded_path = download_file_from_url(test_url, custom_path)
    
    # Verify file was downloaded to custom path
    assert downloaded_path == custom_path
    assert os.path.exists(downloaded_path)
    with open(downloaded_path, 'rb') as f:
        assert f.read() == test_content