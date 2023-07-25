from lib.estimated_reading_time import *
import pytest

"""Given a text of 400 hundred words
Return a string of reading_time: 2 minutes"""

def test_four_hundred_words():
    text = []
    for i in range(0,400):
        text.append("word")
    result = estimated_reading_time(text)
    assert result == "reading time: 2 minutes"

"""Given a text with 20 words
It returns a time of 6 seconds"""

def test_twenty_words():
    text = []
    for i in range(0,20):
        text.append("word")
    result = estimated_reading_time(text)
    assert result == "reading time: 6 seconds"


"""
Given a text of 12,000 words
It returns a time of 1 hours
"""

def test_twelve_thousand_words():
    text = []
    for i in range(0,12000):
        text.append("word")
    result = estimated_reading_time(text)
    assert result == "reading time: 1 hours"


"""
Given a text of 2300 words
It returns a time of 11 minutes, 30 seconds
"""
def test_2300_words():
    text = []
    for i in range(0,2300):
        text.append("word")
    result = estimated_reading_time(text)
    assert result == "reading time: 11 minutes, 30 seconds"

"""
Given a text of 32200 words
It returns a time of 2 hours and 41 minutes
"""

def test_32200_words():
    text = []
    for i in range(0,32200):
        text.append("word")
    result = estimated_reading_time(text)
    assert result == "reading time: 2 hours, 41 minutes"
