import ftplib
import logging

def establish_ftp_connection(host, username, password, port=21, timeout=30):
    """
    Establish a connection to an FTP server.

    Args:
        host (str): The FTP server hostname or IP address
        username (str): Username for FTP authentication
        password (str): Password for FTP authentication
        port (int, optional): Port number. Defaults to 21.
        timeout (int, optional): Connection timeout in seconds. Defaults to 30.

    Returns:
        ftplib.FTP: An established FTP connection

    Raises:
        ValueError: If any required connection parameters are missing
        ftplib.all_errors: For any FTP-related connection errors
    """
    # Validate input parameters
    if not all([host, username, password]):
        raise ValueError("Host, username, and password are required for FTP connection")

    try:
        # Establish FTP connection with specified parameters
        ftp = ftplib.FTP(timeout=timeout)
        ftp.connect(host=host, port=port)
        ftp.login(user=username, passwd=password)
        
        logging.info(f"Successfully connected to FTP server at {host}:{port}")
        return ftp

    except ftplib.all_errors as e:
        logging.error(f"FTP Connection Error: {str(e)}")
        raise