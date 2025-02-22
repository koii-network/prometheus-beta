import readline
import logging
import os
from typing import Optional, List

class ReadlinePromptLogger:
    """
    A class to log interactive prompts using readline history.
    """
    def __init__(self, log_file: Optional[str] = None, log_level: int = logging.INFO):
        """
        Initialize the ReadlinePromptLogger.
        
        :param log_file: Path to the log file. If None, uses a default log file.
        :param log_level: Logging level (default is logging.INFO)
        """
        # Ensure src directory exists
        os.makedirs('logs', exist_ok=True)
        
        # Set up logging
        self.log_file = log_file or 'logs/readline_prompts.log'
        self.logger = logging.getLogger('readline_prompt_logger')
        self.logger.setLevel(log_level)
        
        # Create file handler
        file_handler = logging.FileHandler(self.log_file)
        file_handler.setLevel(log_level)
        
        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        file_handler.setFormatter(formatter)
        
        # Add handler to logger
        self.logger.addHandler(file_handler)
    
    def log_prompt(self, prompt: str) -> str:
        """
        Log the prompt and capture the user's response.
        
        :param prompt: The prompt to display and log
        :return: The user's input
        """
        # Log the prompt
        self.logger.info(f"PROMPT: {prompt}")
        
        # Get user input
        try:
            user_input = input(prompt)
            
            # Log the user's input 
            self.logger.info(f"RESPONSE: {user_input}")
            
            return user_input
        except Exception as e:
            self.logger.error(f"Error during prompt: {str(e)}")
            raise
    
    def get_prompt_history(self, limit: Optional[int] = None) -> List[str]:
        """
        Retrieve readline history.
        
        :param limit: Maximum number of history entries to return
        :return: List of readline history entries
        """
        # Get history
        history = []
        for i in range(readline.get_current_history_length()):
            history.append(readline.get_history_item(i + 1))
        
        # Return limited history if specified
        return history[:limit] if limit is not None else history
    
    def clear_log(self):
        """
        Clear the log file.
        """
        try:
            open(self.log_file, 'w').close()
            self.logger.info("Log file cleared.")
        except Exception as e:
            self.logger.error(f"Error clearing log file: {str(e)}")