import socket

def perform_dns_lookup(hostname):
    """
    Perform a DNS lookup to resolve a hostname to its IP address.
    
    Args:
        hostname (str): The domain name to look up
    
    Returns:
        str: The resolved IP address
    
    Raises:
        ValueError: If hostname is empty or None
        socket.gaierror: If the hostname cannot be resolved
    """
    # Validate input
    if not hostname:
        raise ValueError("Hostname cannot be empty")
    
    try:
        # Perform DNS lookup
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        # Re-raise with a more informative message
        raise socket.gaierror(f"Unable to resolve hostname: {hostname}")