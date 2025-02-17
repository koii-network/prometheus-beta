import requests

def send_http_post_request(url, data=None, headers=None, timeout=10):
    """
    Send an HTTP POST request to the specified URL.
    
    Args:
        url (str): The URL to send the POST request to.
        data (dict, optional): The payload to send with the request. Defaults to None.
        headers (dict, optional): Custom headers to send with the request. Defaults to None.
        timeout (int, optional): Request timeout in seconds. Defaults to 10.
    
    Returns:
        dict: A dictionary containing the response details:
            - 'status_code': HTTP status code of the response
            - 'json': JSON response body (if applicable)
            - 'text': Raw text response
            - 'headers': Response headers
    
    Raises:
        requests.RequestException: For any network-related errors
    """
    try:
        # Use an empty dict if no data provided
        request_data = data or {}
        
        # Use an empty dict if no headers provided
        request_headers = headers or {}
        
        # Send POST request
        response = requests.post(
            url, 
            json=request_data, 
            headers=request_headers, 
            timeout=timeout
        )
        
        # Attempt to parse JSON, fallback to text if not possible
        try:
            response_json = response.json()
        except ValueError:
            response_json = None
        
        return {
            'status_code': response.status_code,
            'json': response_json,
            'text': response.text,
            'headers': dict(response.headers)
        }
    
    except requests.RequestException as e:
        # Re-raise network-related exceptions
        raise