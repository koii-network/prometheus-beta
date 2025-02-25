import os
import json
import pytest
from src.multiple_choice_logger import MultipleChoiceLogger

def test_logger_initialization(tmp_path):
    """Test logger initialization creates file if not exists."""
    log_file = os.path.join(tmp_path, 'responses.json')
    logger = MultipleChoiceLogger(log_file)
    
    assert os.path.exists(log_file)
    
    with open(log_file, 'r') as f:
        initial_content = json.load(f)
    assert initial_content == []

def test_log_response(tmp_path):
    """Test logging a valid response."""
    log_file = os.path.join(tmp_path, 'responses.json')
    logger = MultipleChoiceLogger(log_file)
    
    question = "What is the capital of France?"
    choices = ["London", "Berlin", "Paris", "Madrid"]
    selected_choice = "Paris"
    user_id = "user123"
    
    logger.log_response(question, choices, selected_choice, user_id)
    
    with open(log_file, 'r') as f:
        responses = json.load(f)
    
    assert len(responses) == 1
    assert responses[0]['question'] == question
    assert responses[0]['choices'] == choices
    assert responses[0]['selected_choice'] == selected_choice
    assert responses[0]['user_id'] == user_id

def test_log_response_with_index(tmp_path):
    """Test logging a response using choice index."""
    log_file = os.path.join(tmp_path, 'responses.json')
    logger = MultipleChoiceLogger(log_file)
    
    question = "What is the capital of France?"
    choices = ["London", "Berlin", "Paris", "Madrid"]
    selected_choice_index = 2
    user_id = "user123"
    
    logger.log_response(question, choices, selected_choice_index, user_id)
    
    with open(log_file, 'r') as f:
        responses = json.load(f)
    
    assert len(responses) == 1
    assert responses[0]['selected_choice'] == "Paris"

def test_multiple_responses(tmp_path):
    """Test logging multiple responses."""
    log_file = os.path.join(tmp_path, 'responses.json')
    logger = MultipleChoiceLogger(log_file)
    
    logger.log_response("Q1", ["A", "B", "C"], "A", "user1")
    logger.log_response("Q2", ["X", "Y", "Z"], "Y", "user2")
    
    with open(log_file, 'r') as f:
        responses = json.load(f)
    
    assert len(responses) == 2

def test_get_responses_by_user_id(tmp_path):
    """Test retrieving responses for a specific user."""
    log_file = os.path.join(tmp_path, 'responses.json')
    logger = MultipleChoiceLogger(log_file)
    
    logger.log_response("Q1", ["A", "B", "C"], "A", "user1")
    logger.log_response("Q2", ["X", "Y", "Z"], "Y", "user2")
    logger.log_response("Q3", ["P", "Q", "R"], "Q", "user1")
    
    user1_responses = logger.get_responses("user1")
    assert len(user1_responses) == 2
    assert all(resp['user_id'] == "user1" for resp in user1_responses)

def test_clear_log(tmp_path):
    """Test clearing the log."""
    log_file = os.path.join(tmp_path, 'responses.json')
    logger = MultipleChoiceLogger(log_file)
    
    logger.log_response("Q1", ["A", "B", "C"], "A", "user1")
    logger.clear_log()
    
    with open(log_file, 'r') as f:
        responses = json.load(f)
    
    assert len(responses) == 0

def test_invalid_inputs(tmp_path):
    """Test error handling for invalid inputs."""
    log_file = os.path.join(tmp_path, 'responses.json')
    logger = MultipleChoiceLogger(log_file)
    
    # Empty question
    with pytest.raises(ValueError, match="Question cannot be empty"):
        logger.log_response("", ["A", "B"], "A")
    
    # Empty choices
    with pytest.raises(ValueError, match="Choices list cannot be empty"):
        logger.log_response("Q1", [], "A")
    
    # Invalid choice
    with pytest.raises(ValueError, match="Selected choice must be one of"):
        logger.log_response("Q1", ["A", "B"], "C")
    
    # Out of range index
    with pytest.raises(ValueError, match="Invalid choice index"):
        logger.log_response("Q1", ["A", "B"], 2)

def test_optional_user_id(tmp_path):
    """Test logging response without user ID."""
    log_file = os.path.join(tmp_path, 'responses.json')
    logger = MultipleChoiceLogger(log_file)
    
    logger.log_response("Q1", ["A", "B", "C"], "A")
    
    with open(log_file, 'r') as f:
        responses = json.load(f)
    
    assert responses[0]['user_id'] is None