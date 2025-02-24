import os
import pytest
import json
import shutil
from src.user_response_logger import UserResponseLogger

@pytest.fixture
def logger():
    # Create a temporary log directory for each test
    test_log_dir = 'test_logs'
    os.makedirs(test_log_dir, exist_ok=True)
    
    # Create logger with test log directory
    logger = UserResponseLogger(log_dir=test_log_dir)
    
    yield logger
    
    # Clean up test log directory after test
    shutil.rmtree(test_log_dir)

def test_log_multiple_choice_response(logger):
    question = "What is the capital of France?"
    options = ["London", "Paris", "Berlin", "Madrid"]
    selected_option = "Paris"
    
    # Log the response
    logger.log_multiple_choice_response(question, options, selected_option)
    
    # Check if log file was created
    log_files = os.listdir(logger.log_dir)
    assert len(log_files) == 1
    
    # Verify log file contents
    log_filepath = os.path.join(logger.log_dir, log_files[0])
    with open(log_filepath, 'r') as log_file:
        log_entry = json.load(log_file)
    
    assert log_entry['question'] == question
    assert log_entry['options'] == options
    assert log_entry['selected_option'] == selected_option
    assert log_entry['user_id'] == 'anonymous'

def test_log_multiple_choice_response_with_user_id(logger):
    question = "What is 2 + 2?"
    options = ["3", "4", "5", "6"]
    selected_option = "4"
    user_id = "user123"
    
    # Log the response with specific user ID
    logger.log_multiple_choice_response(question, options, selected_option, user_id)
    
    # Verify log file for specific user
    log_files = os.listdir(logger.log_dir)
    assert len(log_files) == 1
    assert log_files[0].startswith(f'{user_id}_')

def test_invalid_option_raises_error(logger):
    question = "Choose a color"
    options = ["Red", "Blue", "Green"]
    
    # Attempting to log an invalid option should raise ValueError
    with pytest.raises(ValueError, match="Selected option 'Yellow' is not in the list of options."):
        logger.log_multiple_choice_response(question, options, "Yellow")

def test_get_user_responses(logger):
    # Log multiple responses for a user
    user_id = "user456"
    questions = [
        ("Q1: What is 1 + 1?", ["1", "2", "3"], "2"),
        ("Q2: What is 2 * 3?", ["4", "5", "6"], "6")
    ]
    
    for question, options, selected_option in questions:
        logger.log_multiple_choice_response(question, options, selected_option, user_id)
    
    # Retrieve and verify user responses
    user_responses = logger.get_user_responses(user_id)
    assert len(user_responses) == 2
    
    # Check contents of retrieved responses
    response_questions = [resp['question'] for resp in user_responses]
    assert "Q1: What is 1 + 1?" in response_questions
    assert "Q2: What is 2 * 3?" in response_questions