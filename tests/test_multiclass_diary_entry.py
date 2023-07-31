from lib.multiclass_diary_entry import *

"""
Given a title, contents and phone number
We see the phone number represented in the phone number property
"""
def test_given_title_contents_no_number():
    entry1 = DiaryEntry('Day 1', 'Studied coding today')
    entry2 = DiaryEntry('Day 2', 'Did a lot of pair programming today', 12345678)
    assert entry1.phone_number == None
    assert entry2.phone_number == 12345678

"""
Given a diary entry
We can see the reading time for that entry
"""
def test_see_reading_time_for_diary_entry():
    entry1 = DiaryEntry('Day 1', 'Did a lot of pair programming today too', 12345678)
    assert entry1.reading_time(2) == 4