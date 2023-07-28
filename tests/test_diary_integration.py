from lib.diary import *
from lib.diary_entry_2 import *

def test_add_two_entries_then_show_list():
    diary = Diary()
    entry_1 = DiaryEntry('Day 1', 'Studied coding today')
    entry_2 = DiaryEntry('Day 2', 'Studied testing today')
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]

"""Give a couple diary entries
Return the total number of words in both of those entries"""

def test_count_words_for_two_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry('Day 1', 'Studied coding today')
    entry_2 = DiaryEntry('Day 2', 'Did a lot of pair programming yesterday and today')
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 12

"""Given 3 diary entries and a reading speed of 5 wpm
Count the reading time for all entries in minutes"""

def test_reading_time_for_three_entries_and_five_wpm():
    diary = Diary()
    entry_1 = DiaryEntry('Day 1', 'Studied coding today')
    entry_2 = DiaryEntry('Day 2', 'Did a lot of pair programming yesterday and today')
    entry_3 = DiaryEntry('Day 3', 'Focused on refactoring my code for the challenges I completed')
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.reading_time(2) == 11

"""Given 3 diary entries
Find the best entry for a reading time of 2wpm and 4 minutes
"""
def test_three_entries_best_reading_time_entry():
    diary = Diary()
    entry_1 = DiaryEntry('Day 1', 'Studied coding today')
    entry_2 = DiaryEntry('Day 2', 'Did a lot of pair programming yesterday and today')
    entry_3 = DiaryEntry('Day 3', 'Focused on refactoring my code for the challenges I completed')
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.find_best_entry_for_reading_time(2, 5) == entry_3