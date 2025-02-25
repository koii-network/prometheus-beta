import os
import json
import pytest
from src.multiple_choice_logger import log_multiple_choice_responses

def test_log_multiple_choice_responses_basic():
    """Test basic logging functionality"""
    # Temporary log file for testing
    test_log_file = 'test_responses.json'
    
    # Sample responses
    responses = [
        {
            'question_id': '001',
            'question_text': 'What is the capital of France?',
            'selected_option': 'Paris'
        }
    ]
    
    # Log responses
    result = log_multiple_choice_responses(responses, test_log_file)
    
    # Verify logging was successful
    assert result is True
    
    # Check file contents
    with open(test_log_file, 'r') as f:
        logged_responses = json.load(f)
    
    assert len(logged_responses) == 1
    assert logged_responses[0]['question_id'] == '001'
    assert logged_responses[0]['selected_option'] == 'Paris'
    
    # Clean up
    os.remove(test_log_file)

def test_log_multiple_responses():
    """Test logging multiple responses"""
    test_log_file = 'test_multiple_responses.json'
    
    responses = [
        {
            'question_id': '001',
            'question_text': 'What is the capital of France?',
            'selected_option': 'Paris'
        },
        {
            'question_id': '002',
            'question_text': 'What is 2+2?',
            'selected_option': '4'
        }
    ]
    
    result = log_multiple_choice_responses(responses, test_log_file)
    
    assert result is True
    
    with open(test_log_file, 'r') as f:
        logged_responses = json.load(f)
    
    assert len(logged_responses) == 2
    
    # Clean up
    os.remove(test_log_file)

def test_invalid_input_raises_error():
    """Test that invalid inputs raise appropriate errors"""
    # Test non-list input
    with pytest.raises(ValueError, match="Responses must be a list of dictionaries"):
        log_multiple_choice_responses("not a list")
    
    # Test invalid response dictionary
    with pytest.raises(ValueError, match="Each response must be a dictionary"):
        log_multiple_choice_responses([1, 2, 3])
    
    # Test missing keys
    with pytest.raises(ValueError, match="Missing required key"):
        log_multiple_choice_responses([{
            'question_text': 'Test',
            'selected_option': 'A'
        }])

def test_append_to_existing_log():
    """Test appending to an existing log file"""
    test_log_file = 'test_append_responses.json'
    
    # Initial responses
    initial_responses = [
        {
            'question_id': '001',
            'question_text': 'First question',
            'selected_option': 'Option A'
        }
    ]
    
    # Log initial responses
    log_multiple_choice_responses(initial_responses, test_log_file)
    
    # Add more responses
    additional_responses = [
        {
            'question_id': '002',
            'question_text': 'Second question',
            'selected_option': 'Option B'
        }
    ]
    
    # Log additional responses
    result = log_multiple_choice_responses(additional_responses, test_log_file)
    
    assert result is True
    
    # Verify both sets of responses are in the file
    with open(test_log_file, 'r') as f:
        logged_responses = json.load(f)
    
    assert len(logged_responses) == 2
    assert logged_responses[0]['question_id'] == '001'
    assert logged_responses[1]['question_id'] == '002'
    
    # Clean up
    os.remove(test_log_file)