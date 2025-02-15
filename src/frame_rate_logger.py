import time
from typing import Callable, Optional

class FrameRateLogger:
    """
    A class to log and track frame rates in a browser environment.
    """
    def __init__(self, log_interval: float = 1.0):
        """
        Initialize the FrameRateLogger.
        
        :param log_interval: Interval (in seconds) between frame rate calculations
        """
        self.frames_count = 0
        self.start_time = time.time()
        self.log_interval = log_interval
        self.last_log_time = self.start_time
        self.on_log_callback: Optional[Callable[[float], None]] = None

    def log_frame(self):
        """
        Log a frame and calculate frame rate if log interval has passed.
        """
        current_time = time.time()
        self.frames_count += 1

        # Check if log interval has passed
        if current_time - self.last_log_time >= self.log_interval:
            frame_rate = self.frames_count / (current_time - self.last_log_time)
            
            # Call callback if set
            if self.on_log_callback:
                self.on_log_callback(frame_rate)
            
            # Reset for next interval
            self.frames_count = 0
            self.last_log_time = current_time

    def set_log_callback(self, callback: Callable[[float], None]):
        """
        Set a callback function to be called when frame rate is calculated.
        
        :param callback: Function that takes frame rate as an argument
        """
        self.on_log_callback = callback

    def get_total_runtime(self) -> float:
        """
        Get the total runtime of the logger.
        
        :return: Total runtime in seconds
        """
        return time.time() - self.start_time