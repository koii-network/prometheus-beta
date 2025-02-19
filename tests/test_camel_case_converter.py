import pytest
from src.camel_case_converter import convert_to_camel_case

def test_convert_to_camel_case():
    # Test various input formats
    assert convert_to_camel_case('hello world') == 'helloWorld'
    assert convert_to_camel_case('hello-world') == 'helloWorld'
    assert convert_to_camel_case('hello_world') == 'helloWorld'
    assert convert_to_camel_case('Hello World') == 'helloWorld'
    
    # Test with multiple words
    assert convert_to_camel_case('convert to camel case') == 'convertToCamelCase'
    
    # Test edge cases
    assert convert_to_camel_case('') == ''
    assert convert_to_camel_case(' ') == ''
    assert convert_to_camel_case('123') == ''
    
    # Test with mixed delimiters
    assert convert_to_camel_case('hello-world_test case') == 'helloWorldTestCase'
    
    # Test with already camel case input
    assert convert_to_camel_case('helloWorld') == 'helloWorld'
    
    # Test with special characters
    assert convert_to_camel_case('hello@world!test') == 'helloWorldTest'