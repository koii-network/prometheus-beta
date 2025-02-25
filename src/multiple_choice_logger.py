import json
import os
from typing import List, Dict, Any

def log_multiple_choice_responses(responses: List[Dict[str, Any]], log_file: str = 'responses.json') -> bool:
    """
    Log user responses to multiple-choice questions to a JSON file.

    Args:
        responses (List[Dict[str, Any]]): A list of dictionaries containing response data.
        Each response should have keys:
        - 'question_id': Unique identifier for the question
        - 'question_text': Text of the question
        - 'selected_option': The option selected by the user
        - 'timestamp': Optional timestamp of the response

        log_file (str, optional): Path to the log file. Defaults to 'responses.json'.

    Returns:
        bool: True if logging was successful, False otherwise.

    Raises:
        ValueError: If responses are invalid or missing required keys.
        IOError: If there are issues writing to the log file.
    """
    # Validate input
    if not isinstance(responses, list):
        raise ValueError("Responses must be a list of dictionaries")
    
    # Validate each response
    for response in responses:
        if not isinstance(response, dict):
            raise ValueError("Each response must be a dictionary")
        
        # Check for required keys
        required_keys = ['question_id', 'question_text', 'selected_option']
        for key in required_keys:
            if key not in response:
                raise ValueError(f"Missing required key: {key}")
    
    # Ensure log directory exists
    os.makedirs(os.path.dirname(log_file) or '.', exist_ok=True)
    
    try:
        # Read existing responses if file exists
        if os.path.exists(log_file):
            with open(log_file, 'r') as f:
                existing_responses = json.load(f)
        else:
            existing_responses = []
        
        # Append new responses
        existing_responses.extend(responses)
        
        # Write updated responses
        with open(log_file, 'w') as f:
            json.dump(existing_responses, f, indent=2)
        
        return True
    except (IOError, json.JSONDecodeError) as e:
        # Log specific error or re-raise
        print(f"Error logging responses: {e}")
        return False