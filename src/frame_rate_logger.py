import time
from typing import Callable, Optional, List

class FrameRateLogger:
    def __init__(self, log_interval: float = 1.0):
        """
        Initialize the frame rate logger.
        
        :param log_interval: Time interval between logging frame rates (default 1 second)
        """
        self.frame_count = 0
        self.last_log_time = time.time()
        self.log_interval = log_interval
        self.frame_rates = []
    
    def log_frame(self) -> Optional[float]:
        """
        Record a frame and calculate frame rate if log interval has passed.
        
        :return: Calculated frame rate if logging occurs, None otherwise
        """
        current_time = time.time()
        self.frame_count += 1
        
        # Check if log interval has passed
        if current_time - self.last_log_time >= self.log_interval:
            # Calculate frame rate
            elapsed_time = current_time - self.last_log_time
            frame_rate = self.frame_count / elapsed_time
            
            # Store and reset
            self.frame_rates.append(frame_rate)
            self.frame_count = 0
            self.last_log_time = current_time
            
            return frame_rate
        
        return None
    
    def get_frame_rates(self) -> List[float]:
        """
        Retrieve all logged frame rates.
        
        :return: List of logged frame rates
        """
        return self.frame_rates.copy()
    
    def reset(self):
        """
        Reset the frame rate logger to its initial state.
        """
        self.frame_count = 0
        self.last_log_time = time.time()
        self.frame_rates = []