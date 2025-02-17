import os
import requests

def download_file_from_url(url, destination_path=None):
    """
    Download a file from a given URL.
    
    Args:
        url (str): The URL of the file to download
        destination_path (str, optional): Path where the file will be saved. 
                                          If not provided, uses the filename from the URL.
    
    Returns:
        str: The path of the downloaded file
    
    Raises:
        ValueError: If URL is invalid or empty
        requests.exceptions.RequestException: If there's an error downloading the file
    """
    # Validate URL
    if not url or not url.startswith(('http://', 'https://')):
        raise ValueError("Invalid URL. Must start with http:// or https://")
    
    try:
        # Send a GET request to download the file
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Determine destination path
        if destination_path is None:
            # Extract filename from URL if not provided
            filename = url.split('/')[-1]
            destination_path = os.path.join('downloads', filename)
        
        # Create downloads directory if it doesn't exist
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        
        # Write the content to the file
        with open(destination_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        return destination_path
    
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error downloading file: {e}")