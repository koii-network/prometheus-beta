import json
import os
from typing import List, Dict, Any

def log_multiple_choice_responses(questions: List[Dict[str, Any]], responses: List[str], log_file: str = 'user_responses.json') -> None:
    """
    Log user responses to multiple-choice questions.
    
    Args:
        questions (List[Dict[str, Any]]): List of question dictionaries with details.
        responses (List[str]): List of user's selected responses.
        log_file (str, optional): Path to the log file. Defaults to 'user_responses.json'.
    
    Raises:
        ValueError: If the number of questions and responses do not match.
    """
    # Validate input
    if len(questions) != len(responses):
        raise ValueError("Number of questions and responses must be the same")
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(log_file) or '.', exist_ok=True)
    
    # Prepare log entries
    log_entries = []
    for question, response in zip(questions, responses):
        log_entry = {
            'question': question.get('text', 'Unknown Question'),
            'options': question.get('options', []),
            'selected_response': response
        }
        log_entries.append(log_entry)
    
    # Read existing log file or start with empty list
    try:
        with open(log_file, 'r') as f:
            existing_logs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_logs = []
    
    # Append new entries
    existing_logs.extend(log_entries)
    
    # Write updated logs
    with open(log_file, 'w') as f:
        json.dump(existing_logs, f, indent=2)