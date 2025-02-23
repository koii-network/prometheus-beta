import socket
import ipaddress

def perform_dns_lookup(hostname):
    """
    Perform a DNS lookup to resolve a hostname to its IP address.

    Args:
        hostname (str): The domain name to resolve.

    Returns:
        str: The resolved IP address.

    Raises:
        ValueError: If the hostname is invalid or empty.
        socket.gaierror: If the hostname cannot be resolved.
    """
    # Validate input
    if not hostname or not isinstance(hostname, str):
        raise ValueError("Hostname must be a non-empty string")

    # Remove any whitespace
    hostname = hostname.strip()

    try:
        # Perform DNS lookup
        ip_address = socket.gethostbyname(hostname)

        # Validate the returned IP address
        ipaddress.ip_address(ip_address)

        return ip_address

    except socket.gaierror:
        raise socket.gaierror(f"Unable to resolve hostname: {hostname}")
    except ValueError:
        raise ValueError(f"Invalid IP address returned for hostname: {hostname}")