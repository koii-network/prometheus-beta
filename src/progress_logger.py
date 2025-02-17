import sys
import time

def dynamic_progress_logger(iterable, description='Progress', bar_length=50):
    """
    A generator function that logs progress dynamically using a progress bar.
    
    Args:
        iterable (iterable): The input iterable to track progress for
        description (str, optional): Description of the progress. Defaults to 'Progress'.
        bar_length (int, optional): Length of the progress bar. Defaults to 50.
    
    Yields:
        Items from the input iterable
    """
    total = len(iterable)
    
    for i, item in enumerate(iterable, 1):
        # Calculate percentage and progress
        percent = float(i) / total
        filled_length = int(bar_length * percent)
        
        # Create progress bar
        bar = '=' * filled_length + '-' * (bar_length - filled_length)
        
        # Print progress bar
        sys.stdout.write(f'\r{description}: [{bar}] {int(percent * 100)}% Complete')
        sys.stdout.flush()
        
        yield item
    
    # Add a newline after completion
    sys.stdout.write('\n')