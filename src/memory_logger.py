import psutil
import logging
import os

def log_memory_usage(logger=None):
    """
    Log current memory usage statistics.
    
    :param logger: Optional custom logger. If None, creates a default logger.
    :return: Dictionary of memory usage statistics
    """
    # Create a default logger if none is provided
    if logger is None:
        logging.basicConfig(level=logging.INFO, 
                            format='%(asctime)s - %(levelname)s - %(message)s')
        logger = logging.getLogger(__name__)
    
    # Get memory information
    memory = psutil.virtual_memory()
    
    # Prepare memory statistics
    memory_stats = {
        'total': memory.total / (1024 * 1024),  # Total memory in MB
        'available': memory.available / (1024 * 1024),  # Available memory in MB
        'used': memory.used / (1024 * 1024),  # Used memory in MB
        'percent': memory.percent  # Percentage of memory used
    }
    
    # Log the memory statistics
    logger.info(f"Memory Usage Statistics:")
    logger.info(f"Total Memory: {memory_stats['total']:.2f} MB")
    logger.info(f"Available Memory: {memory_stats['available']:.2f} MB")
    logger.info(f"Used Memory: {memory_stats['used']:.2f} MB")
    logger.info(f"Memory Usage: {memory_stats['percent']}%")
    
    return memory_stats