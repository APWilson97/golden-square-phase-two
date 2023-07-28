from lib.diary import *

def test_initial_empty_diary():
    diary = Diary()
    diary.diary = []

def test_all():
    diary = Diary()
    diary.add('Finished refactoring today')
    diary.add('Completed the challenges for the curriculum')
    assert diary.all() == ['Finished refactoring today', 'Completed the challenges for the curriculum']