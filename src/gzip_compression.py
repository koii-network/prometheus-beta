import gzip
import io
import typing

def gzip_compress(data: typing.Union[str, bytes], compression_level: int = 9) -> bytes:
    """
    Compress input data using Gzip compression.

    Args:
        data (str or bytes): The input data to compress.
        compression_level (int, optional): Compression level from 0-9. 
                                           Defaults to 9 (highest compression).

    Returns:
        bytes: Compressed data in Gzip format.

    Raises:
        ValueError: If compression level is not between 0 and 9.
        TypeError: If input data is not str or bytes.
    """
    # Validate compression level
    if not 0 <= compression_level <= 9:
        raise ValueError("Compression level must be between 0 and 9")

    # Validate input data type
    if not isinstance(data, (str, bytes)):
        raise TypeError("Input must be str or bytes")

    # Convert string to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')

    # Compress data
    try:
        with io.BytesIO() as bio:
            with gzip.GzipFile(fileobj=bio, mode='wb', compresslevel=compression_level) as gzf:
                gzf.write(data)
            return bio.getvalue()
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")