from lib.diary_entry import *

def test_diary_entry_initial():
    diary_entry = DiaryEntry('day', 'today was a good day')
    assert diary_entry.title == 'day'
    assert diary_entry.contents == 'today was a good day'

def test_diary_format():
    diary_entry = DiaryEntry('day', 'today was a good day')
    assert diary_entry.format() == 'My day: today was a good day'

def test_count_words_in_diary():
    diary_entry = DiaryEntry('first day', 'I studied a lot of testing and debugging today')
    assert diary_entry.count_words() == 11

def test_reading_time_of_5_words():
    diary_entry = DiaryEntry('first day', 'I studied a lot of testing and debugging today. It was challenging at first but I eventually got there in the end')
    assert diary_entry.reading_time(5) == 4.4

def test_reading_chunk_2wpm_5minutes():
    diary_entry = DiaryEntry('first day', 'I studied a lot of testing and debugging today. It was challenging at first but I eventually got there in the end')
    assert diary_entry.reading_chunk(2, 5) == 'I studied a lot of testing and debugging today. It'

def test_reading_chunk_2wpm_5minutes_called_twice():
    diary_entry = DiaryEntry('first day', 'I studied a lot of testing and debugging today. It was challenging at first but I eventually got there in the end')
    assert diary_entry.reading_chunk(2, 5) == 'I studied a lot of testing and debugging today. It'
    assert diary_entry.reading_chunk(2, 5) == 'was challenging at first but I eventually got there in'

def test_reading_chunk_called_three_times_then_reset():
    diary_entry = DiaryEntry('first day', 'I studied a lot of testing and debugging today. It was challenging at first but I eventually got there in the end')
    assert diary_entry.reading_chunk(2, 5) == 'I studied a lot of testing and debugging today. It'
    assert diary_entry.reading_chunk(2, 6) == 'was challenging at first but I eventually got there in the end'
    assert diary_entry.reading_chunk(2, 2) == 'I studied a lot'