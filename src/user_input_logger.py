import logging
import sys

def log_user_input():
    """
    Logs user input from the command line.
    
    Returns:
        str: The input received from the user
    """
    try:
        # Configure logging
        logging.basicConfig(
            filename='user_input.log', 
            level=logging.INFO, 
            format='%(asctime)s - %(message)s'
        )
        
        # Prompt and get user input
        user_input = input("Please enter your input: ")
        
        # Log the input
        logging.info(f"User input: {user_input}")
        
        return user_input
    
    except Exception as e:
        # Log any errors that occur
        logging.error(f"Error in logging user input: {e}")
        raise