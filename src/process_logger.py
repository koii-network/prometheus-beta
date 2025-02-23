import time
import sys
from typing import Callable, Any

def log_process_progress(task: Callable[..., Any], *args, **kwargs) -> Any:
    """
    Decorator to log real-time progress of a process.
    
    :param task: The function to be monitored
    :param args: Positional arguments for the task
    :param kwargs: Keyword arguments for the task
    :return: Result of the task
    """
    def progress_bar(current, total, bar_length=50):
        """Generate a progress bar string."""
        filled_length = int(round(bar_length * current / float(total)))
        percents = round(100.0 * current / float(total), 1)
        bar = '=' * filled_length + '-' * (bar_length - filled_length)
        sys.stdout.write(f'\r[{bar}] {percents}% Complete')
        sys.stdout.flush()

    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Starting process: {task.__name__}")
        
        # Check if the task has a length or total items
        try:
            total = kwargs.get('total') or len(args[0]) if args else 100
        except:
            total = 100

        # Track progress
        for i in range(total + 1):
            # Update progress bar
            progress_bar(i, total)
            
            # If it's the last iteration, complete the progress
            if i == total:
                print("\nProcess completed successfully!")
                break
            
            # Small delay to simulate processing
            time.sleep(0.1)
        
        # Execute the actual task
        result = task(*args, **kwargs)
        
        end_time = time.time()
        print(f"\nTotal execution time: {end_time - start_time:.2f} seconds")
        
        return result

    return wrapper

# Example usage
@log_process_progress
def example_long_running_task(items):
    """
    Simulate a long-running task by processing a list of items.
    
    :param items: List of items to process
    :return: Processed items
    """
    processed_items = []
    for item in items:
        # Simulate some processing
        processed_items.append(item.upper())
    return processed_items