import logging
import pytest
from src.multi_logger import log_multiple

class TestMultiLogger:
    def setup_method(self):
        # Create a logger with a memory handler for testing
        self.logger = logging.getLogger('test_logger')
        self.logger.setLevel(logging.DEBUG)
        self.handler = logging.Handler()
        self.logger.addHandler(self.handler)
        
        # Capture log messages
        self.log_messages = []
        self.handler.emit = lambda record: self.log_messages.append(record.getMessage())

    def test_log_multiple_basic(self):
        log_multiple(self.logger, 'info', 'Hello', 'World', 123)
        assert len(self.log_messages) == 1
        assert self.log_messages[0] == 'Hello World 123'

    def test_log_multiple_custom_separator(self):
        log_multiple(self.logger, 'debug', 'Apple', 'Banana', 'Cherry', separator=', ')
        assert len(self.log_messages) == 1
        assert self.log_messages[0] == 'Apple, Banana, Cherry'

    def test_log_multiple_different_types(self):
        log_multiple(self.logger, 'warning', 42, 'test', [1,2,3], {'key': 'value'})
        assert len(self.log_messages) == 1
        assert self.log_messages[0] == '42 test [1, 2, 3] {\'key\': \'value\'}'

    def test_invalid_log_level(self):
        with pytest.raises(ValueError, match="Invalid log level"):
            log_multiple(self.logger, 'invalid_level', 'Test')

    def test_log_multiple_empty_values(self):
        log_multiple(self.logger, 'error')
        assert len(self.log_messages) == 1
        assert self.log_messages[0] == ''