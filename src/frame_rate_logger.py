class FrameRateLogger:
    def __init__(self, log_interval=1000):
        """
        Initialize a frame rate logger.
        
        :param log_interval: Interval in milliseconds between frame rate calculations
        """
        self.frames = 0
        self.start_time = None
        self.log_interval = log_interval
        self.last_log_time = None
        self.fps_callback = None

    def start_tracking(self, fps_callback=None):
        """
        Start tracking frame rates.
        
        :param fps_callback: Optional callback function to handle FPS logging
        """
        import time
        self.frames = 0
        self.start_time = time.time() * 1000  # Convert to milliseconds
        self.last_log_time = self.start_time
        self.fps_callback = fps_callback

    def log_frame(self):
        """
        Log a single frame and calculate frame rate if needed.
        
        :return: Current frames per second (FPS) if logged, None otherwise
        """
        import time
        
        # Increment frame count
        self.frames += 1
        
        # Ensure tracking has started
        if self.start_time is None:
            return None
        
        # Get current time in milliseconds
        current_time = time.time() * 1000
        
        # Check if it's time to log frame rate
        if current_time - self.last_log_time >= self.log_interval:
            # Calculate elapsed time and FPS
            elapsed_time = (current_time - self.start_time) / 1000  # Convert to seconds
            fps = self.frames / elapsed_time
            
            # Call callback if provided
            if self.fps_callback:
                self.fps_callback(fps)
            
            # Reset for next interval
            self.frames = 0
            self.start_time = current_time
            self.last_log_time = current_time
            
            return fps
        
        return None

    def stop_tracking(self):
        """
        Stop tracking frame rates and reset the logger.
        """
        self.frames = 0
        self.start_time = None
        self.last_log_time = None
        self.fps_callback = None