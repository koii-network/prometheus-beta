import time
import sys
from typing import Callable, Any, Optional

def log_process_progress(process_func: Callable[..., Any], 
                         total_steps: int, 
                         update_interval: float = 0.5, 
                         log_func: Optional[Callable[[str], None]] = None) -> Any:
    """
    Log real-time progress of a process with customizable logging.
    
    Args:
        process_func (Callable): The function to be executed
        total_steps (int): Total number of steps in the process
        update_interval (float, optional): Interval between progress updates. Defaults to 0.5 seconds.
        log_func (Callable, optional): Custom logging function. Defaults to print if not provided.
    
    Returns:
        The result of the process_func
    """
    # Use print as default logging if no custom log function is provided
    if log_func is None:
        log_func = print
    
    def progress_wrapper(*args, **kwargs):
        start_time = time.time()
        current_step = 0
        last_update_time = start_time
        
        def update_progress(step):
            nonlocal current_step, last_update_time
            current_step = step
            current_time = time.time()
            
            # Only update if enough time has passed or it's the last step
            if current_time - last_update_time >= update_interval or step == total_steps:
                progress_percentage = (current_step / total_steps) * 100
                elapsed_time = current_time - start_time
                
                log_func(f"Progress: {current_step}/{total_steps} steps "
                         f"({progress_percentage:.2f}%) - "
                         f"Elapsed time: {elapsed_time:.2f} seconds")
                
                last_update_time = current_time
        
        # Monkey patch sys.stdout.write to track progress
        original_write = sys.stdout.write
        def progress_write(text):
            original_write(text)
            # Try to extract numeric progress if possible
            try:
                # Look for a number followed by a slash or percentage
                progress_match = [s for s in text.split() if '/' in s or '%' in s]
                if progress_match:
                    step_match = progress_match[0]
                    if '/' in step_match:
                        current, total = map(int, step_match.split('/'))
                        update_progress(current)
                    elif '%' in step_match:
                        current_percentage = float(step_match.replace('%', ''))
                        update_progress(int(current_percentage * total_steps / 100))
            except Exception:
                pass
        
        try:
            sys.stdout.write = progress_write
            result = process_func(*args, **kwargs)
            # Ensure final progress is logged
            update_progress(total_steps)
            return result
        finally:
            # Restore original stdout.write
            sys.stdout.write = original_write
    
    return progress_wrapper