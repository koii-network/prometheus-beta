import time
from typing import List, Dict, Optional

class FrameRateLogger:
    def __init__(self, log_interval: float = 1.0):
        """
        Initialize the frame rate logger.
        
        :param log_interval: Time interval between frame rate calculations (default 1 second)
        """
        self.frames_rendered = 0
        self.start_time = time.time()
        self.log_interval = log_interval
        self.frame_rate_history: List[Dict[str, float]] = []

    def log_frame(self) -> Optional[float]:
        """
        Log a frame and calculate frame rate if log interval has passed.
        
        :return: Current frame rate if calculated, otherwise None
        """
        current_time = time.time()
        self.frames_rendered += 1

        # Check if log interval has passed
        if current_time - self.start_time >= self.log_interval:
            frame_rate = self.frames_rendered / (current_time - self.start_time)
            
            # Store frame rate log
            log_entry = {
                'timestamp': current_time,
                'frame_rate': frame_rate,
                'frames_rendered': self.frames_rendered
            }
            self.frame_rate_history.append(log_entry)

            # Reset for next interval
            self.frames_rendered = 0
            self.start_time = current_time

            return frame_rate
        
        return None

    def get_frame_rate_history(self) -> List[Dict[str, float]]:
        """
        Retrieve the history of frame rate logs.
        
        :return: List of frame rate log entries
        """
        return self.frame_rate_history