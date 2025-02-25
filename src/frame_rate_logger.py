import time
from typing import List, Optional

class FrameRateLogger:
    """
    A utility class for logging frame rates in a browser environment.
    
    This class provides methods to track and calculate frame rates, 
    with support for multiple metrics and error handling.
    """
    
    def __init__(self, buffer_size: int = 60):
        """
        Initialize the FrameRateLogger.
        
        :param buffer_size: Maximum number of frame times to keep in memory
        """
        self.frame_times: List[float] = []
        self.buffer_size = max(1, buffer_size)
    
    def log_frame(self) -> None:
        """
        Log the current frame time.
        
        Adds the current timestamp to the frame times list,
        maintaining the specified buffer size.
        """
        current_time = time.time()
        self.frame_times.append(current_time)
        
        # Maintain the buffer size by removing oldest frames
        if len(self.frame_times) > self.buffer_size:
            self.frame_times.pop(0)
    
    def get_fps(self) -> Optional[float]:
        """
        Calculate the current frames per second (FPS).
        
        :return: Calculated FPS, or None if insufficient data
        """
        if len(self.frame_times) < 2:
            return None
        
        # Calculate time span and number of frames
        time_span = self.frame_times[-1] - self.frame_times[0]
        frame_count = len(self.frame_times) - 1
        
        # Prevent division by zero
        if time_span <= 0:
            return None
        
        # Calculate and return FPS
        return frame_count / time_span
    
    def reset(self) -> None:
        """
        Reset the frame times buffer.
        """
        self.frame_times.clear()