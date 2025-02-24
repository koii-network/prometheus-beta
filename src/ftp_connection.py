import ftplib
from typing import Optional, Tuple

def establish_ftp_connection(
    host: str, 
    username: str, 
    password: str, 
    port: int = 21
) -> Tuple[Optional[ftplib.FTP], Optional[str]]:
    """
    Establish a connection to an FTP server.

    Args:
        host (str): Hostname or IP address of the FTP server
        username (str): Username for FTP authentication
        password (str): Password for FTP authentication
        port (int, optional): Port number. Defaults to 21.

    Returns:
        Tuple containing:
        - FTP connection object if successful, None otherwise
        - Error message if connection fails, None if successful
    """
    try:
        # Validate input parameters
        if not host or not username or not password:
            return None, "Missing required connection parameters"

        # Attempt to establish FTP connection
        ftp = ftplib.FTP()
        ftp.connect(host=host, port=port)
        ftp.login(user=username, passwd=password)
        
        return ftp, None
    
    except ftplib.all_errors as e:
        # Catch and handle various FTP-related errors
        return None, f"FTP Connection Error: {str(e)}"
    except Exception as e:
        # Catch any unexpected errors
        return None, f"Unexpected Error: {str(e)}"