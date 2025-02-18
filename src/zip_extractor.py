import os
import zipfile

def extract_zip_files(zip_path, extract_path=None):
    """
    Extract all files from a zip archive.

    Args:
        zip_path (str): Path to the zip file to extract.
        extract_path (str, optional): Destination path for extracted files. 
                                      Defaults to the same directory as the zip file.

    Returns:
        list: A list of paths to the extracted files.

    Raises:
        FileNotFoundError: If the zip file does not exist.
        zipfile.BadZipFile: If the zip file is corrupted.
    """
    # Validate zip file exists
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"Zip file not found: {zip_path}")

    # If no extract path provided, use the zip file's directory
    if extract_path is None:
        extract_path = os.path.dirname(os.path.abspath(zip_path))

    # Ensure extract path exists
    os.makedirs(extract_path, exist_ok=True)

    # List to store extracted file paths
    extracted_files = []

    # Extract zip contents
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Check for zip file corruption
        try:
            zip_ref.testzip()
        except zipfile.BadZipFile:
            raise zipfile.BadZipFile(f"Corrupted zip file: {zip_path}")

        # Extract all files
        for file in zip_ref.namelist():
            # Avoid directory traversal attacks by using ZipFile.extract
            full_path = zip_ref.extract(file, path=extract_path)
            extracted_files.append(full_path)

    return extracted_files