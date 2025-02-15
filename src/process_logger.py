import logging
import time
from typing import Callable, Any, Optional

class ProcessLogger:
    def __init__(self, logger: Optional[logging.Logger] = None):
        """
        Initialize a ProcessLogger with optional custom logger.
        
        :param logger: Optional custom logger. If not provided, creates a default logger.
        """
        self.logger = logger or logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO, 
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def log_progress(self, 
                     func: Callable[..., Any], 
                     *args, 
                     total_steps: Optional[int] = None, 
                     update_interval: float = 1.0, 
                     **kwargs) -> Any:
        """
        Log real-time progress of a function execution.
        
        :param func: Function to be executed and logged
        :param args: Positional arguments for the function
        :param total_steps: Optional total number of steps for percentage calculation
        :param update_interval: Time interval between progress logs (in seconds)
        :param kwargs: Keyword arguments for the function
        :return: Result of the function execution
        """
        def progress_wrapper():
            start_time = time.time()
            current_step = 0
            last_update_time = start_time

            try:
                result = func(*args, **kwargs)
                
                # If the function returns an iterable, track progress
                if hasattr(result, '__iter__'):
                    for item in result:
                        current_step += 1
                        
                        # Log progress at specified intervals
                        current_time = time.time()
                        if current_time - last_update_time >= update_interval:
                            elapsed_time = current_time - start_time
                            
                            # Calculate percentage if total_steps is provided
                            if total_steps is not None:
                                percentage = (current_step / total_steps) * 100
                                self.logger.info(f"Progress: {current_step}/{total_steps} ({percentage:.2f}%) - Elapsed: {elapsed_time:.2f}s")
                            else:
                                self.logger.info(f"Progress: {current_step} steps - Elapsed: {elapsed_time:.2f}s")
                            
                            last_update_time = current_time
                        
                        yield item
                else:
                    self.logger.info("Function does not return an iterable. Unable to track progress.")
                    return result

            except Exception as e:
                self.logger.error(f"Error during process execution: {e}")
                raise

        return progress_wrapper() if hasattr(func, '__iter__') else func(*args, **kwargs)