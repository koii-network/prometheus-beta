class FontLogger:
    """
    A logging utility that supports different font sizes for output.
    
    Supports font sizes from 1 (smallest) to 6 (largest).
    """
    
    @staticmethod
    def log(message, size=3):
        """
        Log a message with a specified font size.
        
        Args:
            message (str): The message to log
            size (int, optional): Font size from 1-6. Defaults to 3.
        
        Raises:
            ValueError: If size is not between 1 and 6
        """
        # Validate font size
        if not isinstance(size, int) or size < 1 or size > 6:
            raise ValueError("Font size must be an integer between 1 and 6")
        
        # Simulate font size logging by using HTML-like tags
        font_sizes = {
            1: "small",
            2: "medium-small", 
            3: "medium",
            4: "medium-large",
            5: "large", 
            6: "extra-large"
        }
        
        # Format the output with the corresponding font size
        formatted_message = f"[{font_sizes[size]} font] {message}"
        print(formatted_message)
        
        return formatted_message