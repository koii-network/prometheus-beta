import pytest
from src.hyphen_to_space import convert_hyphens_to_spaces

def test_convert_hyphens_to_spaces():
    # Test basic conversion
    assert convert_hyphens_to_spaces('hello-world') == 'hello world'
    
    # Test multiple hyphens
    assert convert_hyphens_to_spaces('python-is-awesome') == 'python is awesome'
    
    # Test string with no hyphens remains unchanged
    assert convert_hyphens_to_spaces('nohyphens') == 'nohyphens'
    
    # Test empty string
    assert convert_hyphens_to_spaces('') == ''
    
    # Test string with only hyphens
    assert convert_hyphens_to_spaces('----') == '    '

def test_convert_hyphens_to_spaces_error_handling():
    # Test non-string input raises TypeError
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_hyphens_to_spaces(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_hyphens_to_spaces(None)