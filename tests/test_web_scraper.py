import pytest
import requests
from unittest.mock import patch, Mock
from src.web_scraper import scrape_webpage

def test_scrape_webpage_basic():
    # Mock the requests.get method to return a controlled HTML response
    mock_html = '''
    <html>
        <body>
            <p>First paragraph</p>
            <p>Second paragraph</p>
            <div>Not a paragraph</div>
        </body>
    </html>
    '''
    
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.text = mock_html
        mock_response.raise_for_status = lambda: None
        mock_get.return_value = mock_response
        
        # Test the scraper
        result = scrape_webpage('http://example.com')
        
        assert len(result) == 2
        assert 'First paragraph' in result
        assert 'Second paragraph' in result

def test_scrape_webpage_with_class():
    # Mock the requests.get method to return a HTML with class-specific elements
    mock_html = '''
    <html>
        <body>
            <p class="content">First content paragraph</p>
            <p>General paragraph</p>
            <p class="content">Second content paragraph</p>
        </body>
    </html>
    '''
    
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.text = mock_html
        mock_response.raise_for_status = lambda: None
        mock_get.return_value = mock_response
        
        # Test scraping with a specific class
        result = scrape_webpage('http://example.com', tag='p', class_name='content')
        
        assert len(result) == 2
        assert 'First content paragraph' in result
        assert 'Second content paragraph' in result
        assert 'General paragraph' not in result

def test_scrape_webpage_connection_error():
    # Test handling of connection errors
    with patch('requests.get') as mock_get:
        mock_get.side_effect = requests.ConnectionError("Network error")
        
        with pytest.raises(ValueError, match="Error fetching webpage"):
            scrape_webpage('http://nonexistent.com')

def test_scrape_webpage_bad_status():
    # Test handling of bad HTTP status
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.HTTPError("404 Not Found")
        mock_get.return_value = mock_response
        
        with pytest.raises(ValueError, match="Error fetching webpage"):
            scrape_webpage('http://example.com')

def test_scrape_webpage_empty_result():
    # Test scenario with no matching elements
    mock_html = '''
    <html>
        <body>
            <div>No paragraphs here</div>
        </body>
    </html>
    '''
    
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.text = mock_html
        mock_response.raise_for_status = lambda: None
        mock_get.return_value = mock_response
        
        result = scrape_webpage('http://example.com')
        
        assert len(result) == 0