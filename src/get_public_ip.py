import requests

def get_public_ip():
    """
    Retrieve the public IP address of the system.
    
    Returns:
        str: Public IP address of the system.
    
    Raises:
        requests.RequestException: If there's an error retrieving the IP address.
    """
    try:
        # Use a reliable IP lookup service
        response = requests.get('https://api.ipify.org', timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.text.strip()
    except requests.RequestException as e:
        raise ValueError(f"Could not retrieve public IP: {e}")