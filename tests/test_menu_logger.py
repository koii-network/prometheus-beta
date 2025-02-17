import os
import logging
import pytest
from src.menu_logger import MenuLogger

class TestMenuLogger:
    def setup_method(self):
        # Use a temporary log file for each test
        self.log_file = 'test_menu_selections.log'
        self.menu_logger = MenuLogger(log_file=self.log_file)
    
    def teardown_method(self):
        # Remove the log file after each test
        if os.path.exists(self.log_file):
            os.remove(self.log_file)
    
    def test_single_selection_logging(self):
        """Test logging a single menu selection"""
        self.menu_logger.log_selection('Main Menu', 'Settings')
        
        # Read the log file and verify contents
        with open(self.log_file, 'r') as f:
            log_content = f.read()
        
        assert 'Menu: Main Menu - Selected: Settings' in log_content
    
    def test_multiple_selections_logging(self):
        """Test logging multiple menu selections"""
        self.menu_logger.log_multiple_selections('Preferences', ['Dark Mode', 'Notifications'])
        
        # Read the log file and verify contents
        with open(self.log_file, 'r') as f:
            log_content = f.read()
        
        assert 'Menu: Preferences - Selections: [\'Dark Mode\', \'Notifications\']' in log_content
    
    def test_empty_menu_name_handling(self):
        """Test handling of empty menu name"""
        # This should log a warning and not raise an exception
        self.menu_logger.log_selection('', 'Option')
        self.menu_logger.log_multiple_selections('', ['Option1', 'Option2'])
        
        # Read the log file and verify warning
        with open(self.log_file, 'r') as f:
            log_content = f.read()
        
        assert 'WARNING' in log_content
        assert 'Invalid menu selection' in log_content
    
    def test_none_selection_handling(self):
        """Test handling of None selections"""
        # This should log a warning and not raise an exception
        self.menu_logger.log_selection('Menu', None)
        self.menu_logger.log_multiple_selections('Menu', [])
        
        # Read the log file and verify warning
        with open(self.log_file, 'r') as f:
            log_content = f.read()
        
        assert 'WARNING' in log_content
        assert 'Invalid menu selections' in log_content