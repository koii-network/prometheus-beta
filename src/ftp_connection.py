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
    
    try:
        # Attempt to establish FTP connection
        ftp = ftplib.FTP(timeout=timeout)
        ftp.connect(host=host, port=port)
        
        # Authenticate if credentials are provided
        if username is not None and password is not None:
            ftp.login(user=username, passwd=password)
        elif username is not None or password is not None:
            raise ValueError("Both username and password must be provided for authentication")
        
        return ftp
    
    except socket.gaierror:
        raise ConnectionError(f"Could not resolve host: {host}")
    except socket.timeout:
        raise ConnectionError(f"Connection to {host} timed out")
    except ftplib.all_errors as e:
        raise ConnectionError(f"FTP connection error: {str(e)}")