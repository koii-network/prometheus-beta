import logging
import sys
import os

def log_user_input():
    """
    Capture and log user input from the command line.
    
    Returns:
        str: The logged user input
    """
    try:
        # Ensure logs directory exists
        os.makedirs('logs', exist_ok=True)
        
        # Configure logging
        logger = logging.getLogger('user_input_logger')
        logger.setLevel(logging.INFO)
        
        # Create file handler
        file_handler = logging.FileHandler('logs/user_input.log')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - User Input: %(message)s'))
        
        # Create console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter('%(asctime)s - User Input: %(message)s'))
        
        # Clear any existing handlers to prevent duplicate logging
        logger.handlers.clear()
        
        # Add handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        # Prompt and capture user input
        user_input = input("Please enter your input: ")
        
        # Log the input
        logger.info(user_input)
        
        return user_input
    
    except Exception as e:
        logging.error(f"Error logging user input: {e}")
        return None