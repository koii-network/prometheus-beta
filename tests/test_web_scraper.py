import pytest
import requests_mock
from src.web_scraper import scrape_webpage

def test_scrape_webpage_full_page():
    # Mock URL and response
    mock_url = 'https://example.com'
    mock_html = '<html><body><p>Hello</p><div>World</div><span>Test</span></body></html>'
    
    with requests_mock.Mocker() as m:
        m.get(mock_url, text=mock_html)
        
        # Scrape without selector
        result = scrape_webpage(mock_url)
        
        assert 'url' in result
        assert 'data' in result
        assert result['url'] == mock_url
        assert set(result['data']) == {'Hello', 'World', 'Test'}

def test_scrape_webpage_with_selector():
    # Mock URL and response
    mock_url = 'https://example.com'
    mock_html = '''
    <html>
        <body>
            <div class="content">First Content</div>
            <div class="content">Second Content</div>
            <p>Ignored Text</p>
        </body>
    </html>
    '''
    
    with requests_mock.Mocker() as m:
        m.get(mock_url, text=mock_html)
        
        # Scrape with specific selector
        result = scrape_webpage(mock_url, selector='.content')
        
        assert result['data'] == ['First Content', 'Second Content']

def test_scrape_webpage_invalid_url():
    # Test invalid URL
    with pytest.raises(ValueError, match="Invalid URL"):
        scrape_webpage('invalid_url')

def test_scrape_webpage_connection_error():
    # Test connection error
    with requests_mock.Mocker() as m:
        mock_url = 'https://example.com'
        m.get(mock_url, status_code=404)
        
        with pytest.raises(ConnectionError):
            scrape_webpage(mock_url)