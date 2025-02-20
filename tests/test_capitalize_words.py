import pytest
from src.capitalize_words import capitalize_comma_separated_words

def test_capitalize_simple_words():
    assert capitalize_comma_separated_words('hello,world') == 'Hello,World'

def test_capitalize_mixed_case():
    assert capitalize_comma_separated_words('hELLo,wORLd') == 'Hello,World'

def test_single_word():
    assert capitalize_comma_separated_words('hello') == 'Hello'

def test_multiple_words():
    assert capitalize_comma_separated_words('apple,banana,cherry') == 'Apple,Banana,Cherry'

def test_invalid_input_with_spaces():
    with pytest.raises(ValueError, match="Input must contain only alphabetical characters and commas"):
        capitalize_comma_separated_words('hello world')

def test_invalid_input_with_punctuation():
    with pytest.raises(ValueError, match="Input must contain only alphabetical characters and commas"):
        capitalize_comma_separated_words('hello!,world')

def test_empty_string():
    assert capitalize_comma_separated_words('') == ''

def test_consecutive_commas():
    with pytest.raises(ValueError, match="Input must contain only alphabetical characters and commas"):
        capitalize_comma_separated_words('hello,,world')