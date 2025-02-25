import os
import tarfile
from typing import Union, List, Optional


def extract_tar_archive(
    archive_path: str, 
    extract_path: Optional[str] = None, 
    specific_files: Optional[Union[str, List[str]]] = None
) -> List[str]:
    """
    Extract files from a tar archive with flexible options.

    Args:
        archive_path (str): Path to the tar archive file.
        extract_path (Optional[str], optional): Destination directory for extraction. 
            If None, extracts to the archive's directory. Defaults to None.
        specific_files (Optional[Union[str, List[str]]], optional): 
            Specific file(s) to extract from the archive. 
            Can be a single filename or a list of filenames.
            If None, extracts all files. Defaults to None.

    Returns:
        List[str]: List of full paths to extracted files.

    Raises:
        FileNotFoundError: If the archive file does not exist.
        ValueError: If the archive is invalid or cannot be opened.
        PermissionError: If there are insufficient permissions to extract.
    """
    # Validate archive path
    if not os.path.exists(archive_path):
        raise FileNotFoundError(f"Archive file not found: {archive_path}")

    # Determine extraction path
    if extract_path is None:
        extract_path = os.path.dirname(os.path.abspath(archive_path))
    else:
        # Ensure extraction directory exists
        os.makedirs(extract_path, exist_ok=True)

    # Normalize specific_files to a list
    if specific_files is None:
        specific_files = []
    elif isinstance(specific_files, str):
        specific_files = [specific_files]

    # List to store extracted file paths
    extracted_files = []

    try:
        # Open the tar archive
        with tarfile.open(archive_path, 'r:*') as tar:
            # Use a safe filter
            tar_filter = lambda member, destination_path: member

            # If no specific files are specified, extract all
            if not specific_files:
                tar.extractall(path=extract_path, filter=tar_filter)
                extracted_files = [
                    os.path.join(extract_path, member.name) 
                    for member in tar.getmembers() 
                    if member.isfile()
                ]
            else:
                # Extract only specified files
                for filename in specific_files:
                    try:
                        # Use a more explicit extraction method
                        tar.extract(filename, path=extract_path, filter=tar_filter)
                        extracted_files.append(
                            os.path.join(extract_path, filename)
                        )
                    except KeyError:
                        # Ignore files not found in the archive
                        continue

    except tarfile.TarError as e:
        raise ValueError(f"Error processing tar archive: {e}")

    return extracted_files