"""As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO."""

"""Function Signature
check_for_to_do(text)
- Verify if the string #TODO is included within the argument to the method
- return a boolean value of either True of False
- parameters - text, this would be the text to check if the #TODO string is inside
- the text argument
- side effects - no changes to the argument text, no printing of anything"""

"""Examples

Given a text where it is included, should return True
check_for_to_do('This is my #TODO list') -> True

Given a text where it is not inclided, should return False
check_for_to_do('I don't have a list') -> False

Given a text where it has TODO but it is missing a hash #, should return False
check_for_to_do('This is my TODO list') -> False

Given an empty string, it should raise an exception stating that the text is empty
check_for_to_do('') -> Exception raised with a string of 'Text is empty'

Given a text where it is separated by commas, should return True if #TODO is inside string
check_for_to_do('This is my #TODO, list) -> True

Given a text where #TODO is separated into separate letters, should return False
check_for_to_do('This is my # T O D O list) -> False

"""

from lib.to_do import *
import pytest

def test_todo_is_included():
    result = check_for_to_do('This is my #TODO list')
    assert result == True

def test_todo_is_not_included():
    result = check_for_to_do("I don't have a list")
    assert result == False

def test_todo_missing_hash():
    result = check_for_to_do('I have a TODO list')
    assert result == False

def test_empty_string_exception():
    with pytest.raises(Exception) as error:
        check_for_to_do('')
    error_message = str(error.value)
    assert error_message == 'Text is empty'

def test_todo_is_included_with_comma():
    result = check_for_to_do('This is my #TODO, list')
    assert result == True

def test_todo_is_separate_chars():
    result = check_for_to_do('This is my # T O D O list')
    assert result == False