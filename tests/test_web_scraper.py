import pytest
import requests
import requests_mock
from src.web_scraper import scrape_web_page


def test_scrape_web_page_basic():
    """Test basic web page scraping functionality."""
    mock_html = """
    <html>
        <body>
            <div class="test-class">First Element</div>
            <a href="https://example.com">Link Text</a>
        </body>
    </html>
    """
    
    with requests_mock.Mocker() as m:
        m.get('http://test.com', text=mock_html)
        results = scrape_web_page('http://test.com')
        
        assert len(results) == 2
        assert any(item['text'] == 'First Element' for item in results)
        assert any(item['href'] == 'https://example.com' for item in results)


def test_scrape_web_page_with_selector():
    """Test web page scraping with a specific CSS selector."""
    mock_html = """
    <html>
        <body>
            <div class="target">Target Element</div>
            <div class="other">Other Element</div>
        </body>
    </html>
    """
    
    with requests_mock.Mocker() as m:
        m.get('http://test.com', text=mock_html)
        results = scrape_web_page('http://test.com', '.target')
        
        assert len(results) == 1
        assert results[0]['text'] == 'Target Element'


def test_scrape_web_page_invalid_url():
    """Test handling of invalid URL input."""
    with pytest.raises(ValueError):
        scrape_web_page('')


def test_scrape_web_page_connection_error():
    """Test handling of connection errors."""
    with pytest.raises(ConnectionError):
        with requests_mock.Mocker() as m:
            m.get('http://nonexistent.com', exc=requests.exceptions.ConnectTimeout)
            scrape_web_page('http://nonexistent.com')


def test_scrape_web_page_bad_status():
    """Test handling of bad HTTP status codes."""
    with pytest.raises(ConnectionError):
        with requests_mock.Mocker() as m:
            m.get('http://test.com', status_code=404)
            scrape_web_page('http://test.com')