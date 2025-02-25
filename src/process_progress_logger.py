import logging
import time
from typing import Callable, Optional, Any

class ProcessProgressLogger:
    """
    A utility class for logging real-time progress of a process.
    
    Allows tracking progress, estimated time remaining, and logging progress updates.
    """
    
    def __init__(self, 
                 total_steps: int, 
                 logger: Optional[logging.Logger] = None, 
                 log_level: int = logging.INFO):
        """
        Initialize the progress logger.
        
        Args:
            total_steps (int): Total number of steps in the process
            logger (Optional[logging.Logger]): Logger to use. If None, creates a default logger
            log_level (int): Logging level to use for progress updates
        
        Raises:
            ValueError: If total_steps is not a positive integer
        """
        if not isinstance(total_steps, int) or total_steps <= 0:
            raise ValueError("total_steps must be a positive integer")
        
        self.total_steps = total_steps
        self.current_step = 0
        self.start_time = time.time()
        
        # Set up logger
        self.logger = logger or logging.getLogger(__name__)
        self.log_level = log_level
    
    def update(self, steps: int = 1):
        """
        Update the progress of the process.
        
        Args:
            steps (int, optional): Number of steps completed. Defaults to 1.
        
        Raises:
            ValueError: If steps would cause progress to exceed total steps
        """
        if self.current_step + steps > self.total_steps:
            raise ValueError("Cannot progress beyond total steps")
        
        self.current_step += steps
        
        # Calculate progress percentage
        progress_percent = (self.current_step / self.total_steps) * 100
        
        # Calculate estimated time
        elapsed_time = time.time() - self.start_time
        if self.current_step > 0:
            estimated_total_time = (elapsed_time / self.current_step) * self.total_steps
            remaining_time = max(0, estimated_total_time - elapsed_time)
        else:
            remaining_time = 0
        
        # Log progress
        self.logger.log(
            self.log_level, 
            f"Progress: {self.current_step}/{self.total_steps} "
            f"({progress_percent:.2f}%) "
            f"- Estimated time remaining: {remaining_time:.2f} seconds"
        )
    
    def complete(self):
        """
        Mark the process as complete.
        
        Logs total time taken and ensures full progress is recorded.
        """
        # Ensure we're at full progress
        if self.current_step < self.total_steps:
            self.current_step = self.total_steps
        
        total_time = time.time() - self.start_time
        
        self.logger.log(
            self.log_level, 
            f"Process complete. Total time: {total_time:.2f} seconds"
        )

def track_process(
    process: Callable[..., Any], 
    total_steps: int, 
    logger: Optional[logging.Logger] = None
) -> Any:
    """
    Decorator to track progress of a process automatically.
    
    Args:
        process (Callable): The process to track
        total_steps (int): Total number of steps in the process
        logger (Optional[logging.Logger]): Logger to use. If None, uses default logger
    
    Returns:
        Wrapped function that logs progress
    """
    def wrapper(*args, **kwargs):
        progress_logger = ProcessProgressLogger(total_steps, logger)
        
        try:
            result = process(*args, **kwargs)
            progress_logger.complete()
            return result
        except Exception as e:
            progress_logger.logger.error(f"Process failed: {str(e)}")
            raise
    
    return wrapper