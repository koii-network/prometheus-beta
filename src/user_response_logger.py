import os
import json
from typing import List, Dict, Any

class UserResponseLogger:
    def __init__(self, log_dir: str = 'logs'):
        """
        Initialize the UserResponseLogger with a specified log directory.
        
        :param log_dir: Directory to store log files, defaults to 'logs'
        """
        self.log_dir = log_dir
        # Ensure log directory exists
        os.makedirs(self.log_dir, exist_ok=True)
    
    def log_multiple_choice_response(self, 
                                     question: str, 
                                     options: List[str], 
                                     selected_option: str, 
                                     user_id: str = 'anonymous') -> None:
        """
        Log a user's response to a multiple-choice question.
        
        :param question: The text of the multiple-choice question
        :param options: List of available options
        :param selected_option: The option selected by the user
        :param user_id: Optional identifier for the user, defaults to 'anonymous'
        :raises ValueError: If selected option is not in the list of options
        """
        # Validate selected option
        if selected_option not in options:
            raise ValueError(f"Selected option '{selected_option}' is not in the list of options.")
        
        # Prepare log entry
        log_entry = {
            'user_id': user_id,
            'question': question,
            'options': options,
            'selected_option': selected_option,
            'timestamp': os.path.getmtime
        }
        
        # Generate a unique log filename
        log_filename = os.path.join(self.log_dir, f'{user_id}_{hash(question)}.json')
        
        # Write log entry to file
        with open(log_filename, 'w') as log_file:
            json.dump(log_entry, log_file, indent=2)
    
    def get_user_responses(self, user_id: str = 'anonymous') -> List[Dict[str, Any]]:
        """
        Retrieve all logged responses for a specific user.
        
        :param user_id: User identifier to filter logs
        :return: List of logged responses for the user
        """
        user_responses = []
        
        # Iterate through log files
        for filename in os.listdir(self.log_dir):
            if filename.startswith(f'{user_id}_'):
                filepath = os.path.join(self.log_dir, filename)
                with open(filepath, 'r') as log_file:
                    user_responses.append(json.load(log_file))
        
        return user_responses