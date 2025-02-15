import requests
import os

def download_file(url, destination=None):
    """
    Download a file from a given URL.
    
    Args:
        url (str): The URL of the file to download
        destination (str, optional): Path where the file will be saved. 
                                     If not provided, uses the filename from the URL.
    
    Returns:
        str: Path to the downloaded file
    
    Raises:
        ValueError: If URL is invalid or empty
        requests.RequestException: If there's an error downloading the file
    """
    # Validate URL
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL provided")
    
    try:
        # Send a GET request to download the file
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Determine destination filename
        if destination is None:
            # Extract filename from URL if no destination is specified
            filename = url.split('/')[-1]
            destination = os.path.join('downloads', filename)
        
        # Ensure the downloads directory exists
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        
        # Write the file
        with open(destination, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        return destination
    
    except requests.RequestException as e:
        raise requests.RequestException(f"Error downloading file from {url}: {str(e)}")