import sys
import time

def dynamic_progress_logger(iterable, total=None, prefix='Progress:', suffix='Complete', 
                             decimals=1, length=50, fill='█', print_end="\r"):
    """
    Dynamic progress bar logger that updates output for iterables.
    
    Args:
        iterable: Input collection to iterate over
        total: Total number of iterations (optional, defaults to len(iterable))
        prefix: Prefix string before progress bar
        suffix: Suffix string after progress bar
        decimals: Number of decimal places for percentage
        length: Character length of progress bar
        fill: Bar fill character
        print_end: End character (default prevents multiple lines)
    
    Yields:
        Items from the original iterable
    """
    # If total is not provided, try to get length of iterable
    if total is None:
        try:
            total = len(iterable)
        except TypeError:
            total = sum(1 for _ in iterable)
            # Reset iterable after counting
            iterable = list(iterable)
    
    # Validate inputs
    if total <= 0:
        raise ValueError("Total must be a positive number")
    
    def print_progress_bar(iteration):
        """Internal function to print and update progress bar"""
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + '-' * (length - filled_length)
        
        sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
        sys.stdout.flush()
    
    # Initial call
    print_progress_bar(0)
    
    # Iterate through items
    for i, item in enumerate(iterable, 1):
        yield item
        print_progress_bar(i)
    
    # Print newline on completion
    print()