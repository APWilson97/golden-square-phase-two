import pytest
from lib.grammar_stats import *

def test_given_valid_string():
    grammar_data = GrammarStats()
    result = grammar_data.check('This is a valid string!')
    assert result == True

def test_given_invalid_string():
    grammar_data = GrammarStats()
    result = grammar_data.check('this is not a valid string,')
    assert result == False

def test_given_capital_letter_invalid_punctuation():
    grammar_data = GrammarStats()
    result = grammar_data.check('This is not a valid string;')
    assert result == False

def test_given_punctuation_invalid_first_letter():
    grammar_data = GrammarStats()
    result = grammar_data.check('this is not a valid string.')
    assert result == False

def test_given_empty_string():
    grammar_data = GrammarStats()
    result = grammar_data.check('')
    assert result == False

def test_given_string_with_space():
    grammar_data = GrammarStats()
    result = grammar_data.check(' ')
    assert result == False

"""Given 4 different strings, 2 are valid and 2 are not, should return an integer of 50 representing percentage"""

def test_percentage_good_of_fifty():
    grammar_data = GrammarStats()
    grammar_data.check('This is a valid string!')
    grammar_data.check('this is not a valid string')
    grammar_data.check('this is not a valid string')
    grammar_data.check('This should be a valid string.')
    assert grammar_data.percentage_good() == 50

def test_percentage_good_of_51():
    grammar_data = GrammarStats()
    valid_strings = ['This is a valid string!' for i in range(1,27)]
    invalid_strings = ['this is not a valid string' for i in range(1,26)]
    for string in valid_strings:
        grammar_data.check(string)
    
    for string in invalid_strings:
        grammar_data.check(string)
    
    assert grammar_data.percentage_good() == 51


"""For checking the percentage of texts that have passed the check method, could create an instance variable
where it keeps track of the number of the texts that have passed and also a total number of texts checked
assigned to another instance variable
For the test method, we can call the check method multiple times and then call the percentage_good method at the end"""