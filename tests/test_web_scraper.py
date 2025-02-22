import pytest
import requests
from unittest.mock import patch
from src.web_scraper import scrape_webpage

# Sample HTML for mocking
MOCK_HTML = """
<!DOCTYPE html>
<html>
<body>
    <div class="test-class">First Item</div>
    <div class="test-class">Second Item</div>
    <a href="https://example.com/link1">Link 1</a>
    <a href="https://example.com/link2">Link 2</a>
</body>
</html>
"""

class MockResponse:
    def __init__(self, text, status_code=200):
        self.text = text
        self.status_code = status_code
    
    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.HTTPError(f"HTTP Error: {self.status_code}")

def test_scrape_webpage_successful():
    with patch('requests.get') as mock_get:
        mock_get.return_value = MockResponse(MOCK_HTML)
        
        # Test div elements
        results = scrape_webpage('https://example.com', '.test-class')
        assert len(results) == 2
        assert results[0]['text'] == 'First Item'
        assert results[1]['text'] == 'Second Item'
        
        # Test link elements
        link_results = scrape_webpage('https://example.com', 'a')
        assert len(link_results) == 2
        assert link_results[0]['href'] == 'https://example.com/link1'
        assert link_results[1]['href'] == 'https://example.com/link2'

def test_invalid_url():
    with pytest.raises(ValueError, match="Invalid URL"):
        scrape_webpage('invalid_url', 'div')

def test_unreachable_url():
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.RequestException("Connection Error")
        
        with pytest.raises(ValueError, match="Error accessing webpage"):
            scrape_webpage('https://nonexistent.url', 'div')

def test_no_matching_elements():
    with patch('requests.get') as mock_get:
        mock_get.return_value = MockResponse(MOCK_HTML)
        
        with pytest.raises(RuntimeError, match="No elements found"):
            scrape_webpage('https://example.com', '.non-existent-class')