import pytest
import requests
from unittest.mock import patch
from src.web_scraper import scrape_webpage

class MockResponse:
    def __init__(self, text, status_code=200):
        self.text = text
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.exceptions.HTTPError(f"HTTP Error {self.status_code}")

def test_scrape_webpage_basic():
    mock_html = """
    <html>
        <body>
            <p>First paragraph</p>
            <p>Second paragraph</p>
        </body>
    </html>
    """
    
    with patch('requests.get', return_value=MockResponse(mock_html)):
        results = scrape_webpage('http://example.com')
        assert results == ['First paragraph', 'Second paragraph']

def test_scrape_webpage_with_attr():
    mock_html = """
    <html>
        <body>
            <div class="content">Article 1</div>
            <div class="content">Article 2</div>
            <div>Not content</div>
        </body>
    </html>
    """
    
    with patch('requests.get', return_value=MockResponse(mock_html)):
        results = scrape_webpage('http://example.com', tag='div', attr={'class': 'content'})
        assert results == ['Article 1', 'Article 2']

def test_scrape_webpage_invalid_url():
    with patch('requests.get', side_effect=requests.exceptions.ConnectionError):
        with pytest.raises(ValueError, match="Error accessing webpage"):
            scrape_webpage('http://nonexistent.url')

def test_scrape_webpage_no_results():
    mock_html = "<html><body></body></html>"
    
    with patch('requests.get', return_value=MockResponse(mock_html)):
        results = scrape_webpage('http://example.com')
        assert results == []