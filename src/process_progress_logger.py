import time
import logging
from typing import Callable, Optional, Any

class ProcessProgressLogger:
    """
    A utility class for logging real-time progress of processes.
    
    This class provides methods to track and log the progress of long-running tasks,
    with configurable logging levels and update intervals.
    """
    
    def __init__(self, logger: Optional[logging.Logger] = None, log_level: int = logging.INFO):
        """
        Initialize the ProcessProgressLogger.
        
        Args:
            logger (Optional[logging.Logger]): Custom logger. If None, creates a default logger.
            log_level (int): Logging level (default: logging.INFO)
        """
        self.logger = logger or logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
    
    def track_progress(
        self, 
        process: Callable[..., Any], 
        *args, 
        total_steps: Optional[int] = None, 
        update_interval: float = 1.0, 
        **kwargs
    ) -> Any:
        """
        Execute a process while logging its progress.
        
        Args:
            process (Callable): The function/process to track
            *args: Positional arguments for the process
            total_steps (Optional[int]): Total number of steps for percentage calculation
            update_interval (float): Interval between progress updates in seconds
            **kwargs: Keyword arguments for the process
        
        Returns:
            The result of the process
        
        Raises:
            ValueError: If total_steps is not a positive integer when provided
        """
        if total_steps is not None and total_steps <= 0:
            raise ValueError("total_steps must be a positive integer")
        
        start_time = time.time()
        current_step = 0
        result = None
        
        try:
            def progress_wrapper(*wrapper_args, **wrapper_kwargs):
                nonlocal current_step, result
                current_step += 1
                
                if total_steps is not None:
                    percentage = (current_step / total_steps) * 100
                    progress_msg = f"Progress: {current_step}/{total_steps} ({percentage:.2f}%)"
                else:
                    progress_msg = f"Step {current_step} completed"
                
                self.logger.info(progress_msg)
                
                # If this is a generator, yield the result
                if hasattr(process, '__next__'):
                    result = next(process(*wrapper_args, **wrapper_kwargs))
                    return result
                
                # If this is a regular function, return the result
                result = process(*wrapper_args, **wrapper_kwargs)
                return result
            
            # If process is a generator
            if hasattr(process, '__iter__'):
                list(map(progress_wrapper, *args, **kwargs))
            else:
                # Regular function
                result = progress_wrapper(*args, **kwargs)
            
            elapsed_time = time.time() - start_time
            self.logger.info(f"Process completed in {elapsed_time:.2f} seconds")
            
            return result
        
        except Exception as e:
            self.logger.error(f"Process failed: {str(e)}")
            raise