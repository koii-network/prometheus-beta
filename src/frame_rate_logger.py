class FrameRateLogger:
    def __init__(self, log_interval=1000):
        """
        Initialize a frame rate logger.
        
        :param log_interval: Interval in milliseconds between frame rate calculations (default: 1000ms)
        """
        self.frames_rendered = 0
        self.start_time = None
        self.log_interval = log_interval
        self.logs = []
    
    def start(self):
        """
        Start frame rate tracking.
        """
        self.start_time = self._get_current_time()
        self.frames_rendered = 0
    
    def log_frame(self):
        """
        Log a single frame render.
        """
        self.frames_rendered += 1
        current_time = self._get_current_time()
        
        # Calculate frame rate if log interval has passed
        if current_time - self.start_time >= self.log_interval:
            fps = (self.frames_rendered / (current_time - self.start_time)) * 1000
            log_entry = {
                'timestamp': current_time,
                'frames_rendered': self.frames_rendered,
                'fps': round(fps, 2)
            }
            self.logs.append(log_entry)
            
            # Reset for next interval
            self.start_time = current_time
            self.frames_rendered = 0
    
    def get_logs(self):
        """
        Retrieve logged frame rates.
        
        :return: List of frame rate log entries
        """
        return self.logs
    
    def _get_current_time(self):
        """
        Get current time in milliseconds.
        
        In a browser environment, this would typically use performance.now()
        This method can be overridden for testing or different time sources.
        
        :return: Current time in milliseconds
        """
        try:
            # Simulating browser performance.now() 
            import time
            return int(time.time() * 1000)
        except ImportError:
            return 0