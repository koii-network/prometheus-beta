import ftplib
import socket

def establish_ftp_connection(host, username, password, port=21, timeout=30):
    """
    Establish a connection to an FTP server.

    Args:
        host (str): The FTP server hostname or IP address
        username (str): Username for FTP authentication
        password (str): Password for FTP authentication
        port (int, optional): FTP server port. Defaults to 21.
        timeout (int, optional): Connection timeout in seconds. Defaults to 30.

    Returns:
        ftplib.FTP: An authenticated FTP connection object

    Raises:
        ValueError: If any required connection parameters are missing
        ConnectionError: If unable to establish FTP connection
    """
    # Validate input parameters
    if not all([host, username, password]):
        raise ValueError("Host, username, and password are required")

    try:
        # Attempt to establish FTP connection
        ftp = ftplib.FTP(timeout=timeout)
        ftp.connect(host=host, port=port)
        ftp.login(user=username, passwd=password)
        return ftp

    except socket.gaierror:
        raise ConnectionError(f"Could not resolve hostname: {host}")
    except ftplib.all_errors as e:
        raise ConnectionError(f"FTP connection failed: {str(e)}")