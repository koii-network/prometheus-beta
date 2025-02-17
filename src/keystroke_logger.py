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
        
        # Configure logging
        logging.basicConfig(
            filename=self.log_file, 
            level=logging.INFO, 
            format='%(asctime)s - %(message)s'
        )
    
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
        logging.info(f"Keystroke: {key}")
    
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