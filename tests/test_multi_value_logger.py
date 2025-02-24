import logging
import pytest
from unittest.mock import Mock

from src.multi_value_logger import log_multiple_values

def test_log_multiple_values_default():
    """Test logging multiple values with default settings"""
    mock_logger = Mock(spec=logging.Logger)
    log_multiple_values(1, "hello", 3.14, logger=mock_logger)
    mock_logger.info.assert_called_once_with("1 hello 3.14")

def test_log_multiple_values_custom_level():
    """Test logging with different log levels"""
    mock_logger = Mock(spec=logging.Logger)
    log_multiple_values("error", "test", level="error", logger=mock_logger)
    mock_logger.error.assert_called_once_with("error test")

def test_log_multiple_values_mixed_types():
    """Test logging values of different types"""
    mock_logger = Mock(spec=logging.Logger)
    log_multiple_values(1, "string", [1, 2, 3], {"key": "value"}, logger=mock_logger)
    mock_logger.info.assert_called_once_with("1 string [1, 2, 3] {'key': 'value'}")

def test_invalid_log_level():
    """Test that an invalid log level raises a ValueError"""
    with pytest.raises(ValueError, match="Invalid logging level"):
        log_multiple_values("test", level="invalid_level")

def test_invalid_logger():
    """Test that an invalid logger raises a TypeError"""
    with pytest.raises(TypeError, match="Logger must be a valid logging.Logger instance"):
        log_multiple_values("test", logger="not a logger")

def test_log_multiple_values_no_values():
    """Test logging with no values"""
    mock_logger = Mock(spec=logging.Logger)
    log_multiple_values(logger=mock_logger)
    mock_logger.info.assert_called_once_with("")