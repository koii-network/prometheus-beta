import os
import pytest
from src.word_counter import analyze_word_frequency

def test_word_frequency_normal_case(tmp_path):
    # Create a temporary file with sample words
    test_file = tmp_path / "test_words.txt"
    test_file.write_text("apple, banana, apple, cherry, banana, date")
    
    result, total_words = analyze_word_frequency(str(test_file))
    
    assert result == {'apple': 2, 'banana': 2, 'cherry': 1, 'date': 1}
    assert total_words == 6

def test_word_frequency_empty_file(tmp_path):
    # Create an empty file
    test_file = tmp_path / "empty_file.txt"
    test_file.write_text("")
    
    result, total_words = analyze_word_frequency(str(test_file))
    
    assert result == {}
    assert total_words == 0

def test_word_frequency_single_word(tmp_path):
    # Create a file with a single word
    test_file = tmp_path / "single_word.txt"
    test_file.write_text("hello")
    
    result, total_words = analyze_word_frequency(str(test_file))
    
    assert result == {'hello': 1}
    assert total_words == 1

def test_word_frequency_with_spaces(tmp_path):
    # Create a file with words with extra spaces
    test_file = tmp_path / "spaced_words.txt"
    test_file.write_text("  cat ,  dog  , cat  ,  bird")
    
    result, total_words = analyze_word_frequency(str(test_file))
    
    assert result == {'cat': 2, 'dog': 1, 'bird': 1}
    assert total_words == 4

def test_file_not_found():
    # Test file not found scenario
    with pytest.raises(FileNotFoundError):
        analyze_word_frequency("non_existent_file.txt")