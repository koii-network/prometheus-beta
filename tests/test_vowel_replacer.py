import pytest
from src.vowel_replacer import replace_vowels

def test_replace_vowels_basic():
    assert replace_vowels('hello') == 'holli'
    assert replace_vowels('world') == 'wurld'

def test_replace_vowels_uppercase():
    assert replace_vowels('HELLO') == 'HOLLI'
    assert replace_vowels('WORLD') == 'WURLD'

def test_replace_vowels_mixed_case():
    assert replace_vowels('Hello World') == 'Holli Wurld'

def test_replace_vowels_edge_cases():
    assert replace_vowels('') == ''
    assert replace_vowels('xyz') == 'xyz'
    assert replace_vowels('aeiou') == 'eioua'
    assert replace_vowels('AEIOU') == 'EIOUA'

def test_replace_vowels_with_punctuation():
    assert replace_vowels('hello, world!') == 'holli, wurld!'

def test_replace_vowels_circular_replacement():
    assert replace_vowels('u') == 'a'
    assert replace_vowels('U') == 'A'