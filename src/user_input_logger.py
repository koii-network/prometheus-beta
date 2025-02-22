import logging
import sys

def log_user_input():
    """
    Log user input from the command line.
    
    Returns:
        str: The logged user input
    """
    # Configure logging 
    logging.basicConfig(
        filename='user_input.log', 
        level=logging.INFO, 
        format='%(asctime)s - %(message)s'
    )
    
    try:
        # Prompt for and get user input
        user_input = input("Please enter your input: ")
        
        # Log the input
        logging.info(f"User input: {user_input}")
        
        return user_input
    
    except Exception as e:
        # Log any errors that occur during input
        logging.error(f"Error capturing user input: {e}")
        raise