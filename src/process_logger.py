import logging
import time
from typing import Callable, Optional, Any

class ProcessLogger:
    """
    A utility class for logging real-time progress of a process.
    
    Provides methods to track and log the progress of long-running tasks
    with customizable logging and progress tracking.
    """
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """
        Initialize the ProcessLogger.
        
        Args:
            logger (Optional[logging.Logger]): Custom logger. 
                If not provided, a default logger will be created.
        """
        self.logger = logger or logging.getLogger(__name__)
        self.start_time = None
        self.current_progress = 0
    
    def log_progress(self, current: int, total: int, frequency: int = 10, 
                     message: Optional[str] = None) -> None:
        """
        Log the progress of a process at specified intervals.
        
        Args:
            current (int): Current progress value
            total (int): Total expected value
            frequency (int, optional): Log every nth update. Defaults to 10.
            message (Optional[str], optional): Custom message to include in log
        
        Raises:
            ValueError: If current or total are invalid
        """
        # Validate inputs
        if total <= 0:
            raise ValueError("Total must be a positive number")
        if current < 0:
            raise ValueError("Current progress cannot be negative")
        if current > total:
            raise ValueError("Current progress cannot exceed total")
        
        # Initialize start time on first call
        if self.start_time is None:
            self.start_time = time.time()
        
        # Calculate progress percentage
        progress_percent = (current / total) * 100
        
        # Log at specified frequency
        if current % frequency == 0 or current == total:
            # Construct log message
            log_msg = f"Progress: {current}/{total} ({progress_percent:.2f}%)"
            if message:
                log_msg += f" - {message}"
            
            # Add time elapsed
            time_elapsed = time.time() - self.start_time
            log_msg += f" | Time elapsed: {time_elapsed:.2f}s"
            
            # Log the message
            self.logger.info(log_msg)
        
        # Update current progress
        self.current_progress = current
    
    def track_process(self, process: Callable[..., Any], *args, **kwargs) -> Any:
        """
        Track the progress of a callable process.
        
        Args:
            process (Callable): Function to track
            *args: Positional arguments for the process
            **kwargs: Keyword arguments for the process
        
        Returns:
            The result of the process
        """
        try:
            result = process(*args, **kwargs)
            return result
        except Exception as e:
            self.logger.error(f"Process failed: {str(e)}")
            raise