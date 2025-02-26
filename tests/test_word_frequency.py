import os
import pytest
from src.word_frequency import count_word_frequencies, get_total_word_count

@pytest.fixture
def sample_file(tmp_path):
    """Create a temporary file with sample words for testing."""
    file_path = tmp_path / "sample_words.txt"
    file_path.write_text("apple, banana, apple, cherry, banana, date, apple")
    return str(file_path)

@pytest.fixture
def empty_file(tmp_path):
    """Create an empty temporary file."""
    file_path = tmp_path / "empty_file.txt"
    file_path.touch()
    return str(file_path)

def test_count_word_frequencies(sample_file):
    """Test counting word frequencies."""
    result = count_word_frequencies(sample_file)
    
    # Check if the result is as expected
    assert result == {
        'apple': 3,
        'banana': 2,
        'cherry': 1,
        'date': 1
    }
    
    # Verify the result is sorted in descending order
    frequencies = list(result.values())
    assert frequencies == sorted(frequencies, reverse=True)

def test_get_total_word_count(sample_file):
    """Test getting total word count."""
    total_count = get_total_word_count(sample_file)
    assert total_count == 7

def test_empty_file(empty_file):
    """Test handling of empty file."""
    with pytest.raises(ValueError, match="The file is empty."):
        count_word_frequencies(empty_file)

def test_nonexistent_file():
    """Test handling of nonexistent file."""
    with pytest.raises(FileNotFoundError):
        count_word_frequencies("nonexistent_file.txt")

def test_file_with_extra_spaces(tmp_path):
    """Test file with extra spaces and whitespace."""
    file_path = tmp_path / "extra_spaces.txt"
    file_path.write_text("  apple ,  banana ,apple,  cherry  ")
    
    result = count_word_frequencies(str(file_path))
    assert result == {
        'apple': 2,
        'banana': 1,
        'cherry': 1
    }

def test_case_sensitivity(tmp_path):
    """Test that word counting is case-sensitive."""
    file_path = tmp_path / "case_test.txt"
    file_path.write_text("Apple, apple, APPLE, Apple")
    
    result = count_word_frequencies(str(file_path))
    assert result == {
        'Apple': 2,
        'apple': 1,
        'APPLE': 1
    }