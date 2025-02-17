import pytest
import requests
from unittest.mock import patch
from src.web_scraper import scrape_webpage

class MockResponse:
    def __init__(self, text, status_code=200):
        self.text = text
        self.status_code = status_code
    
    def raise_for_status(self):
        pass

@pytest.mark.parametrize("url,selector,mock_html,expected", [
    # Test with simple HTML and no selector
    ("https://example.com", None, 
     "<html><body><p>Hello</p><p>World</p></body></html>", 
     {"data": ["Hello", "World"], "url": "https://example.com", "status_code": 200}),
    
    # Test with specific selector
    ("https://example.com", "p", 
     "<html><body><p>Hello</p><div>Ignored</div><p>World</p></body></html>", 
     {"data": ["Hello", "World"], "url": "https://example.com", "status_code": 200}),
    
    # Test with empty results
    ("https://example.com", ".nonexistent", 
     "<html><body><p>Hello</p></body></html>", 
     {"data": [], "url": "https://example.com", "status_code": 200})
])
def test_scrape_webpage_success(url, selector, mock_html, expected):
    with patch('requests.get') as mock_get:
        mock_get.return_value = MockResponse(mock_html)
        result = scrape_webpage(url, selector)
        assert result == expected

def test_scrape_webpage_invalid_url():
    with pytest.raises(ValueError, match="Invalid URL"):
        scrape_webpage("invalid_url")

def test_scrape_webpage_request_exception():
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.RequestException("Connection error")
        with pytest.raises(ValueError, match="Error accessing webpage"):
            scrape_webpage("https://example.com")

def test_scrape_webpage_timeout():
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.Timeout("Request timed out")
        with pytest.raises(ValueError, match="Error accessing webpage"):
            scrape_webpage("https://example.com")