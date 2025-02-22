import os
import logging
import pytest
from src.menu_logger import log_user_selection

def test_log_user_selection_basic(tmp_path):
    """Test basic logging functionality"""
    log_file = str(tmp_path / 'menu_selections.log')
    log_user_selection('main_menu', 'option1', log_file)
    
    # Check log file exists and contains expected content
    assert os.path.exists(log_file)
    with open(log_file, 'r') as f:
        log_content = f.read()
        assert 'Menu: main_menu' in log_content
        assert 'Selection: option1' in log_content

def test_log_user_selection_numeric(tmp_path):
    """Test logging with numeric selection"""
    log_file = str(tmp_path / 'numeric_menu.log')
    log_user_selection('number_menu', 42, log_file)
    
    with open(log_file, 'r') as f:
        log_content = f.read()
        assert 'Menu: number_menu' in log_content
        assert 'Selection: 42' in log_content

def test_log_user_selection_invalid_menu_name():
    """Test that empty menu name raises ValueError"""
    with pytest.raises(ValueError, match="Menu name cannot be empty"):
        log_user_selection('', 'option1')

def test_log_user_selection_none_selection():
    """Test that None selection raises ValueError"""
    with pytest.raises(ValueError, match="Selection cannot be None"):
        log_user_selection('menu', None)

def test_log_file_directory_creation(tmp_path):
    """Test that log directory is created if it doesn't exist"""
    log_file = str(tmp_path / 'nested' / 'directory' / 'menu_log.log')
    log_user_selection('test_menu', 'test_option', log_file)
    
    assert os.path.exists(log_file)

def test_multiple_selections(tmp_path):
    """Test logging multiple selections in the same log file"""
    log_file = str(tmp_path / 'multiple_selections.log')
    
    log_user_selection('main_menu', 'option1', log_file)
    log_user_selection('sub_menu', 'option2', log_file)
    
    with open(log_file, 'r') as f:
        log_content = f.read()
        assert 'Menu: main_menu' in log_content
        assert 'Selection: option1' in log_content
        assert 'Menu: sub_menu' in log_content
        assert 'Selection: option2' in log_content