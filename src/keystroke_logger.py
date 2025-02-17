import logging
import os
from pynput import keyboard

class KeystrokeLogger:
    def __init__(self, log_file='keystrokes.log'):
        """
        Initialize the keystroke logger.
        
        :param log_file: Path to the log file where keystrokes will be recorded
        """
        # Ensure the logs directory exists
        os.makedirs('logs', exist_ok=True)
        self.log_file = os.path.join('logs', log_file)
        
        # Configure logging
        logging.basicConfig(
            filename=self.log_file, 
            level=logging.INFO, 
            format='%(asctime)s - %(message)s'
        )
        
        # Keyboard listener
        self.listener = None

    def on_press(self, key):
        """
        Callback method for key press events.
        
        :param key: The key that was pressed
        """
        try:
            # Try to log the character representation of the key
            char = key.char
            logging.info(f"Key pressed: {char}")
        except AttributeError:
            # Handle special keys (e.g., Enter, Shift, etc.)
            logging.info(f"Special key pressed: {key}")

    def start_logging(self):
        """
        Start logging keystrokes.
        
        :return: The keyboard listener
        """
        # Prevent multiple listeners
        if self.listener:
            return self.listener
        
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        logging.info("Keystroke logging started")
        return self.listener

    def stop_logging(self):
        """
        Stop logging keystrokes.
        """
        if self.listener:
            self.listener.stop()
            logging.info("Keystroke logging stopped")
            self.listener = None

    def get_log_file_path(self):
        """
        Get the path to the log file.
        
        :return: Path to the log file
        """
        return self.log_file