import pytest
import requests
from unittest.mock import patch, MagicMock
from src.web_scraper import scrape_webpage

# Mock webpage HTML for testing
MOCK_HTML = """
<!DOCTYPE html>
<html>
    <body>
        <h1 class="title">Test Title</h1>
        <div class="content">First Content</div>
        <div class="content">Second Content</div>
        <span class="author">John Doe</span>
    </body>
</html>
"""

def test_successful_scraping():
    """Test successful web scraping with multiple selectors"""
    with patch('requests.get') as mock_get:
        # Setup mock response
        mock_response = MagicMock()
        mock_response.text = MOCK_HTML
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        # Define selectors
        selectors = {
            'title': '.title',
            'contents': '.content',
            'author': '.author'
        }

        # Call scrape function
        result = scrape_webpage('http://example.com', selectors)

        # Assertions
        assert result is not None
        assert result['title'] == ['Test Title']
        assert result['contents'] == ['First Content', 'Second Content']
        assert result['author'] == ['John Doe']

def test_invalid_url():
    """Test handling of invalid URLs"""
    with pytest.raises(ValueError):
        scrape_webpage('', {})
    
    with pytest.raises(ValueError):
        scrape_webpage(None, {})

def test_no_selectors():
    """Test handling of empty selectors"""
    with pytest.raises(ValueError):
        scrape_webpage('http://example.com', {})

def test_network_error():
    """Test handling of network-related errors"""
    with patch('requests.get') as mock_get:
        # Simulate network error
        mock_get.side_effect = requests.RequestException("Network Error")

        result = scrape_webpage('http://example.com', {'test': '.selector'})
        assert result is None

def test_timeout_error():
    """Test handling of timeout errors"""
    with patch('requests.get') as mock_get:
        # Simulate timeout
        mock_get.side_effect = requests.Timeout("Request timed out")

        result = scrape_webpage('http://example.com', {'test': '.selector'})
        assert result is None