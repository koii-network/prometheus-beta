import os
import logging
import pytest
import tempfile
import time

from src.menu_logger import MenuLogger

class TestMenuLogger:
    @pytest.fixture
    def temp_log_file(self):
        """Create a temporary log file for testing."""
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
            temp_file_path = temp_file.name
        yield temp_file_path
        # Clean up the temporary file
        if os.path.exists(temp_file_path):
            os.unlink(temp_file_path)
    
    def _read_log_file(self, log_file_path):
        """
        Read log file with a retry mechanism to handle potential 
        filesystem synchronization delays.
        """
        for _ in range(5):  # Try up to 5 times
            try:
                with open(log_file_path, 'r') as log:
                    return log.read()
            except FileNotFoundError:
                time.sleep(0.1)  # Wait a bit before retrying
        return ''
    
    def test_log_selection_basic(self, temp_log_file):
        """Test basic logging of a menu selection."""
        logger = MenuLogger(log_file=temp_log_file)
        logger.log_selection('File')
        
        # Force log flushing
        logging.shutdown()
        
        # Read the log file and verify content
        log_content = self._read_log_file(temp_log_file)
        assert 'Menu: Default Menu, Selection: File' in log_content
    
    def test_log_selection_with_context(self, temp_log_file):
        """Test logging a selection with additional context."""
        logger = MenuLogger(log_file=temp_log_file)
        context = {'user': 'john_doe', 'timestamp': '2023-01-01'}
        logger.log_selection('Edit', 'Text Editor', context)
        
        # Force log flushing
        logging.shutdown()
        
        # Read the log file and verify content
        log_content = self._read_log_file(temp_log_file)
        assert 'Menu: Text Editor, Selection: Edit' in log_content
        assert 'user: john_doe' in log_content
        assert 'timestamp: 2023-01-01' in log_content
    
    def test_log_invalid_selection(self, temp_log_file):
        """Test logging an invalid menu selection."""
        logger = MenuLogger(log_file=temp_log_file)
        logger.log_invalid_selection('999', 'Main Menu')
        
        # Force log flushing
        logging.shutdown()
        
        # Read the log file and verify content
        log_content = self._read_log_file(temp_log_file)
        assert 'Invalid Selection - Menu: Main Menu, Attempted Selection: 999' in log_content
    
    def test_log_selection_none_raises_error(self, temp_log_file):
        """Test that logging None as a selection raises a ValueError."""
        logger = MenuLogger(log_file=temp_log_file)
        
        with pytest.raises(ValueError, match="Selection cannot be None"):
            logger.log_selection(None)
    
    def test_multiple_selections(self, temp_log_file):
        """Test logging multiple selections."""
        logger = MenuLogger(log_file=temp_log_file)
        
        logger.log_selection('New', 'File Menu')
        logger.log_selection('Open', 'File Menu')
        logger.log_invalid_selection('Exit', 'File Menu')
        
        # Force log flushing
        logging.shutdown()
        
        # Read the log file and verify content
        log_content = self._read_log_file(temp_log_file)
        assert 'Menu: File Menu, Selection: New' in log_content
        assert 'Menu: File Menu, Selection: Open' in log_content
        assert 'Invalid Selection - Menu: File Menu, Attempted Selection: Exit' in log_content