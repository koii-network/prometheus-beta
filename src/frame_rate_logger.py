import time
from typing import List, Optional

class FrameRateLogger:
    def __init__(self):
        self._frame_times: List[float] = []
        self._start_time: Optional[float] = None

    def start(self):
        """Start frame rate logging."""
        self._frame_times = []
        self._start_time = time.time()

    def log_frame(self):
        """Log a single frame timestamp."""
        if self._start_time is None:
            raise RuntimeError("Frame rate logging not started. Call start() first.")
        current_time = time.time()
        self._frame_times.append(current_time)

    def get_frame_rate(self, duration: Optional[float] = None) -> float:
        """
        Calculate frame rate.
        
        Args:
            duration (Optional[float]): Duration to calculate frame rate for. 
                                        If None, uses entire logged period.
        
        Returns:
            float: Frames per second (FPS)
        """
        if self._start_time is None:
            raise RuntimeError("Frame rate logging not started. Call start() first.")
        
        if not self._frame_times:
            return 0.0

        current_time = time.time()
        if duration is None:
            start = self._start_time
            end = current_time
        else:
            start = max(current_time - duration, self._start_time)
            end = current_time

        frames_in_period = sum(1 for t in self._frame_times if start <= t <= end)
        total_time = end - start

        return frames_in_period / total_time if total_time > 0 else 0.0