import psutil
import logging
import os

def log_memory_usage(logger=None):
    """
    Logs current memory usage statistics.
    
    Args:
        logger (logging.Logger, optional): Logger to use. If None, creates a default logger.
    
    Returns:
        dict: A dictionary containing memory usage statistics
    """
    # Use default logger if none provided
    if logger is None:
        logging.basicConfig(level=logging.INFO, 
                            format='%(asctime)s - %(levelname)s - %(message)s')
        logger = logging.getLogger(__name__)
    
    # Get memory information
    memory = psutil.virtual_memory()
    
    # Create memory usage statistics dictionary
    memory_stats = {
        'total_memory_bytes': memory.total,
        'available_memory_bytes': memory.available,
        'used_memory_bytes': memory.used,
        'memory_percent_used': memory.percent,
        'process_memory_bytes': psutil.Process(os.getpid()).memory_info().rss
    }
    
    # Log the memory statistics
    logger.info(f"Memory Usage Statistics:")
    logger.info(f"Total Memory: {memory_stats['total_memory_bytes']:,} bytes")
    logger.info(f"Available Memory: {memory_stats['available_memory_bytes']:,} bytes")
    logger.info(f"Used Memory: {memory_stats['used_memory_bytes']:,} bytes")
    logger.info(f"Memory Usage Percentage: {memory_stats['memory_percent_used']}%")
    logger.info(f"Current Process Memory: {memory_stats['process_memory_bytes']:,} bytes")
    
    return memory_stats