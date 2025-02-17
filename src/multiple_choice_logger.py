import json
import os
from typing import List, Dict, Any

def log_multiple_choice_responses(questions: List[Dict[str, Any]], user_responses: List[str], log_file: str = 'mc_responses.json') -> None:
    """
    Log user responses to multiple-choice questions.
    
    Args:
        questions (List[Dict[str, Any]]): List of multiple-choice question dictionaries.
        user_responses (List[str]): List of user's selected responses.
        log_file (str, optional): Path to the log file. Defaults to 'mc_responses.json'.
    
    Raises:
        ValueError: If the number of questions and responses don't match.
    """
    # Validate input
    if len(questions) != len(user_responses):
        raise ValueError("Number of questions and responses must be the same.")
    
    # Prepare log entries
    log_entries = []
    for question, response in zip(questions, user_responses):
        log_entry = {
            'question': question.get('text', 'Unknown Question'),
            'choices': question.get('choices', []),
            'user_response': response
        }
        log_entries.append(log_entry)
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(log_file) or '.', exist_ok=True)
    
    # Write or append to log file
    try:
        if os.path.exists(log_file):
            with open(log_file, 'r+') as f:
                try:
                    existing_logs = json.load(f)
                except json.JSONDecodeError:
                    existing_logs = []
                
                existing_logs.extend(log_entries)
                f.seek(0)
                json.dump(existing_logs, f, indent=2)
                f.truncate()
        else:
            with open(log_file, 'w') as f:
                json.dump(log_entries, f, indent=2)
    except IOError as e:
        raise IOError(f"Error writing to log file: {e}")