import requests

def get_public_ip():
    """
    Retrieve the public IP address of the system.
    
    Returns:
        str: The public IP address of the system.
    
    Raises:
        requests.RequestException: If there's an error retrieving the IP address.
    """
    try:
        # Use ipify.org API to get public IP
        response = requests.get('https://api.ipify.org', timeout=10)
        response.raise_for_status()  # Raise an exception for bad responses
        return response.text.strip()
    except requests.RequestException as e:
        raise RuntimeError(f"Could not retrieve public IP address: {e}")