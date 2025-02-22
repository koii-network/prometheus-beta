class EnhancedLogger:
    """
    A logging utility that supports different font sizes for output.
    
    Font sizes are represented as follows:
    - 'small': Minimal font size
    - 'normal': Default font size
    - 'large': Large font size
    - 'huge': Extra large font size
    """
    
    @staticmethod
    def log(message, font_size='normal'):
        """
        Log a message with specified font size.
        
        Args:
            message (str): The message to log
            font_size (str, optional): Size of the font. 
                Defaults to 'normal'.
                Supported sizes: 'small', 'normal', 'large', 'huge'
        
        Raises:
            ValueError: If an unsupported font size is provided
        """
        font_sizes = {
            'small': '\033[94m',   # Blue, smaller
            'normal': '\033[0m',   # Default
            'large': '\033[1m',    # Bold
            'huge': '\033[91m'     # Red, very prominent
        }
        
        if font_size not in font_sizes:
            raise ValueError(f"Unsupported font size: {font_size}. "
                             f"Supported sizes are: {list(font_sizes.keys())}")
        
        # Apply font size coloring/styling
        styled_message = f"{font_sizes[font_size]}{message}\033[0m"
        
        # Actually print the message
        print(styled_message)
        
        return styled_message