import pytest
import logging
from unittest.mock import patch, Mock
from src.readline_logger import log_interactive_prompt

def test_log_interactive_prompt_basic():
    """Test basic functionality without logging."""
    with patch('builtins.input', return_value='test input'):
        result = log_interactive_prompt("Enter something: ")
        assert result == 'test input'

def test_log_interactive_prompt_with_logger():
    """Test prompt logging with a mock logger."""
    mock_logger = Mock(spec=logging.Logger)
    
    with patch('builtins.input', return_value='logged input'):
        result = log_interactive_prompt(
            "Enter something: ", 
            logger=mock_logger, 
            log_level=logging.INFO
        )
        
        assert result == 'logged input'
        
        # Check logger was called twice (for prompt and input)
        assert mock_logger.log.call_count == 2
        
        # Verify first call is the prompt
        first_call = mock_logger.log.call_args_list[0]
        assert first_call[0][0] == logging.INFO
        assert "Prompt: Enter something:" in first_call[0][1]
        
        # Verify second call is the input
        second_call = mock_logger.log.call_args_list[1]
        assert second_call[0][0] == logging.INFO
        assert "User input: logged input" in second_call[0][1]

def test_log_interactive_prompt_with_validator():
    """Test input validation."""
    def valid_input(s: str) -> bool:
        return len(s) > 3
    
    with patch('builtins.input', return_value='good'):
        result = log_interactive_prompt(
            "Enter something long: ", 
            validator=valid_input
        )
        assert result == 'good'
    
    with patch('builtins.input', return_value='bad'):
        with pytest.raises(ValueError, match="Input failed validation"):
            log_interactive_prompt(
                "Enter something long: ", 
                validator=valid_input
            )

def test_log_interactive_prompt_input_error():
    """Test error handling during input."""
    mock_logger = Mock(spec=logging.Logger)
    
    with patch('builtins.input', side_effect=KeyboardInterrupt):
        with pytest.raises(KeyboardInterrupt):
            log_interactive_prompt(
                "Enter something: ", 
                logger=mock_logger
            )
        
        # Verify error was logged
        mock_logger.error.assert_called_once()