import socket

def perform_dns_lookup(hostname):
    """
    Perform a DNS lookup to resolve a hostname to its IP address.
    
    Args:
        hostname (str): The domain name to look up.
    
    Returns:
        str: The IP address of the hostname.
    
    Raises:
        ValueError: If the hostname is empty or None.
        socket.gaierror: If the hostname cannot be resolved.
    """
    # Check for invalid input
    if not hostname:
        raise ValueError("Hostname cannot be empty")
    
    try:
        # Perform DNS lookup
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        # If lookup fails, raise an error with a descriptive message
        raise socket.gaierror(f"Could not resolve hostname: {hostname}")