import os
import tarfile

def create_tar_archive(source_dir, archive_path, compress_type='gz'):
    """
    Create a tar archive of a given directory.
    
    Args:
        source_dir (str): Path to the directory to be archived
        archive_path (str): Path where the tar archive will be created
        compress_type (str, optional): Compression type. 
                                      Defaults to 'gz' (gzip compression).
                                      Other options: 'bz2', 'xz', None for no compression
    
    Raises:
        ValueError: If source directory does not exist
        OSError: If there are issues creating the archive
    
    Returns:
        str: Path to the created tar archive
    """
    # Validate source directory exists
    source_dir = os.path.abspath(source_dir)
    if not os.path.isdir(source_dir):
        raise ValueError(f"Source directory does not exist: {source_dir}")
    
    # Determine compression mode
    compression_modes = {
        'gz': 'w:gz',
        'bz2': 'w:bz2',
        'xz': 'w:xz',
        None: 'w'
    }
    
    if compress_type not in compression_modes:
        raise ValueError(f"Unsupported compression type: {compress_type}")
    
    # Ensure the directory for the archive exists
    os.makedirs(os.path.dirname(os.path.abspath(archive_path)), exist_ok=True)
    
    # Create tar archive
    try:
        with tarfile.open(archive_path, compression_modes[compress_type]) as tar:
            tar.add(source_dir, arcname=os.path.basename(source_dir))
    except Exception as e:
        raise OSError(f"Error creating tar archive: {e}")
    
    return archive_path