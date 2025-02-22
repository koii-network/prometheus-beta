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
        username (str): The username for FTP authentication
        password (str): The password for FTP authentication
        port (int, optional): The port number. Defaults to 21.
        timeout (int, optional): Connection timeout in seconds. Defaults to 30.
    
    Returns:
        Optional[ftplib.FTP]: An established FTP connection or None if connection fails
    
    Raises:
        ValueError: If any required connection parameters are missing
        ftplib.all_errors: For various FTP-related connection errors
    """
    # Validate input parameters
    if not all([host, username, password]):
        raise ValueError("Host, username, and password are required")
    
    try:
        # Establish the FTP connection
        ftp = ftplib.FTP(timeout=timeout)
        ftp.connect(host=host, port=port)
        ftp.login(user=username, passwd=password)
        
        return ftp
    
    except (ftplib.all_errors, ConnectionError) as e:
        # Log the error or handle it as needed
        print(f"FTP Connection Error: {e}")
        return None