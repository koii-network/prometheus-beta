import requests

def get_public_ip():
    """
    Retrieve the public IP address of the system.
    
    Returns:
        str: The public IP address of the system.
    
    Raises:
        ConnectionError: If unable to connect to IP lookup service.
        ValueError: If unable to parse the IP address.
    """
    try:
        # Use multiple IP lookup services for reliability
        ip_services = [
            'https://api.ipify.org',
            'https://ipinfo.io/ip',
            'https://checkip.amazonaws.com'
        ]
        
        for service in ip_services:
            try:
                response = requests.get(service, timeout=5)
                response.raise_for_status()
                
                # Strip any whitespace or newline characters
                ip_address = response.text.strip()
                
                # Basic IP address validation
                parts = ip_address.split('.')
                if len(parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts):
                    return ip_address
            except (requests.RequestException, ValueError):
                # If one service fails, try the next
                continue
        
        # If all services fail
        raise ConnectionError("Unable to retrieve public IP address")
    
    except Exception as e:
        raise ConnectionError(f"Error retrieving public IP: {str(e)}")