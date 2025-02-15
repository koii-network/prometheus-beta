import json
import os
from datetime import datetime

def log_multiple_choice_response(question, choices, user_response, log_file='user_responses.json'):
    """
    Log a user's response to a multiple-choice question.
    
    Args:
        question (str): The multiple-choice question text
        choices (list): List of possible answer choices
        user_response (str): The user's selected response
        log_file (str, optional): Path to the log file. Defaults to 'user_responses.json'
    
    Raises:
        ValueError: If the user response is not in the list of choices
    """
    # Validate user response
    if user_response not in choices:
        raise ValueError(f"Invalid response. Must be one of {choices}")
    
    # Prepare log entry
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'question': question,
        'choices': choices,
        'user_response': user_response
    }
    
    # Ensure logs directory exists
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    # Read existing log entries or create new list
    try:
        with open(log_file, 'r') as f:
            logs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []
    
    # Append new log entry
    logs.append(log_entry)
    
    # Write updated logs
    with open(log_file, 'w') as f:
        json.dump(logs, f, indent=2)
    
    return log_entry