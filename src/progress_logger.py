import sys
import time
from typing import Callable, Any, Optional

class ProgressLogger:
    """
    A utility class for logging real-time progress of a process.
    
    This class provides methods to track and display the progress of 
    long-running tasks with customizable output and update mechanisms.
    """
    
    def __init__(self, total_steps: Optional[int] = None, prefix: str = 'Progress', 
                 suffix: str = 'Complete', decimals: int = 1, 
                 length: int = 50, fill: str = '█', 
                 print_end: str = "\r"):
        """
        Initialize the ProgressLogger.
        
        :param total_steps: Total number of steps in the process (optional)
        :param prefix: Prefix text for the progress bar
        :param suffix: Suffix text for the progress bar
        :param decimals: Number of decimal places for percentage
        :param length: Character length of the progress bar
        :param fill: Character to use for filling the progress bar
        :param print_end: End character for print (default prevents multiple lines)
        """
        self.total_steps = total_steps
        self.prefix = prefix
        self.suffix = suffix
        self.decimals = decimals
        self.length = length
        self.fill = fill
        self.print_end = print_end
        self.start_time = time.time()
    
    def print_progress_bar(self, iteration: int, 
                            additional_info: Optional[str] = None):
        """
        Print/update progress bar.
        
        :param iteration: Current iteration
        :param additional_info: Optional additional information to display
        """
        # Prevent division by zero
        if self.total_steps is None or self.total_steps == 0:
            return
        
        # Calculate percentage and progress bar
        percent = ("{0:." + str(self.decimals) + "f}").format(
            100 * (iteration / float(self.total_steps))
        )
        filled_length = int(self.length * iteration // self.total_steps)
        bar = self.fill * filled_length + '-' * (self.length - filled_length)
        
        # Calculate elapsed time
        elapsed_time = time.time() - self.start_time
        
        # Construct output string
        output = f'\r{self.prefix} |{bar}| {percent}% {self.suffix}'
        
        # Add additional info if provided
        if additional_info:
            output += f' | {additional_info}'
        
        # Print with time tracking
        sys.stdout.write(output)
        sys.stdout.flush()
        
        # Print new line on completion
        if iteration == self.total_steps:
            print()
    
    def track_progress(self, 
                       process: Callable[..., Any], 
                       *args, 
                       **kwargs) -> Any:
        """
        Wrap a process with progress tracking.
        
        :param process: Function to track
        :param args: Positional arguments for the process
        :param kwargs: Keyword arguments for the process
        :return: Result of the process
        """
        if self.total_steps is None:
            return process(*args, **kwargs)
        
        # Track progress while running the process
        for i in range(self.total_steps + 1):
            # Call process at appropriate intervals
            if i == self.total_steps:
                self.print_progress_bar(i)
                break
            
            # Simulate progress or allow custom progress tracking
            result = process(*args, **kwargs)
            
            # Update progress bar
            self.print_progress_bar(i)
        
        return result