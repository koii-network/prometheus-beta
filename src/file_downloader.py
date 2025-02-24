import requests
import os

def download_file(url, destination=None):
    """
    Download a file from a given URL.

    Args:
        url (str): The URL of the file to download.
        destination (str, optional): The path where the file should be saved. 
                                     If not provided, uses the filename from the URL.

    Returns:
        str: The path to the downloaded file.

    Raises:
        ValueError: If the URL is invalid or empty.
        requests.HTTPError: If there's an error downloading the file.
        IOError: If there's an error saving the file.
    """
    # Validate URL
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL: URL must be a non-empty string")

    # Send a GET request to download the file
    response = requests.get(url, stream=True)
    
    # Explicitly raise HTTPError for bad status codes
    response.raise_for_status()

    # Determine the destination file path
    if destination is None:
        # Extract filename from URL or Content-Disposition header
        filename = response.headers.get('Content-Disposition')
        if filename:
            filename = filename.split('filename=')[-1].strip('"\'')
        else:
            filename = url.split('/')[-1]
        
        # Use downloads directory if no destination specified
        destination = os.path.join('downloads', filename)

    # Ensure the directory exists
    os.makedirs(os.path.dirname(destination), exist_ok=True)

    # Write the file
    with open(destination, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    return destination