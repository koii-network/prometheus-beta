import json
import os
from typing import List, Dict, Any

def log_multiple_choice_responses(question: str, options: List[str], user_response: str, log_file: str = 'user_responses.json') -> None:
    """
    Log user responses to multiple-choice questions.
    
    Args:
        question (str): The text of the multiple-choice question
        options (List[str]): List of available options for the question
        user_response (str): The user's selected response
        log_file (str, optional): Path to the JSON log file. Defaults to 'user_responses.json'
    
    Raises:
        ValueError: If the user response is not in the list of options
    """
    # Validate user response
    if user_response not in options:
        raise ValueError(f"Invalid response. Must be one of: {options}")
    
    # Ensure log directory exists
    os.makedirs(os.path.dirname(log_file) or '.', exist_ok=True)
    
    # Read existing log or create new
    try:
        with open(log_file, 'r') as f:
            logs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []
    
    # Create log entry
    log_entry = {
        'question': question,
        'options': options,
        'user_response': user_response,
        'timestamp': os.path.getmtime(log_file) if os.path.exists(log_file) else None
    }
    
    # Append new log entry
    logs.append(log_entry)
    
    # Write updated logs
    with open(log_file, 'w') as f:
        json.dump(logs, f, indent=2)