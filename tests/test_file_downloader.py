import os
import pytest
import requests
from src.file_downloader import download_file

class MockResponse:
    def __init__(self, content=b'test content', status_code=200, headers=None):
        self.content = content
        self.status_code = status_code
        self.headers = headers or {}
        
    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"HTTP Error {self.status_code}")
    
    def iter_content(self, chunk_size):
        yield self.content

def test_download_file_basic(tmp_path, monkeypatch):
    # Mock requests.get to return a controlled response
    def mock_get(*args, **kwargs):
        return MockResponse()
    
    monkeypatch.setattr(requests, 'get', mock_get)
    
    # Use a temporary path for saving
    save_path = tmp_path / 'test_download.txt'
    
    # Download the file
    downloaded_path = download_file('http://example.com/test.txt', str(save_path))
    
    # Verify file was downloaded
    assert os.path.exists(downloaded_path)
    assert downloaded_path == str(save_path)
    
    # Check file contents
    with open(downloaded_path, 'rb') as f:
        assert f.read() == b'test content'

def test_download_file_default_path(tmp_path, monkeypatch):
    # Mock requests.get to return a controlled response
    def mock_get(*args, **kwargs):
        return MockResponse(headers={'Content-Disposition': 'attachment; filename="downloaded.txt"'})
    
    monkeypatch.setattr(requests, 'get', mock_get)
    
    # Download with default path generation
    downloaded_path = download_file('http://example.com/file')
    
    # Verify file was downloaded
    assert os.path.exists(downloaded_path)
    assert os.path.basename(downloaded_path) == 'downloaded.txt'

def test_invalid_url_raises_error():
    # Test invalid URL inputs
    with pytest.raises(ValueError):
        download_file('')
    
    with pytest.raises(ValueError):
        download_file(None)

def test_download_network_error(monkeypatch):
    # Simulate network error
    def mock_get(*args, **kwargs):
        raise requests.RequestException("Network error")
    
    monkeypatch.setattr(requests, 'get', mock_get)
    
    with pytest.raises(requests.RequestException):
        download_file('http://example.com/nonexistent')

def test_http_error(monkeypatch):
    # Simulate HTTP error
    def mock_get(*args, **kwargs):
        response = MockResponse(status_code=404)
        return response
    
    monkeypatch.setattr(requests, 'get', mock_get)
    
    with pytest.raises(requests.HTTPError):
        download_file('http://example.com/404')

def test_large_file_download(tmp_path, monkeypatch):
    # Simulate large file download
    large_content = b'x' * (1024 * 1024)  # 1MB of data
    
    def mock_get(*args, **kwargs):
        return MockResponse(content=large_content)
    
    monkeypatch.setattr(requests, 'get', mock_get)
    
    save_path = tmp_path / 'large_file.bin'
    downloaded_path = download_file('http://example.com/largefile', str(save_path))
    
    # Verify file was downloaded correctly
    assert os.path.exists(downloaded_path)
    with open(downloaded_path, 'rb') as f:
        assert f.read() == large_content