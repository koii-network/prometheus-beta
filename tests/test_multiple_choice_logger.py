import os
import json
import pytest
import tempfile
from src.multiple_choice_logger import log_multiple_choice_response

def test_log_multiple_choice_response():
    # Create a temporary log file
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_log:
        temp_log_path = temp_log.name
    
    try:
        # Test logging a valid response
        question = "What is the capital of France?"
        choices = ["Paris", "London", "Berlin", "Madrid"]
        user_response = "Paris"
        
        result = log_multiple_choice_response(
            question, 
            choices, 
            user_response, 
            log_file=temp_log_path
        )
        
        # Verify the returned log entry
        assert result['question'] == question
        assert result['choices'] == choices
        assert result['user_response'] == user_response
        assert 'timestamp' in result
        
        # Read and verify the log file
        with open(temp_log_path, 'r') as f:
            logs = json.load(f)
        
        assert len(logs) == 1
        assert logs[0]['question'] == question
        assert logs[0]['user_response'] == user_response
    
    finally:
        # Clean up the temporary file
        os.unlink(temp_log_path)

def test_invalid_response_raises_error():
    # Test that an invalid response raises a ValueError
    question = "What is the capital of France?"
    choices = ["Paris", "London", "Berlin", "Madrid"]
    
    with pytest.raises(ValueError, match="Invalid response. Must be one of"):
        log_multiple_choice_response(
            question, 
            choices, 
            "Rome"  # Not in choices
        )

def test_multiple_log_entries():
    # Create a temporary log file
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_log:
        temp_log_path = temp_log.name
    
    try:
        # Log multiple entries
        log_multiple_choice_response(
            "Question 1", 
            ["A", "B", "C"], 
            "A", 
            log_file=temp_log_path
        )
        log_multiple_choice_response(
            "Question 2", 
            ["X", "Y", "Z"], 
            "Y", 
            log_file=temp_log_path
        )
        
        # Read and verify log file
        with open(temp_log_path, 'r') as f:
            logs = json.load(f)
        
        assert len(logs) == 2
        assert logs[0]['question'] == "Question 1"
        assert logs[1]['question'] == "Question 2"
    
    finally:
        # Clean up the temporary file
        os.unlink(temp_log_path)