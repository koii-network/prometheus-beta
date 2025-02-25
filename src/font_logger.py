class FontLogger:
    """
    A logging utility that supports different font sizes for output.
    """
    FONT_SIZES = {
        'small': '\033[92m',  # Green color for small
        'medium': '\033[93m', # Yellow color for medium 
        'large': '\033[91m',  # Red color for large
        'default': '\033[0m'  # Reset to default
    }

    @classmethod
    def log(cls, message, size='default'):
        """
        Log a message with specified font size/style.
        
        Args:
            message (str): The message to log
            size (str, optional): Font size/style. 
                Defaults to 'default'. 
                Options: 'small', 'medium', 'large', 'default'
        
        Returns:
            str: Formatted log message
        
        Raises:
            ValueError: If an invalid size is specified
        """
        # Validate size
        if size not in cls.FONT_SIZES:
            raise ValueError(f"Invalid font size. Choose from {list(cls.FONT_SIZES.keys())}")
        
        # Format and return the log message
        formatted_message = f"{cls.FONT_SIZES[size]}{message}{cls.FONT_SIZES['default']}"
        print(formatted_message)
        return formatted_message