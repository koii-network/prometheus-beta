import requests

def get_public_ip():
    """
    Retrieve the public IP address of the system.
    
    Returns:
        str: The public IP address as a string.
    
    Raises:
        ConnectionError: If unable to connect to IP lookup service.
        ValueError: If unable to parse the IP address.
    """
    try:
        # Use a reliable IP lookup service
        response = requests.get('https://api.ipify.org', timeout=10)
        response.raise_for_status()  # Raise an exception for bad responses
        
        # Validate the IP address format
        ip_address = response.text.strip()
        
        # Basic validation of IP address format
        parts = ip_address.split('.')
        if len(parts) != 4:
            raise ValueError("Invalid IP address format")
        
        for part in parts:
            if not part.isdigit() or int(part) < 0 or int(part) > 255:
                raise ValueError("Invalid IP address format")
        
        return ip_address
    
    except requests.RequestException as e:
        raise ConnectionError(f"Failed to retrieve public IP: {str(e)}")