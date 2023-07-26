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