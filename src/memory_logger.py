import psutil
import logging
import os

def log_memory_usage(logger=None):
    """
    Log memory usage statistics of the current process.

    Args:
        logger (logging.Logger, optional): Custom logger. 
                If not provided, creates a default logger.

    Returns:
        dict: A dictionary containing memory usage statistics
    """
    # Create a default logger if not provided
    if logger is None:
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        
        # Create console handler if no handlers exist
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)

    # Get memory info for the current process
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()

    # Memory usage statistics
    stats = {
        'rss': mem_info.rss,  # Resident Set Size (non-swapped physical memory)
        'vms': mem_info.vms,  # Virtual Memory Size
        'uss': getattr(mem_info, 'uss', None),  # Unique Set Size (if available)
        'pss': getattr(mem_info, 'pss', None)   # Proportional Set Size (if available)
    }

    # Log the memory usage
    logger.info(f"Memory Usage Statistics (bytes):")
    for key, value in stats.items():
        if value is not None:
            logger.info(f"{key.upper()}: {value:,}")

    return stats