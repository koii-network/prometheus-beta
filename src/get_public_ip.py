import requests

def get_public_ip():
    """
    Retrieve the public IP address of the system.
    
    Returns:
        str: The public IP address of the system.
    
    Raises:
        ConnectionError: If unable to connect to IP lookup service.
        ValueError: If the response cannot be parsed.
    """
    try:
        # Use multiple IP lookup services for redundancy
        ip_services = [
            'https://api.ipify.org',
            'https://checkip.amazonaws.com',
            'https://ipinfo.io/ip'
        ]
        
        for service in ip_services:
            try:
                response = requests.get(service, timeout=5)
                response.raise_for_status()  # Raise an error for bad responses
                
                # Strip any whitespace or newline characters
                ip_address = response.text.strip()
                
                # Basic validation of IP address format
                if not _validate_ip_address(ip_address):
                    continue
                
                return ip_address
            except (requests.RequestException, ValueError):
                continue
        
        # If all services fail
        raise ConnectionError("Unable to retrieve public IP address")
    except Exception:
        raise ConnectionError("Unable to retrieve public IP address")

def _validate_ip_address(ip):
    """
    Validate the format of an IP address.
    
    Args:
        ip (str): IP address to validate
    
    Returns:
        bool: True if valid IP address, False otherwise
    """
    try:
        # Basic IPv4 validation
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        
        return all(0 <= int(part) <= 255 for part in parts)
    except (ValueError, TypeError):
        return False