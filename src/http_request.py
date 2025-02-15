import requests

def send_get_request(url, headers=None, params=None, timeout=10):
    """
    Send an HTTP GET request to the specified URL.

    Args:
        url (str): The URL to send the GET request to.
        headers (dict, optional): Optional HTTP headers to include in the request. Defaults to None.
        params (dict, optional): Optional query parameters to include in the request. Defaults to None.
        timeout (int, optional): Timeout for the request in seconds. Defaults to 10.

    Returns:
        dict: A dictionary containing the response details:
            - 'status_code': HTTP status code of the response
            - 'content': Response content as text
            - 'headers': Response headers
            - 'json': JSON response (if applicable, else None)

    Raises:
        requests.RequestException: For any network-related errors
    """
    try:
        # Send the GET request
        response = requests.get(
            url, 
            headers=headers, 
            params=params, 
            timeout=timeout
        )
        
        # Raise an exception for HTTP error responses
        response.raise_for_status()
        
        # Attempt to parse JSON, return None if not possible
        try:
            json_response = response.json()
        except ValueError:
            json_response = None
        
        # Return a comprehensive response dictionary
        return {
            'status_code': response.status_code,
            'content': response.text,
            'headers': dict(response.headers),
            'json': json_response
        }
    
    except requests.RequestException as e:
        # Reraise any request-related exceptions
        raise