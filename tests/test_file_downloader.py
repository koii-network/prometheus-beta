import os
import pytest
import requests
import tempfile
import responses
from src.file_downloader import download_file

class TestFileDownloader:
    @pytest.fixture
    def temp_dir(self):
        """Create a temporary directory for downloads."""
        with tempfile.TemporaryDirectory() as tmpdir:
            yield tmpdir

    @responses.activate
    def test_download_file_with_default_filename(self, temp_dir):
        """Test downloading a file with default filename."""
        # Mock URL and file content
        test_url = 'https://example.com/test.txt'
        test_content = b'Hello, World!'
        responses.add(responses.GET, test_url, body=test_content, status=200)

        # Download file
        save_path = download_file(test_url)
        
        # Verify file was downloaded correctly
        assert os.path.exists(save_path)
        with open(save_path, 'rb') as f:
            assert f.read() == test_content

    @responses.activate
    def test_download_file_with_custom_path(self, temp_dir):
        """Test downloading a file to a specific path."""
        # Mock URL and file content
        test_url = 'https://example.com/sample.txt'
        test_content = b'Custom path download'
        responses.add(responses.GET, test_url, body=test_content, status=200)

        # Custom save path
        custom_path = os.path.join(temp_dir, 'downloaded_file.txt')
        save_path = download_file(test_url, custom_path)
        
        # Verify file was downloaded to correct path
        assert save_path == custom_path
        assert os.path.exists(custom_path)
        with open(custom_path, 'rb') as f:
            assert f.read() == test_content

    def test_invalid_url_raises_error(self):
        """Test that invalid URL raises a ValueError."""
        with pytest.raises(ValueError):
            download_file("")
        with pytest.raises(ValueError):
            download_file(None)

    @responses.activate
    def test_download_non_existent_url(self):
        """Test downloading from a non-existent URL."""
        test_url = 'https://example.com/nonexistent.txt'
        responses.add(responses.GET, test_url, status=404)

        with pytest.raises(requests.RequestException):
            download_file(test_url)

    @responses.activate
    def test_large_file_download(self):
        """Test downloading a larger file in chunks."""
        test_url = 'https://example.com/largefile.bin'
        # Create a larger test content
        test_content = b'0' * (1024 * 1024)  # 1MB of zeros
        responses.add(responses.GET, test_url, body=test_content, status=200)

        # Download large file
        save_path = download_file(test_url)
        
        # Verify file size and content
        assert os.path.exists(save_path)
        assert os.path.getsize(save_path) == len(test_content)
        with open(save_path, 'rb') as f:
            assert f.read() == test_content