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
        requests.RequestException: If there's an error downloading the file.
    """
    # Validate URL
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL provided")

    try:
        # Send a GET request to download the file
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Determine the destination file path
        if destination is None:
            # Extract filename from URL or Content-Disposition header
            filename = response.headers.get('Content-Disposition')
            if filename:
                filename = filename.split('filename=')[-1].strip('"')
            else:
                filename = os.path.basename(url.split('?')[0])
            
            # Use current directory if no path is specified
            destination = os.path.join(os.getcwd(), filename)

        # Ensure the directory exists
        os.makedirs(os.path.dirname(destination), exist_ok=True)

        # Write the content to the file
        with open(destination, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        return destination

    except requests.RequestException as e:
        raise RuntimeError(f"Error downloading file from {url}: {str(e)}")