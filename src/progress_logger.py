import sys
from tqdm import tqdm
from typing import Iterable, Any, Optional

def dynamic_progress_log(items: Iterable[Any], 
                          description: Optional[str] = None, 
                          total: Optional[int] = None,
                          log_every: int = 1) -> list:
    """
    Process an iterable with a dynamically updating progress bar and optional logging.
    
    Args:
        items (Iterable): The items to process
        description (str, optional): Description of the progress bar
        total (int, optional): Total number of items if known
        log_every (int, optional): Log a message every nth iteration
    
    Returns:
        list: Processed results from the items
    
    Raises:
        TypeError: If items is not iterable
        ValueError: If log_every is less than 1
    """
    if not hasattr(items, '__iter__'):
        raise TypeError("Input must be an iterable")
    
    if log_every < 1:
        raise ValueError("log_every must be a positive integer")
    
    # Determine total if not provided
    try:
        total = total or len(items)
    except TypeError:
        total = None
    
    results = []
    
    # Capture original stderr in case we need it
    original_stderr = sys.stderr
    
    # Create progress bar
    with tqdm(items, 
              desc=description or "Processing", 
              total=total, 
              unit='item', 
              file=sys.stderr) as progress_bar:
        
        for index, item in enumerate(progress_bar, 1):
            # Process the item
            results.append(item)
            
            # Optional logging
            if log_every > 0 and index % log_every == 0:
                # Use write method to explicitly log
                original_stderr.write(f"Processed {index} items: Current item = {item}\n")
    
    return results