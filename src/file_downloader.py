import requests
import os

def download_file_from_url(url, destination_path=None):
    """
    Download a file from a given URL.
    
    Args:
        url (str): The URL of the file to download
        destination_path (str, optional): Path where the file should be saved. 
                                          If not provided, uses the filename from the URL.
    
    Returns:
        str: The path where the file was saved
    
    Raises:
        ValueError: If URL is invalid or empty
        requests.RequestException: For network-related errors
        IOError: For file writing errors
    """
    # Validate URL
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL provided")
    
    # Send GET request to download the file
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes
    except requests.RequestException as e:
        raise requests.RequestException(f"Error downloading file from {url}: {str(e)}")
    
    # Determine destination path
    if destination_path is None:
        # Extract filename from URL or Content-Disposition header
        filename = response.headers.get('Content-Disposition', '').split('filename=')[-1] or url.split('/')[-1]
        destination_path = os.path.join('downloads', filename)
    
    # Ensure download directory exists
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    
    # Write file
    try:
        with open(destination_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    except IOError as e:
        raise IOError(f"Error saving file to {destination_path}: {str(e)}")
    
    return destination_path