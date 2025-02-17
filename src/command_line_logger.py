import logging
import sys

def log_user_input():
    """
    Capture and log user input from the command line.
    
    Returns:
        str: The logged user input
    """
    try:
        # Configure logging
        logging.basicConfig(
            level=logging.INFO, 
            format='%(asctime)s - User Input: %(message)s',
            handlers=[
                logging.FileHandler('user_input.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        
        # Prompt and capture user input
        user_input = input("Please enter your input: ")
        
        # Log the input
        logging.info(user_input)
        
        return user_input
    
    except Exception as e:
        logging.error(f"Error logging user input: {e}")
        return None