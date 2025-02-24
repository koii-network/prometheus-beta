import ftplib
import socket

def establish_ftp_connection(host, username=None, password=None, port=21, timeout=30):
    """
    Establish an FTP connection with configurable parameters.
    
    Args:
        host (str): The FTP server hostname or IP address
        username (str, optional): Username for authentication. Defaults to None.
        password (str, optional): Password for authentication. Defaults to None.
        port (int, optional): Port number for FTP connection. Defaults to 21.
        timeout (int, optional): Connection timeout in seconds. Defaults to 30.
    
    Returns:
        ftplib.FTP: An established FTP connection object
    
    Raises:
        ValueError: If host is empty or None
        ConnectionError: If connection fails due to network or authentication issues
    """
    # Validate host
    if not host:
        raise ValueError("Host must be a non-empty string")
    
    # Validate credentials
    if (username is not None and password is None) or (username is None and password is not None):
        raise ValueError("Both username and password must be provided for authentication")
    
    try:
        # Attempt to establish FTP connection
        ftp = ftplib.FTP(timeout=timeout)
        try:
            ftp.connect(host=host, port=port)
        except (socket.gaierror, socket.timeout) as e:
            if isinstance(e, socket.gaierror):
                raise ConnectionError(f"Could not resolve host: {host}")
            else:
                raise ConnectionError(f"Connection to {host} timed out")
        
        # Authenticate if credentials are provided
        if username is not None and password is not None:
            try:
                ftp.login(user=username, passwd=password)
            except ftplib.error_perm as e:
                raise ConnectionError(f"FTP connection error: {str(e)}")
        
        return ftp
    
    except ftplib.all_errors as e:
        raise ConnectionError(f"FTP connection error: {str(e)}")