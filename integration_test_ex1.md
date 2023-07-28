Examples of Integration Tests:

Given a couple of diary entries
Add those entries into a Diary instance and return a list of them

entry_1 = DiaryEntry('Day 1', 'Studied coding today')
entry_2 = DiaryEntry('Day 2', 'Studied testing today')
diary.add(entry_1)
diary.add(entry_2)
diary.all() -> {'Day 1': Studied coding today', 'Day 2': 'Studied testing today'}

Given a couple diary entries
Count the number of words in in both of those entries

entry_1 = DiaryEntry('Day 1', 'Studied coding today')
entry_2 = DiaryEntry('Day 2', 'Did a lot of pair programming yesterday and today')
diary.add(entry_1)
diary.add(entry_2)
diary.count_words() -> 12

Given three diary entries and a reading speed of 5 wpm
Count the reading time for reading all entries in minutes

entry_1 = DiaryEntry('Day 1', 'Studied coding today')
entry_2 = DiaryEntry('Day 2', 'Did a lot of pair programming yesterday and today')
entry_3 = DiaryEntry('Day 3', 'Focused on refactoring my code for the challenges I completed')
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)
diary.reading_time(2) -> 11

Given 3 diary entries
Find the best entry for a reading time of 2wpm and 4 minutes

entry_1 = DiaryEntry('Day 1', 'Studied coding today')
entry_2 = DiaryEntry('Day 2', 'Did a lot of pair programming yesterday and today')
entry_3 = DiaryEntry('Day 3', 'Focused on refactoring my code for the challenges I completed')
diary.add(entry_1)
diary.add(entry_2)
diary.add(entry_3)

diary.find_best_entry_for_reading_time(2, 5) -> entry_3
^^^They can read a max of 10 words in 4 minutes total