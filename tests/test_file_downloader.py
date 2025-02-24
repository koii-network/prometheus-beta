import os
import pytest
import requests
import requests_mock

from src.file_downloader import download_file

@pytest.fixture
def temp_downloads_dir(tmpdir):
    """Create a temporary downloads directory."""
    downloads_dir = tmpdir.mkdir('downloads')
    return str(downloads_dir)

def test_download_file_success(requests_mock, temp_downloads_dir, monkeypatch):
    """Test successful file download."""
    # Setup
    test_url = 'https://example.com/testfile.txt'
    test_content = b'Hello, World!'
    requests_mock.get(test_url, content=test_content)
    
    # Monkeypatch the downloads path
    monkeypatch.chdir(temp_downloads_dir)
    monkeypatch.setattr('src.file_downloader.os.path.join', 
                        lambda base, filename: os.path.join(temp_downloads_dir, filename))
    
    # Expected destination
    expected_path = os.path.join(temp_downloads_dir, 'testfile.txt')
    
    # Execute
    downloaded_path = download_file(test_url)
    
    # Verify
    assert downloaded_path == expected_path
    assert os.path.exists(downloaded_path)
    with open(downloaded_path, 'rb') as f:
        assert f.read() == test_content

def test_download_file_custom_destination(requests_mock, tmpdir):
    """Test downloading file to a custom destination."""
    # Setup
    test_url = 'https://example.com/testfile.txt'
    test_content = b'Custom destination test'
    requests_mock.get(test_url, content=test_content)
    
    custom_path = os.path.join(str(tmpdir), 'custom_downloads', 'myfile.txt')
    
    # Execute
    downloaded_path = download_file(test_url, custom_path)
    
    # Verify
    assert downloaded_path == custom_path
    assert os.path.exists(downloaded_path)
    with open(downloaded_path, 'rb') as f:
        assert f.read() == test_content

def test_download_file_invalid_url():
    """Test handling of invalid URL."""
    with pytest.raises(ValueError, match="Invalid URL"):
        download_file('')
    
    with pytest.raises(ValueError, match="Invalid URL"):
        download_file(None)

def test_download_file_network_error(requests_mock):
    """Test handling of network errors."""
    test_url = 'https://example.com/testfile.txt'
    requests_mock.get(test_url, exc=requests.ConnectionError)
    
    with pytest.raises(requests.RequestException):
        download_file(test_url)

def test_download_file_bad_status(requests_mock):
    """Test handling of bad HTTP status codes."""
    test_url = 'https://example.com/testfile.txt'
    requests_mock.get(test_url, status_code=404)
    
    with pytest.raises(requests.HTTPError):
        download_file(test_url)