import pytest
from src.multi_line_logger import log_multiline

def test_single_string_message():
    result = log_multiline("Hello, world!")
    expected_lines = [
        '==================================================',
        'Hello, world!',
        '=================================================='
    ]
    assert result.split('\n') == expected_lines

def test_multiple_messages():
    messages = ["First line", "Second line", "Third line"]
    result = log_multiline(messages)
    expected_lines = [
        '==================================================',
        'First line',
        '==================================================',
        'Second line',
        '==================================================',
        'Third line',
        '=================================================='
    ]
    assert result.split('\n') == expected_lines

def test_custom_separator():
    result = log_multiline("Custom separator", separator='-')
    expected_lines = [
        '--------------------------------------------------',
        'Custom separator',
        '--------------------------------------------------'
    ]
    assert result.split('\n') == expected_lines

def test_custom_line_length():
    result = log_multiline("Custom length", separator='*', line_length=10)
    expected_lines = [
        '**********',
        'Custom length',
        '**********'
    ]
    assert result.split('\n') == expected_lines

def test_invalid_separator():
    with pytest.raises(ValueError, match="Separator must be a single character"):
        log_multiline("Invalid", separator='too long')

def test_invalid_line_length():
    with pytest.raises(ValueError, match="Line length must be a positive integer"):
        log_multiline("Invalid", line_length=-5)

def test_numeric_message():
    result = log_multiline(42)
    expected_lines = [
        '==================================================',
        '42',
        '=================================================='
    ]
    assert result.split('\n') == expected_lines