from lib.personal_diary import *
import pytest

def test_if_string_is_more_than_5_words():
    result = make_snippet('Hello my name is Alex Wilson and I am a student.')
    assert result == 'Hello my name is Alex...'

def test_if_string_is_5_words():
    result = make_snippet('This string is five words')
    assert result == 'This string is five words'

def test_if_string_is_less_than_five_words():
    result = make_snippet('Hello world')
    assert result == 'Hello world'

def test_if_string_is_empty():
    result = make_snippet('')
    assert result == ''

def test_if_argument_is_a_number():
    with pytest.raises(Exception) as error:
        make_snippet(123)
    error_message = str(error.value)
    assert error_message == 'Input must be a string!'

def test_if_string_has_numbers_inside():
    result = make_snippet('There are more than 5 words in this string')
    assert result == 'There are more than 5...'

def test_if_input_is_float():
    with pytest.raises(Exception) as error:
        make_snippet(5.23)
    error_message = str(error.value)
    assert error_message == 'Input must be a string!'

def test_string_with_commas_does_not_count_as_words():
    result = make_snippet('one,two,three,four,five,six')
    assert result == 'one,two,three,four,five,six'