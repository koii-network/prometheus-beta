import os
import json
import pytest
from src.user_response_logger import log_multiple_choice_responses

def test_successful_logging(tmp_path):
    """Test logging a valid user response"""
    log_file = os.path.join(tmp_path, 'responses.json')
    question = "What is your favorite color?"
    options = ["Red", "Blue", "Green"]
    user_response = "Blue"
    
    log_multiple_choice_responses(question, options, user_response, log_file)
    
    # Verify file was created and contains correct data
    with open(log_file, 'r') as f:
        logs = json.load(f)
    
    assert len(logs) == 1
    assert logs[0]['question'] == question
    assert logs[0]['options'] == options
    assert logs[0]['user_response'] == user_response

def test_invalid_response():
    """Test that invalid response raises ValueError"""
    with pytest.raises(ValueError, match="Invalid response"):
        log_multiple_choice_responses(
            "What is your favorite color?", 
            ["Red", "Blue", "Green"], 
            "Yellow"
        )

def test_multiple_log_entries(tmp_path):
    """Test logging multiple responses to the same file"""
    log_file = os.path.join(tmp_path, 'multiple_responses.json')
    
    log_multiple_choice_responses(
        "First question", 
        ["Option1", "Option2"], 
        "Option1", 
        log_file
    )
    
    log_multiple_choice_responses(
        "Second question", 
        ["A", "B", "C"], 
        "B", 
        log_file
    )
    
    # Verify both entries are in the file
    with open(log_file, 'r') as f:
        logs = json.load(f)
    
    assert len(logs) == 2
    assert logs[0]['question'] == "First question"
    assert logs[1]['question'] == "Second question"

def test_default_log_file_creation():
    """Test logging to default file"""
    # Ensure no existing file interferes
    if os.path.exists('user_responses.json'):
        os.remove('user_responses.json')
    
    log_multiple_choice_responses(
        "Test question", 
        ["Yes", "No"], 
        "Yes"
    )
    
    assert os.path.exists('user_responses.json')
    os.remove('user_responses.json')  # Clean up