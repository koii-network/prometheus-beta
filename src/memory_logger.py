import psutil
import logging
import os

def log_memory_usage(logger=None):
    """
    Log memory usage statistics of the current process.
    
    Args:
        logger (logging.Logger, optional): Logger to use. If not provided, 
                                           creates a default logger.
    
    Returns:
        dict: A dictionary containing memory usage statistics
    """
    # If no logger is provided, create a default one
    if logger is None:
        logging.basicConfig(level=logging.INFO, 
                            format='%(asctime)s - %(levelname)s - %(message)s')
        logger = logging.getLogger(__name__)
    
    # Get memory information
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    
    # Memory statistics
    memory_stats = {
        'rss': memory_info.rss / (1024 * 1024),  # Resident Set Size in MB
        'vms': memory_info.vms / (1024 * 1024),  # Virtual Memory Size in MB
        'percent': psutil.virtual_memory().percent
    }
    
    # Log the memory usage
    logger.info(f"Memory Usage Statistics:")
    logger.info(f"Resident Set Size (RSS): {memory_stats['rss']:.2f} MB")
    logger.info(f"Virtual Memory Size (VMS): {memory_stats['vms']:.2f} MB")
    logger.info(f"Total System Memory Usage: {memory_stats['percent']}%")
    
    return memory_stats