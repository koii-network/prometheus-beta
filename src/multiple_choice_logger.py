import json
import os
from typing import Dict, List, Union, Optional

class MultipleChoiceLogger:
    """
    A class to log and manage user responses to multiple-choice questions.
    
    Attributes:
        log_file (str): Path to the JSON file where responses will be stored.
    """
    
    def __init__(self, log_file: str = 'user_responses.json'):
        """
        Initialize the MultipleChoiceLogger.
        
        Args:
            log_file (str, optional): Path to the log file. Defaults to 'user_responses.json'.
        """
        self.log_file = log_file
        
        # Ensure the directory exists
        os.makedirs(os.path.dirname(log_file) or '.', exist_ok=True)
        
        # Initialize the log file if it doesn't exist
        if not os.path.exists(log_file):
            with open(log_file, 'w') as f:
                json.dump([], f)
    
    def log_response(self, 
                     question: str, 
                     choices: List[str], 
                     selected_choice: Union[str, int], 
                     user_id: Optional[str] = None) -> None:
        """
        Log a user's response to a multiple-choice question.
        
        Args:
            question (str): The text of the multiple-choice question.
            choices (List[str]): List of available choices for the question.
            selected_choice (Union[str, int]): The choice selected by the user.
            user_id (Optional[str], optional): Identifier for the user. Defaults to None.
        
        Raises:
            ValueError: If the selected choice is not valid.
        """
        # Validate inputs
        if not question:
            raise ValueError("Question cannot be empty")
        
        if not choices:
            raise ValueError("Choices list cannot be empty")
        
        # Convert selected_choice to string if it's an index
        if isinstance(selected_choice, int):
            if selected_choice < 0 or selected_choice >= len(choices):
                raise ValueError(f"Invalid choice index. Must be between 0 and {len(choices)-1}")
            selected_choice = choices[selected_choice]
        
        # Validate selected choice is in the list of choices
        if selected_choice not in choices:
            raise ValueError(f"Selected choice must be one of: {choices}")
        
        # Read existing log
        with open(self.log_file, 'r') as f:
            responses = json.load(f)
        
        # Create response entry
        response_entry = {
            'question': question,
            'choices': choices,
            'selected_choice': selected_choice,
            'user_id': user_id
        }
        
        # Add to log
        responses.append(response_entry)
        
        # Write updated log
        with open(self.log_file, 'w') as f:
            json.dump(responses, f, indent=2)
    
    def get_responses(self, user_id: Optional[str] = None) -> List[Dict]:
        """
        Retrieve logged responses, optionally filtered by user_id.
        
        Args:
            user_id (Optional[str], optional): Filter responses by user ID. Defaults to None.
        
        Returns:
            List[Dict]: List of logged responses.
        """
        with open(self.log_file, 'r') as f:
            responses = json.load(f)
        
        if user_id is not None:
            return [resp for resp in responses if resp['user_id'] == user_id]
        
        return responses
    
    def clear_log(self) -> None:
        """
        Clear all logged responses.
        """
        with open(self.log_file, 'w') as f:
            json.dump([], f)