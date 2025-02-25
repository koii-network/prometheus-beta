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
            raise requests.HTTPError()

def test_scrape_webpage_basic():
    mock_html = """
    <html>
        <body>
            <div>First Element</div>
            <div>Second Element</div>
        </body>
    </html>
    """
    
    with patch('requests.get') as mock_get:
        mock_get.return_value = MockResponse(mock_html)
        
        results = scrape_webpage('http://example.com', 'div')
        
        assert len(results) == 2
        assert results == ['First Element', 'Second Element']

def test_scrape_webpage_with_class():
    mock_html = """
    <html>
        <body>
            <div class="test-class">Specific Element</div>
            <div>Other Element</div>
        </body>
    </html>
    """
    
    with patch('requests.get') as mock_get:
        mock_get.return_value = MockResponse(mock_html)
        
        results = scrape_webpage('http://example.com', 'div', 'test-class')
        
        assert len(results) == 1
        assert results == ['Specific Element']

def test_scrape_webpage_no_elements():
    mock_html = "<html><body></body></html>"
    
    with patch('requests.get') as mock_get:
        mock_get.return_value = MockResponse(mock_html)
        
        with pytest.raises(RuntimeError, match="No div elements found on the page"):
            scrape_webpage('http://example.com', 'div')

def test_scrape_webpage_request_error():
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.RequestException("Connection error")
        
        with pytest.raises(ValueError, match="Error accessing URL"):
            scrape_webpage('http://invalid-url', 'div')