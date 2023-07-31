from lib.multiclass_diary import *
from lib.multiclass_phone_number import *

"""
Given an empty diary
Check that the diary is empty
"""
def test_initial_empty_diary():
    diary = Diary()
    assert diary._diary == []

"""
Given a diary
When we add 2 entries
We see those entries reflected in the diary entry list
"""
def test_two_diary_entries_no_numbers():
    diary = Diary()
    entry1 = DiaryEntry('Day 1', 'I studied coding today')
    entry2 = DiaryEntry('Day 2', 'I studied testing today and it was really fun')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.all() == [entry1, entry2]

"""
Given a diary
When we add 2 entries
We can see which diary entry is better for a given reading time and wpm
"""
def test_two_entries_best_reading_time():
    diary = Diary()
    entry1 = DiaryEntry('Day 1', 'I studied coding today')
    entry2 = DiaryEntry('Day 2', 'I studied testing today and it was really fun')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.find_best_entry_for_reading_time(3,3) == entry2

"""
Given a diary
When we add 3 entries
We can see which ones have phone numbers associated with them
"""

def test_three_entries_two_with_phone_numbers():
    diary = Diary()
    number1 = PhoneNumber(12345678)
    number2 = PhoneNumber(87654321)
    entry1 = DiaryEntry('Day 1', 'I studied coding today', number1)
    entry2 = DiaryEntry('Day 2', 'I studied testing today and it was really fun')
    entry3 = DiaryEntry('Day 3', 'We did a lot of pair programming today and I made a new friend', number2)
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.list_phone_numbers() == [entry1, entry3]