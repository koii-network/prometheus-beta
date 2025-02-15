import sys
import time

def dynamic_progress_bar(iterable, desc='Progress', bar_length=50):
    """
    Create a dynamic progress bar that updates while iterating through an iterable.
    
    Args:
        iterable (iterable): The iterable to track progress for
        desc (str, optional): Description of the progress. Defaults to 'Progress'.
        bar_length (int, optional): Length of the progress bar. Defaults to 50.
    
    Yields:
        Items from the input iterable
    """
    total = len(iterable)
    
    for i, item in enumerate(iterable, 1):
        # Calculate percentage and progress
        percent = float(i) / total
        filled_length = int(bar_length * percent)
        
        # Create bar with '=' for filled and '-' for remaining
        bar = '=' * filled_length + '-' * (bar_length - filled_length)
        
        # Construct the progress message
        status = f'{desc}: [{bar}] {int(percent * 100)}% ({i}/{total})'
        
        # Print and flush to ensure immediate update
        sys.stdout.write('\r' + status)
        sys.stdout.flush()
        
        yield item
    
    # Move to next line after completion
    print()