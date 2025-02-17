import os
import json
import pytest
from src.multiple_choice_logger import log_multiple_choice_responses

def test_log_multiple_choice_responses():
    # Prepare test data
    questions = [
        {
            'text': 'What is the capital of France?',
            'choices': ['London', 'Berlin', 'Paris', 'Madrid']
        },
        {
            'text': 'Which programming language is this?',
            'choices': ['Python', 'Java', 'C++', 'JavaScript']
        }
    ]
    responses = ['Paris', 'Python']
    test_log_file = 'test_mc_responses.json'
    
    # Call the function
    log_multiple_choice_responses(questions, responses, test_log_file)
    
    # Verify the log file was created and contains correct data
    assert os.path.exists(test_log_file)
    
    with open(test_log_file, 'r') as f:
        logs = json.load(f)
    
    assert len(logs) == 2
    assert logs[0]['question'] == 'What is the capital of France?'
    assert logs[0]['user_response'] == 'Paris'
    assert logs[1]['question'] == 'Which programming language is this?'
    assert logs[1]['user_response'] == 'Python'
    
    # Clean up
    os.remove(test_log_file)

def test_log_multiple_choice_responses_mismatched_input():
    questions = [{'text': 'Q1'}, {'text': 'Q2'}]
    responses = ['A1']
    
    with pytest.raises(ValueError, match="Number of questions and responses must be the same."):
        log_multiple_choice_responses(questions, responses)

def test_log_multiple_choice_responses_append():
    questions1 = [{'text': 'First Question', 'choices': ['A', 'B']}]
    responses1 = ['A']
    questions2 = [{'text': 'Second Question', 'choices': ['X', 'Y']}]
    responses2 = ['X']
    test_log_file = 'test_append_responses.json'
    
    # First log
    log_multiple_choice_responses(questions1, responses1, test_log_file)
    log_multiple_choice_responses(questions2, responses2, test_log_file)
    
    # Verify both logs are present
    with open(test_log_file, 'r') as f:
        logs = json.load(f)
    
    assert len(logs) == 2
    assert logs[0]['question'] == 'First Question'
    assert logs[1]['question'] == 'Second Question'
    
    # Clean up
    os.remove(test_log_file)