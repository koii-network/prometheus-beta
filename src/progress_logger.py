from typing import Iterable, Any, Optional
from tqdm import tqdm

def log_progress(
    iterable: Iterable[Any], 
    desc: Optional[str] = None, 
    total: Optional[int] = None
) -> Iterable[Any]:
    """
    Create a dynamically updating progress bar for an iterable.

    Args:
        iterable (Iterable): The input iterable to track progress for.
        desc (Optional[str], optional): Description of the progress bar. Defaults to None.
        total (Optional[int], optional): Total number of items. Defaults to None.

    Returns:
        Iterable: An iterable wrapped with a progress bar.

    Raises:
        TypeError: If the input is not an iterable.
        ValueError: If total is provided but is not a positive integer.
    """
    # Validate inputs
    if not hasattr(iterable, '__iter__'):
        raise TypeError("Input must be an iterable")
    
    if total is not None and (not isinstance(total, int) or total <= 0):
        raise ValueError("Total must be a positive integer")

    # Use tqdm to create a dynamic progress bar
    return tqdm(
        iterable, 
        desc=desc, 
        total=total, 
        dynamic_ncols=True,  # Dynamically adjust to terminal width
        unit='it',  # Default unit of iteration
        unit_scale=True  # Auto-scale unit (k, M, etc.)
    )