from lib.diary_entry_2 import *

def test_title_and_contents_added():
    entry_1 = DiaryEntry('Day 1', 'Studied coding today')
    assert entry_1.title == 'Day 1'
    assert entry_1.contents == 'Studied coding today'

def test_count_words_for_one_entry():
    entry_1 = DiaryEntry('Day 1', 'Studied coding today')
    assert entry_1.count_words() == 3

def test_reading_time():
    entry_1 = DiaryEntry('Day 1', 'Today was a good day to code')
    assert entry_1.reading_time(2) == 3.5

def test_reading_chunk():
    entry_1 = DiaryEntry('Day 1', 'Today was a good day to code as I was learning how to test drive a multiclass system. There were some challenges I faced when it came to knowing how to perform integration tests.')
    assert entry_1.reading_chunk(5, 3) == 'Today was a good day to code as I was learning how to test drive'
    assert entry_1.reading_chunk(5, 3) == 'a multiclass system. There were some challenges I faced when it came to knowing how'
    assert entry_1.reading_chunk(5, 3) == 'to perform integration tests.'