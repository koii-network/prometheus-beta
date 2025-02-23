import time
import logging
from typing import Callable, Optional, Any

class ProcessProgressLogger:
    """
    A utility class for logging real-time progress of a process.
    
    This class provides methods to track and log the progress of long-running 
    operations with customizable logging and progress tracking.
    """
    
    def __init__(self, 
                 logger: Optional[logging.Logger] = None, 
                 log_level: int = logging.INFO):
        """
        Initialize the ProcessProgressLogger.
        
        Args:
            logger (Optional[logging.Logger]): A custom logger. 
                If None, creates a default logger.
            log_level (int): Logging level for progress updates. 
                Defaults to logging.INFO.
        """
        # Use provided logger or create a default one
        self.logger = logger or logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        
        # Progress tracking attributes
        self.total_steps = 0
        self.current_step = 0
        self.start_time = None
    
    def start(self, total_steps: int):
        """
        Initialize progress tracking.
        
        Args:
            total_steps (int): Total number of steps in the process.
        
        Raises:
            ValueError: If total_steps is not a positive integer.
        """
        if total_steps <= 0:
            raise ValueError("Total steps must be a positive integer")
        
        self.total_steps = total_steps
        self.current_step = 0
        self.start_time = time.time()
        
        self.logger.info(f"Process started. Total steps: {total_steps}")
    
    def update(self, steps: int = 1):
        """
        Update progress and log the current status.
        
        Args:
            steps (int): Number of steps completed. Defaults to 1.
        
        Raises:
            ValueError: If steps would cause progress to exceed total steps.
        """
        if self.start_time is None:
            raise RuntimeError("Progress tracking not started. Call start() first.")
        
        if self.current_step + steps > self.total_steps:
            raise ValueError("Cannot exceed total steps")
        
        self.current_step += steps
        
        # Calculate progress percentage
        progress_percent = (self.current_step / self.total_steps) * 100
        
        # Calculate elapsed time
        elapsed_time = time.time() - self.start_time
        
        # Estimate remaining time if progress has been made
        estimated_total_time = None
        estimated_remaining_time = None
        if self.current_step > 0:
            estimated_total_time = (elapsed_time / self.current_step) * self.total_steps
            estimated_remaining_time = estimated_total_time - elapsed_time
        
        # Log progress
        log_message = (
            f"Progress: {self.current_step}/{self.total_steps} steps "
            f"({progress_percent:.2f}%) "
            f"Elapsed: {elapsed_time:.2f}s"
        )
        
        # Add estimated times if available
        if estimated_total_time is not None:
            log_message += (
                f" Est. Total: {estimated_total_time:.2f}s "
                f"Est. Remaining: {estimated_remaining_time:.2f}s"
            )
        
        self.logger.info(log_message)
        
        return progress_percent
    
    def complete(self):
        """
        Mark the process as complete and log final status.
        
        Raises:
            RuntimeError: If progress tracking was not started.
        """
        if self.start_time is None:
            raise RuntimeError("Progress tracking not started")
        
        if self.current_step < self.total_steps:
            # Auto-complete if not fully progressed
            self.current_step = self.total_steps
        
        total_time = time.time() - self.start_time
        
        self.logger.info(
            f"Process completed. "
            f"Total steps: {self.total_steps}, "
            f"Total time: {total_time:.2f}s"
        )
        
        # Reset tracking
        self.start_time = None
        self.total_steps = 0
        self.current_step = 0