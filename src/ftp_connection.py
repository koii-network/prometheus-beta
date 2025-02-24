import ftplib
from typing import Optional, Tuple

def establish_ftp_connection(
    host: str, 
    username: str, 
    password: str, 
    port: int = 21, 
    timeout: int = 30
) -> Tuple[Optional[ftplib.FTP], Optional[str]]:
    """
    Establish a connection to an FTP server.

    Args:
        host (str): The FTP server hostname or IP address
        username (str): Username for FTP authentication
        password (str): Password for FTP authentication
        port (int, optional): FTP server port. Defaults to 21.
        timeout (int, optional): Connection timeout in seconds. Defaults to 30.

    Returns:
        Tuple[Optional[ftplib.FTP], Optional[str]]: 
        - A tuple containing the FTP connection object if successful, 
          or None if connection fails
        - An error message if connection fails, or None if successful
    """
    try:
        # Validate input parameters
        if not host or not username or not password:
            return None, "Missing required connection parameters"

        # Establish FTP connection with timeout
        ftp = ftplib.FTP(timeout=timeout)
        ftp.connect(host=host, port=port)
        
        # Attempt to login
        ftp.login(user=username, passwd=password)
        
        return ftp, None
    
    except ftplib.all_errors as e:
        # Catch and handle various FTP-related exceptions
        return None, f"FTP Connection Error: {str(e)}"
    except Exception as e:
        # Catch any unexpected errors
        return None, f"Unexpected Error: {str(e)}"