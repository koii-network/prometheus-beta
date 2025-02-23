import logging
import pytest
from src.currency_logger import log_formatted_currency

# Configure logging to capture log messages
class LogCapture:
    def __init__(self):
        self.log_messages = []
        self.handler = logging.StreamHandler()
        self.formatter = logging.Formatter('%(message)s')
        self.handler.setFormatter(self.formatter)
        
    def __enter__(self):
        self.logger = logging.getLogger()
        self.logger.addHandler(self.handler)
        self.logger.setLevel(logging.INFO)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.logger.removeHandler(self.handler)

def test_log_formatted_currency_default():
    with LogCapture() as log:
        result = log_formatted_currency(123.45)
        assert result == '$123.45'

def test_log_formatted_currency_specific_currency():
    with LogCapture() as log:
        result = log_formatted_currency(678.90, currency='EUR')
        assert result == '€678.90'

def test_log_formatted_currency_custom_currency():
    with LogCapture() as log:
        result = log_formatted_currency(456.78, currency='BRL')
        assert result == 'BRL456.78'

def test_log_formatted_currency_int():
    with LogCapture() as log:
        result = log_formatted_currency(100)
        assert result == '$100.00'

def test_log_formatted_currency_invalid_type():
    with pytest.raises(TypeError):
        log_formatted_currency('not a number')

def test_log_formatted_currency_negative():
    with pytest.raises(ValueError):
        log_formatted_currency(-50)

def test_log_formatted_currency_empty_currency():
    with pytest.raises(ValueError):
        log_formatted_currency(100, currency='')

def test_log_formatted_currency_custom_log_level():
    with LogCapture() as log:
        result = log_formatted_currency(250.75, log_level=logging.DEBUG)
        assert result == '$250.75'