import os
import pytest
import shutil
from src.file_mover import move_file

@pytest.fixture
def setup_test_files(tmp_path):
    """Create test files and directories for file moving tests."""
    # Create a source directory with a test file
    source_dir = tmp_path / 'source'
    source_dir.mkdir()
    test_file = source_dir / 'test_file.txt'
    test_file.write_text('Test content')

    # Create destination directory
    dest_dir = tmp_path / 'destination'
    dest_dir.mkdir()

    return {
        'source_file': str(test_file),
        'dest_dir': str(dest_dir),
        'dest_file': str(dest_dir / 'test_file.txt')
    }

def test_move_file_success(setup_test_files):
    """Test successful file move."""
    result = move_file(
        setup_test_files['source_file'], 
        setup_test_files['dest_file']
    )
    
    assert result == setup_test_files['dest_file']
    assert os.path.exists(setup_test_files['dest_file'])
    assert not os.path.exists(setup_test_files['source_file'])

def test_move_file_empty_paths():
    """Test that empty paths raise ValueError."""
    with pytest.raises(ValueError):
        move_file('', '')

def test_move_file_nonexistent_source(tmp_path):
    """Test moving a non-existent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        move_file(
            str(tmp_path / 'nonexistent_file.txt'), 
            str(tmp_path / 'destination' / 'file.txt')
        )

def test_move_file_directory_as_source(tmp_path):
    """Test attempting to move a directory raises IsADirectoryError."""
    test_dir = tmp_path / 'test_directory'
    test_dir.mkdir()

    with pytest.raises(IsADirectoryError):
        move_file(
            str(test_dir), 
            str(tmp_path / 'destination' / 'directory')
        )

def test_move_file_creates_destination_dir(setup_test_files, tmp_path):
    """Test that destination directory is created if it doesn't exist."""
    new_dest_dir = tmp_path / 'new_destination'
    new_dest_file = new_dest_dir / 'test_file.txt'

    result = move_file(
        setup_test_files['source_file'], 
        str(new_dest_file)
    )
    
    assert result == str(new_dest_file)
    assert os.path.exists(str(new_dest_file))
    assert not os.path.exists(setup_test_files['source_file'])