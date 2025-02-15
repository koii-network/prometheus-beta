import pytest
import logging
from src.loop_logger import log_loop_values

def test_log_loop_values_list(caplog):
    caplog.set_level(logging.INFO)
    
    # Test with a list
    result = log_loop_values([1, 2, 3])
    
    assert result == [1, 2, 3]
    assert len(caplog.records) == 3
    assert "Loop iteration 1: 1" in caplog.text
    assert "Loop iteration 2: 2" in caplog.text
    assert "Loop iteration 3: 3" in caplog.text

def test_log_loop_values_tuple(caplog):
    caplog.set_level(logging.INFO)
    
    # Test with a tuple
    result = log_loop_values(('a', 'b', 'c'))
    
    assert result == ['a', 'b', 'c']
    assert len(caplog.records) == 3
    assert "Loop iteration 1: a" in caplog.text
    assert "Loop iteration 2: b" in caplog.text
    assert "Loop iteration 3: c" in caplog.text

def test_log_loop_values_set(caplog):
    caplog.set_level(logging.INFO)
    
    # Test with a set
    result = log_loop_values({10, 20, 30})
    
    assert set(result) == {10, 20, 30}
    assert len(caplog.records) == 3

def test_log_loop_values_custom_log_level(caplog):
    caplog.set_level(logging.DEBUG)
    
    # Test with a custom log level
    result = log_loop_values([1, 2, 3], log_level=logging.DEBUG)
    
    assert result == [1, 2, 3]
    assert len(caplog.records) == 3
    assert caplog.records[0].levelno == logging.DEBUG

def test_log_loop_values_invalid_input():
    # Test with non-iterable input
    with pytest.raises(TypeError, match="Input must be an iterable"):
        log_loop_values(42)

def test_log_loop_values_empty_iterable(caplog):
    # Test with an empty iterable
    result = log_loop_values([])
    
    assert result == []
    assert len(caplog.records) == 0