from lib.count_words import *
import pytest

def test_given_five_word_string():
    result = count_words('Hello my name is Alex')
    assert result == 5

def test_given_string_with_no_spaces():
    result = count_words('HellomynameisAlex')
    assert result == 1

def test_given_string_with_numbers():
    result = count_words('This string is 5 words long')
    assert result == 5

def test_given_string_with_commas_and_no_spaces():
    result = count_words('This,string,only,has,commas')
    assert result == 1

def test_given_string_with_symbols():
    result = count_words('This word & this word')
    assert result == 4

def test_given_empty_string():
    result = count_words('')
    assert result == 0

def test_given_integer_instead_of_string():
    with pytest.raises(Exception) as error:
        count_words(123)
    error_message = str(error.value)
    assert error_message == 'Input should be a string!'