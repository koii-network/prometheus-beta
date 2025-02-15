import logging
import emoji

class EmojiLogger:
    def __init__(self, log_level=logging.INFO):
        """
        Initialize a logger with optional emoji support.
        
        :param log_level: Logging level (default is logging.INFO)
        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        
        # Create console handler and set level
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        
        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        
        # Add handler to logger
        self.logger.addHandler(console_handler)

    def log(self, message, level=logging.INFO, emoji_symbol=None):
        """
        Log a message with optional emoji.
        
        :param message: The message to log
        :param level: Logging level (default is logging.INFO)
        :param emoji_symbol: Optional emoji to prepend to the message
        """
        # Validate emoji if provided
        if emoji_symbol:
            try:
                # Ensure it's a valid emoji
                emoji_symbol = emoji.emojize(emoji_symbol, language='alias')
                message = f"{emoji_symbol} {message}"
            except Exception:
                # If emoji is invalid, log without modification
                pass
        
        # Log based on level
        if level == logging.DEBUG:
            self.logger.debug(message)
        elif level == logging.INFO:
            self.logger.info(message)
        elif level == logging.WARNING:
            self.logger.warning(message)
        elif level == logging.ERROR:
            self.logger.error(message)
        elif level == logging.CRITICAL:
            self.logger.critical(message)
        else:
            # Default to info if level is unrecognized
            self.logger.info(message)

def get_emoji_logger(log_level=logging.INFO):
    """
    Convenience function to get an EmojiLogger instance.
    
    :param log_level: Logging level (default is logging.INFO)
    :return: EmojiLogger instance
    """
    return EmojiLogger(log_level)