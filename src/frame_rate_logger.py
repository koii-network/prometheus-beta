import time
from typing import Callable, Optional, List

class FrameRateLogger:
    """
    A class to log and analyze frame rates in a browser environment.
    
    This logger provides methods to track frame rendering performance 
    by measuring time between frames and calculating various frame rate metrics.
    """
    
    def __init__(self, sample_size: int = 60):
        """
        Initialize the FrameRateLogger.
        
        :param sample_size: Number of frames to track for calculating statistics
        """
        self.frame_times: List[float] = []
        self.sample_size = max(1, sample_size)
        self.start_time: Optional[float] = None
    
    def start(self):
        """
        Start frame rate tracking.
        """
        self.frame_times = []
        self.start_time = time.time()
    
    def log_frame(self):
        """
        Log a new frame and calculate frame time.
        
        :return: Current frame time in milliseconds
        """
        current_time = time.time()
        
        # If this is the first frame, just record the time
        if self.start_time is None:
            self.start_time = current_time
            return 0.0
        
        # Calculate frame time in milliseconds
        frame_time = (current_time - self.start_time) * 1000
        
        # Store frame time and maintain sample size
        self.frame_times.append(frame_time)
        if len(self.frame_times) > self.sample_size:
            self.frame_times.pop(0)
        
        return frame_time
    
    def get_fps(self) -> float:
        """
        Calculate current frames per second (FPS).
        
        :return: Frames per second, or 0 if not enough data
        """
        if len(self.frame_times) < 2:
            return 0.0
        
        # Calculate average frame time
        avg_frame_time = sum(self.frame_times) / len(self.frame_times)
        
        # Convert to FPS
        return 1000 / avg_frame_time if avg_frame_time > 0 else 0.0
    
    def get_frame_time_stats(self) -> dict:
        """
        Get frame time statistics.
        
        :return: Dictionary of frame time statistics
        """
        if not self.frame_times:
            return {
                'avg_frame_time': 0.0,
                'min_frame_time': 0.0,
                'max_frame_time': 0.0
            }
        
        return {
            'avg_frame_time': sum(self.frame_times) / len(self.frame_times),
            'min_frame_time': min(self.frame_times),
            'max_frame_time': max(self.frame_times)
        }