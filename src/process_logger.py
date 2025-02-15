import sys
import time
from typing import Callable, Any, Optional

class ProcessLogger:
    def __init__(self, total_steps: Optional[int] = None, log_func: Optional[Callable] = None):
        """
        Initialize a progress logger.
        
        :param total_steps: Total number of steps in the process (optional)
        :param log_func: Custom logging function (defaults to print to stdout)
        """
        self.total_steps = total_steps
        self.current_step = 0
        self.start_time = time.time()
        self.log_func = log_func or self._default_log

    def _default_log(self, message: str):
        """
        Default logging method that prints to stdout.
        
        :param message: Message to log
        """
        print(message, flush=True)

    def update(self, current_step: Optional[int] = None, message: Optional[str] = None):
        """
        Update the progress of the process.
        
        :param current_step: Current step number (optional)
        :param message: Optional custom message to log
        """
        if current_step is not None:
            self.current_step = current_step
        else:
            self.current_step += 1

        # Calculate progress percentage
        progress_msg = f"Progress: "
        if self.total_steps:
            percentage = (self.current_step / self.total_steps) * 100
            progress_msg += f"{percentage:.2f}% ({self.current_step}/{self.total_steps}) "

        # Calculate elapsed time
        elapsed_time = time.time() - self.start_time
        progress_msg += f"Elapsed: {elapsed_time:.2f}s"

        # Add custom message if provided
        if message:
            progress_msg += f" - {message}"

        # Log the progress
        self.log_func(progress_msg)

    def complete(self, message: Optional[str] = None):
        """
        Mark the process as complete.
        
        :param message: Optional completion message
        """
        total_time = time.time() - self.start_time
        completion_msg = f"Process completed in {total_time:.2f}s"
        
        if message:
            completion_msg += f" - {message}"
        
        self.log_func(completion_msg)
        
        # Reset tracking
        self.current_step = self.total_steps or 0