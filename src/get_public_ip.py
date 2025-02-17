import requests

def get_public_ip():
    """
    Retrieve the public IP address of the system.
    
    Returns:
        str: The public IP address as a string.
    
    Raises:
        ConnectionError: If unable to connect to IP checking service.
        ValueError: If no valid IP address can be retrieved.
    """
    try:
        # Use a reliable public IP checking service
        response = requests.get('https://api.ipify.org', timeout=10)
        response.raise_for_status()  # Raise an exception for bad responses
        
        ip_address = response.text.strip()
        
        # Validate IP address format (basic check)
        if not ip_address:
            raise ValueError("No IP address received")
        
        return ip_address
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to retrieve public IP: {str(e)}")