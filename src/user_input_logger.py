import logging
import sys
import os
from datetime import datetime

def log_user_input():
    """
    Logs user input from the command line.
    
    Returns:
        str: The logged user input
    """
    try:
        # Configure logging with an absolute path
        log_dir = '/app/repos/repo_11'
        os.makedirs(log_dir, exist_ok=True)
        log_path = os.path.join(log_dir, 'user_input.log')
        
        logging.basicConfig(
            filename=log_path, 
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