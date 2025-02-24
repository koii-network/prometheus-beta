import socket
import ipaddress

def perform_dns_lookup(hostname):
    """
    Perform a DNS lookup to resolve a hostname to its IP address.

    Args:
        hostname (str): The domain name to look up.

    Returns:
        str: The resolved IP address.

    Raises:
        ValueError: If the input is not a valid hostname.
        socket.gaierror: If the hostname cannot be resolved.
    """
    # Validate input
    if not isinstance(hostname, str):
        raise ValueError("Hostname must be a string")
    
    # Remove any whitespace and validate hostname format
    hostname = hostname.strip()
    if not hostname:
        raise ValueError("Hostname cannot be empty")
    
    try:
        # Perform DNS lookup
        ip_address = socket.gethostbyname(hostname)
        
        # Validate the returned IP address
        ipaddress.ip_address(ip_address)
        
        return ip_address
    
    except socket.gaierror:
        raise socket.gaierror(f"Could not resolve hostname: {hostname}")
    except ValueError as e:
        raise ValueError(f"Invalid IP address returned for {hostname}: {str(e)}")