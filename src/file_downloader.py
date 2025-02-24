import os
import requests

def download_file(url, save_path=None):
    """
    Download a file from a given URL.

    Args:
        url (str): The URL of the file to download.
        save_path (str, optional): The path where the file will be saved. 
                                   If not provided, uses the filename from the URL.

    Returns:
        str: The full path where the file was saved.

    Raises:
        ValueError: If the URL is invalid or empty.
        requests.RequestException: If there's an error during the download.
        IOError: If there are issues writing the file.
    """
    # Validate URL
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL: URL must be a non-empty string")

    try:
        # Send GET request to download the file
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Determine save path
        if save_path is None:
            # Extract filename from URL or Content-Disposition header
            filename = response.headers.get('Content-Disposition')
            if filename:
                filename = filename.split('filename=')[-1].strip('"\'')
            else:
                filename = url.split('/')[-1]
            
            # Use current directory if no path specified
            save_path = os.path.join(os.getcwd(), filename)

        # Ensure directory exists
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Write file with progress tracking
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)

        return save_path

    except requests.RequestException as e:
        raise requests.RequestException(f"Error downloading file from {url}: {str(e)}")
    except IOError as e:
        raise IOError(f"Error saving file to {save_path}: {str(e)}")