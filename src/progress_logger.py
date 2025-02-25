import sys
import time

def dynamic_progress_logger(iterable, desc='Progress', total=None, update_interval=0.1):
    """
    A generator function that dynamically updates a progress bar while iterating.
    
    :param iterable: The iterable to track progress for
    :param desc: Description of the progress (default: 'Progress')
    :param total: Total number of items (optional)
    :param update_interval: Minimum time between progress updates (default: 0.1 seconds)
    :yields: Items from the original iterable
    """
    # Determine total if not provided
    if total is None:
        try:
            total = len(iterable)
        except TypeError:
            total = None
    
    # If total is known, use percentage-based progress
    if total is not None:
        def update_progress(current, total):
            percent = min(100, max(0, (current / total) * 100))
            bar_length = 50
            filled_length = int(bar_length * current // total)
            bar = '=' * filled_length + '-' * (bar_length - filled_length)
            sys.stdout.write(f'\r{desc}: [{bar}] {percent:.1f}%')
            sys.stdout.flush()
    else:
        # If total is unknown, use spinning cursor
        spinner = ['|', '/', '-', '\\']
        def update_progress(current, _):
            sys.stdout.write(f'\r{desc}: {spinner[current % 4]}')
            sys.stdout.flush()
    
    # Track progress
    current = 0
    last_update_time = 0
    
    try:
        for item in iterable:
            current += 1
            
            # Update progress with throttling
            current_time = time.time()
            if current_time - last_update_time >= update_interval:
                update_progress(current, total or current)
                last_update_time = current_time
            
            yield item
    
    finally:
        # Clear the progress line
        sys.stdout.write('\r' + ' ' * (len(desc) + 60) + '\r')
        sys.stdout.flush()