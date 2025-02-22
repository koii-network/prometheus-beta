import socket
import ipaddress

def perform_dns_lookup(hostname):
    """
    Perform a DNS lookup to resolve a hostname to its IP address.
    
    Args:
        hostname (str): The domain name to resolve.
    
    Returns:
        dict: A dictionary containing the resolved IP addresses.
    
    Raises:
        ValueError: If the hostname is invalid or empty.
        socket.gaierror: If the hostname cannot be resolved.
    """
    # Validate input
    if not hostname or not isinstance(hostname, str):
        raise ValueError("Hostname must be a non-empty string")
    
    try:
        # Perform DNS lookup
        addrinfo = socket.getaddrinfo(hostname, None)
        
        # Extract unique IP addresses
        ipv4_addresses = set()
        ipv6_addresses = set()
        
        for info in addrinfo:
            ip = info[4][0]
            try:
                addr = ipaddress.ip_address(ip)
                if addr.version == 4:
                    ipv4_addresses.add(ip)
                elif addr.version == 6:
                    ipv6_addresses.add(ip)
            except ValueError:
                # Skip invalid IP addresses
                continue
        
        return {
            "hostname": hostname,
            "ipv4_addresses": list(ipv4_addresses),
            "ipv6_addresses": list(ipv6_addresses)
        }
    
    except socket.gaierror as e:
        raise socket.gaierror(f"Unable to resolve hostname: {hostname}. Error: {str(e)}")