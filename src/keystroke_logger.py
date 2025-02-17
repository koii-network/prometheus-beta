import logging
import datetime
import os

class KeystrokeLogger:
    def __init__(self, log_file='keystroke_log.txt'):
        """
        Initialize the keystroke logger.
        
        :param log_file: Path to the log file (default: keystroke_log.txt)
        """
        # Ensure logs directory exists
        os.makedirs('logs', exist_ok=True)
        self.log_file = os.path.join('logs', log_file)
        
        # Configure logging with file handler to ensure file is written
        self.logger = logging.getLogger(f'keystroke_logger_{log_file}')
        self.logger.setLevel(logging.INFO)
        
        # Clear any existing handlers to prevent duplicate logs
        self.logger.handlers.clear()
        
        # Create file handler
        file_handler = logging.FileHandler(self.log_file, mode='a')
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        self.logger.addHandler(file_handler)
    
    def log_keystroke(self, key):
        """
        Log a single keystroke.
        
        :param key: The key pressed by the user
        :raises TypeError: If key is not a string
        """
        # Validate input
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        
        # Log the keystroke
        self.logger.info(f"Keystroke: {key}")
    
    def get_log_contents(self):
        """
        Retrieve the contents of the log file.
        
        :return: List of log entries
        """
        try:
            with open(self.log_file, 'r') as f:
                return f.readlines()
        except FileNotFoundError:
            return []