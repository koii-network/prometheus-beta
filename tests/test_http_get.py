import pytest
import requests
from src.http_get import send_http_get_request

def test_successful_get_request(requests_mock):
    # Mock a successful request
    test_url = 'https://example.com'
    test_content = 'Hello, World!'
    requests_mock.get(test_url, text=test_content, status_code=200)
    
    # Call the function
    result = send_http_get_request(test_url)
    
    # Verify the result
    assert result['status_code'] == 200
    assert result['content'] == test_content

def test_get_request_with_headers(requests_mock):
    # Mock a request with headers
    test_url = 'https://example.com'
    test_headers = {'Authorization': 'Bearer token123'}
    requests_mock.get(test_url, text='Success', status_code=200)
    
    # Call the function
    result = send_http_get_request(test_url, headers=test_headers)
    
    # Verify the result
    assert result['status_code'] == 200

def test_get_request_with_params(requests_mock):
    # Mock a request with query parameters
    test_url = 'https://example.com'
    test_params = {'key1': 'value1', 'key2': 'value2'}
    requests_mock.get(test_url, text='Success', status_code=200)
    
    # Call the function
    result = send_http_get_request(test_url, params=test_params)
    
    # Verify the result
    assert result['status_code'] == 200

def test_empty_url_raises_error():
    # Test that empty URL raises ValueError
    with pytest.raises(ValueError, match="URL cannot be empty"):
        send_http_get_request('')

def test_request_exception(requests_mock):
    # Simulate a request exception
    test_url = 'https://example.com'
    requests_mock.get(test_url, exc=requests.exceptions.ConnectTimeout)
    
    # Verify that a RuntimeError is raised
    with pytest.raises(RuntimeError, match="HTTP GET request failed"):
        send_http_get_request(test_url)

def test_bad_status_code(requests_mock):
    # Simulate a bad status code
    test_url = 'https://example.com'
    requests_mock.get(test_url, status_code=404)
    
    # Verify that an HTTPError is raised
    with pytest.raises(requests.exceptions.HTTPError):
        send_http_get_request(test_url)