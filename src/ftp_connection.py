import ftplib
import socket

def establish_ftp_connection(host, username, password, port=21, timeout=30):
    """
    Establish a secure FTP connection to a specified host.

    Args:
        host (str): The FTP server hostname or IP address.
        username (str): Username for FTP authentication.
        password (str): Password for FTP authentication.
        port (int, optional): Port number for FTP connection. Defaults to 21.
        timeout (int, optional): Connection timeout in seconds. Defaults to 30.

    Returns:
        ftplib.FTP: An established FTP connection object.

    Raises:
        ValueError: If host, username, or password is empty or invalid.
        ConnectionRefusedError: If the connection to the FTP server fails.
        socket.timeout: If the connection times out.
    """
    # Validate input parameters
    if not host or not username or not password:
        raise ValueError("Host, username, and password must be provided")

    try:
        # Establish FTP connection with timeout
        ftp = ftplib.FTP()
        # Set timeout before connecting
        ftp.connect(host=host, port=port, timeout=timeout)
        
        # Attempt login
        ftp.login(user=username, passwd=password)
        
        return ftp
    except socket.timeout:
        # Explicitly raise socket.timeout as requested in the test
        raise socket.timeout(f"Connection to {host} timed out after {timeout} seconds")
    except (socket.gaierror, socket.error) as e:
        raise ConnectionRefusedError(f"Could not connect to FTP server: {e}")
    except ftplib.error_perm as e:
        raise ConnectionRefusedError(f"Authentication failed: {e}")