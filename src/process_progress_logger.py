import time
import logging
from typing import Callable, Optional

class ProcessProgressLogger:
    """
    A utility class for logging the real-time progress of a process.
    
    Allows tracking and logging progress of long-running tasks with 
    configurable logging and update intervals.
    """
    
    def __init__(self, 
                 logger: Optional[logging.Logger] = None, 
                 log_level: int = logging.INFO,
                 update_interval: float = 1.0):
        """
        Initialize the ProcessProgressLogger.
        
        Args:
            logger (Optional[logging.Logger]): Logger to use. 
                If None, creates a default logger.
            log_level (int): Logging level (default: logging.INFO)
            update_interval (float): Minimum time between progress updates (in seconds)
        """
        self._logger = logger or logging.getLogger(__name__)
        self._log_level = log_level
        self._update_interval = update_interval
        self._last_log_time = 0
    
    def log_progress(self, 
                     current: int, 
                     total: int, 
                     prefix: str = "Progress") -> None:
        """
        Log the progress of a process.
        
        Args:
            current (int): Current progress value
            total (int): Total expected value
            prefix (str, optional): Custom prefix for log message
        
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
        
        # Calculate percentage
        current_time = time.time()
        if current_time - self._last_log_time >= self._update_interval:
            percentage = (current / total) * 100
            message = f"{prefix}: {current}/{total} ({percentage:.2f}%)"
            self._logger.log(self._log_level, message)
            self._last_log_time = current_time
    
    def track_process(self, 
                      process: Callable, 
                      total: int, 
                      prefix: str = "Progress") -> Any:
        """
        Wrap a process to automatically log its progress.
        
        Args:
            process (Callable): Function to track
            total (int): Total expected iterations
            prefix (str, optional): Custom prefix for log message
        
        Returns:
            Result of the process
        """
        def wrapper(*args, **kwargs):
            results = []
            for i in range(total):
                result = process(*args, **kwargs)
                results.append(result)
                self.log_progress(i + 1, total, prefix)
            return results
        
        return wrapper