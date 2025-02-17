import logging
import sys
from datetime import datetime

def log_user_input():
    """
    Logs user input from the command line.
    
    Returns:
        str: The logged user input
    """
    try:
        # Configure logging
        logging.basicConfig(
            filename='user_input.log', 
            level=logging.INFO, 
            format='%(asctime)s - %(message)s'
        )
        
        # Prompt for input
        print("Enter your input (press Enter to submit):")
        user_input = input().strip()
        
        # Log the input
        if user_input:
            logging.info(f"User input: {user_input}")
            return user_input
        else:
            logging.warning("Empty input received")
            return ""
    
    except Exception as e:
        logging.error(f"Error logging user input: {str(e)}")
        raise