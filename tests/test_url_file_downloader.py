import os
import pytest
import requests
import requests_mock
from src.url_file_downloader import download_file_from_url

@pytest.fixture
def sample_download_url():
    return 'https://example.com/sample_file.txt'

def test_download_file_with_default_path(sample_download_url, tmp_path):
    # Mock the requests.get method
    with requests_mock.Mocker() as m:
        m.get(sample_download_url, text='Sample file content')
        
        # Change current working directory to temporary path
        with pytest.MonkeyPatch.context() as mp:
            mp.chdir(tmp_path)
            
            # Download file
            downloaded_path = download_file_from_url(sample_download_url)
            
            # Check file was downloaded
            assert os.path.exists(downloaded_path)
            assert os.path.basename(downloaded_path) == 'sample_file.txt'
            
            # Check file contents
            with open(downloaded_path, 'r') as file:
                assert file.read() == 'Sample file content'

def test_download_file_with_custom_path(sample_download_url, tmp_path):
    # Mock the requests.get method
    with requests_mock.Mocker() as m:
        m.get(sample_download_url, text='Custom file content')
        
        # Change current working directory to temporary path
        with pytest.MonkeyPatch.context() as mp:
            mp.chdir(tmp_path)
            
            custom_path = 'downloads/custom_file.txt'
            downloaded_path = download_file_from_url(sample_download_url, custom_path)
            
            # Check file was downloaded
            assert os.path.exists(downloaded_path)
            assert downloaded_path == custom_path
            
            # Check file contents
            with open(downloaded_path, 'r') as file:
                assert file.read() == 'Custom file content'

def test_invalid_url():
    with pytest.raises(ValueError, match="Invalid URL"):
        download_file_from_url('')
    
    with pytest.raises(ValueError, match="Invalid URL"):
        download_file_from_url('invalid_url')

def test_download_error(sample_download_url):
    with requests_mock.Mocker() as m:
        m.get(sample_download_url, status_code=404)
        
        with pytest.raises(RuntimeError, match="Error downloading file"):
            download_file_from_url(sample_download_url)