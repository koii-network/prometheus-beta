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
        The items from the original iterable
    
    Raises:
        ValueError: If bar_length is less than 10
    """
    # Validate inputs
    if bar_length < 10:
        raise ValueError("Progress bar length must be at least 10 characters")
    
    # Get total items if possible
    try:
        total = len(iterable)
    except TypeError:
        # If length can't be determined, use a different progress indicator
        for i, item in enumerate(iterable, 1):
            sys.stdout.write(f'\r{desc}: {i} items processed')
            sys.stdout.flush()
            yield item
        sys.stdout.write('\n')
        return
    
    # Handle empty iterable
    if total == 0:
        sys.stdout.write(f'\r{desc}: |{"-" * bar_length}| 100% (0/0)\n')
        return
    
    # Main progress bar logic
    for i, item in enumerate(iterable, 1):
        # Calculate percentage and progress
        percent = float(i) / total
        filled_length = int(bar_length * percent)
        
        # Create bar with filled and unfilled sections
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        
        # Output progress bar
        sys.stdout.write(f'\r{desc}: |{bar}| {percent:.0%} ({i}/{total})')
        sys.stdout.flush()
        
        yield item
    
    # New line after completion
    sys.stdout.write('\n')