import pytest
from src.dot_case_converter import convert_to_dot_case

def test_convert_to_dot_case():
    # Test various input types
    assert convert_to_dot_case('hello world') == 'hello.world'
    assert convert_to_dot_case('HelloWorld') == 'hello.world'
    assert convert_to_dot_case('hello_world') == 'hello.world'
    assert convert_to_dot_case('hello-world') == 'hello.world'
    
    # Test mixed separators
    assert convert_to_dot_case('Hello_World-Test') == 'hello.world.test'
    
    # Test empty string
    assert convert_to_dot_case('') == ''
    
    # Test None
    assert convert_to_dot_case(None) == ''
    
    # Test multiple consecutive separators
    assert convert_to_dot_case('hello__world  test') == 'hello.world.test'
    
    # Test strings with already dot-like separators
    assert convert_to_dot_case('hello.world') == 'hello.world'
    
    # Test string with mixed casing
    assert convert_to_dot_case('HelloWorldTest') == 'hello.world.test'