import ftplib
from typing import Optional

def establish_ftp_connection(
    host: str, 
    username: str, 
    password: str, 
    port: int = 21, 
    timeout: int = 30
) -> Optional[ftplib.FTP]:
    """
    Establish an FTP connection with the given parameters.
    
    Args:
        host (str): The FTP server hostname or IP address
        username (str): Username for FTP authentication
        password (str): Password for FTP authentication
        port (int, optional): FTP server port. Defaults to 21.
        timeout (int, optional): Connection timeout in seconds. Defaults to 30.
    
    Returns:
        Optional[ftplib.FTP]: An active FTP connection or None if connection fails
    
    Raises:
        ValueError: If any of the required parameters are empty or invalid
    """
    # Validate input parameters
    if not host or not username or not password:
        raise ValueError("Host, username, and password must be provided")
    
    try:
        # Establish FTP connection
        ftp = ftplib.FTP(timeout=timeout)
        ftp.connect(host=host, port=port)
        ftp.login(user=username, passwd=password)
        
        return ftp
    
    except (ftplib.all_errors, ConnectionError) as e:
        # Log the error or handle connection failures
        print(f"FTP Connection Error: {e}")
        return None