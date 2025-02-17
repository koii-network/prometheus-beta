import requests

def get_public_ip():
    """
    Retrieve the public IP address of the system.
    
    Returns:
        str: The public IP address of the system.
    
    Raises:
        ConnectionError: If unable to retrieve the public IP address.
    """
    try:
        # Use a reliable public IP lookup service
        response = requests.get('https://api.ipify.org', timeout=10)
        response.raise_for_status()  # Raise an exception for bad responses
        return response.text.strip()
    except requests.RequestException as e:
        raise ConnectionError(f"Unable to retrieve public IP address: {e}")