import os
import json
import pytest
from src.multiple_choice_logger import log_multiple_choice_responses

def test_log_multiple_choice_responses():
    # Prepare test data
    questions = [
        {
            'text': 'What is the capital of France?',
            'options': ['Paris', 'London', 'Berlin', 'Rome']
        },
        {
            'text': 'Which is the largest planet?',
            'options': ['Mars', 'Jupiter', 'Saturn', 'Neptune']
        }
    ]
    responses = ['Paris', 'Jupiter']
    
    # Temporary log file for testing
    test_log_file = 'test_user_responses.json'
    
    # Call the function
    log_multiple_choice_responses(questions, responses, test_log_file)
    
    # Verify the log file was created
    assert os.path.exists(test_log_file)
    
    # Read and validate log content
    with open(test_log_file, 'r') as f:
        logs = json.load(f)
    
    assert len(logs) == 2
    assert logs[0]['question'] == 'What is the capital of France?'
    assert logs[0]['selected_response'] == 'Paris'
    assert logs[1]['question'] == 'Which is the largest planet?'
    assert logs[1]['selected_response'] == 'Jupiter'

def test_log_multiple_choice_responses_mismatched_length():
    # Test case with mismatched questions and responses
    questions = [{'text': 'Test Question'}]
    responses = ['Response1', 'Response2']
    
    with pytest.raises(ValueError, match="Number of questions and responses must be the same"):
        log_multiple_choice_responses(questions, responses)

def test_log_multiple_choice_responses_appends():
    # Test that logs are appended, not overwritten
    questions1 = [{'text': 'First Question', 'options': ['A', 'B']}]
    responses1 = ['A']
    
    questions2 = [{'text': 'Second Question', 'options': ['X', 'Y']}]
    responses2 = ['Y']
    
    test_log_file = 'test_append_responses.json'
    
    # First log
    log_multiple_choice_responses(questions1, responses1, test_log_file)
    
    # Second log
    log_multiple_choice_responses(questions2, responses2, test_log_file)
    
    # Verify both entries are present
    with open(test_log_file, 'r') as f:
        logs = json.load(f)
    
    assert len(logs) == 2
    assert logs[0]['question'] == 'First Question'
    assert logs[1]['question'] == 'Second Question'

def test_log_multiple_choice_responses_handles_missing_fields():
    # Test handling of questions with missing optional fields
    questions = [
        {'text': 'Incomplete Question'},
        {}
    ]
    responses = ['Answer1', 'Answer2']
    
    test_log_file = 'test_incomplete_questions.json'
    
    # Should not raise an exception
    log_multiple_choice_responses(questions, responses, test_log_file)
    
    # Verify logs
    with open(test_log_file, 'r') as f:
        logs = json.load(f)
    
    assert len(logs) == 2
    assert logs[0]['question'] == 'Incomplete Question'
    assert logs[1]['question'] == 'Unknown Question'