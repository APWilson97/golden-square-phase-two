Describe the Problem:
As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

Design the Class System:

                                           ┌───────────────────────────────────────┐
                                           │ Diary()                               │
                                           │                                       │
┌───────────────────────────────┐          │ add()                                 │◄──────────────────────────────────┐
│ TodoList()                    │          │ all()                                 │                                   │
│                               │          │ best_entry_for_reading_time(wpm,mins) │        
│ add()                         │          │ reading_time()                        │        ┌──────────────────────────┴──────┐
│ incomplete()                  │          │ count_words()                         ├───────►│ PhoneNumber()                   │
│ complete()                    │          │                                       │        │                                 │
│ give_up()                     │          └──────┬────────────────────────────────┘        │ list_phone_numbers()            │
└─────┬───────────────▲─────────┘                 │                     ▲                   │                                 │
      │               │                           │                     │                   │                                 │
      │               │                           ▼                     │                   │                                 │
      │               │                    ┌────────────────────────────┴──────────┐        │                                 │
 ┌────▼───────────────┴─────────┐          │ DiaryEntry()                          │        │                                 │
 │ Todo()                       │          │                                       │        │                                 │
 │                              │          │ count_words()                         │        │                                 │
 │ mark_complete()              │          │ reading_time()                        │        │                                 │
 │                              │          │                                       │        └─────────────────────────────────┘
 │                              │          │                                       │
 │                              │          │                                       │
 └──────────────────────────────┘          │                                       │
                                           └───────────────────────────────────────┘


class Diary:
    def __init__(self):
        self._diary = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self._diary.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self._diary

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        word_count = 0
        for entry in self._diary:
            word_count += entry.count_words()
        return word_count

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        total_reading_time = 0
        for entry in self._diary:
            total_reading_time += entry.reading_time(wpm)
        return total_reading_time

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        best_entry = None
        most_amount_of_words_read = wpm * minutes

        for entry in self._diary:
            if len(entry.contents) <= most_amount_of_words_read:
                best_entry = entry
        return entry
    
class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string
    #   phone_number: an integer

    def __init__(self, title, contents, phone_number=None): # title, contents are strings, phone_number is an integer
        # Side-effects:
        #   Sets the title and contents properties
        self.title = title
        self.contents = contents
        self.previous_chunk = 0

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        return len(self.contents.split())

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        minutes =  self.count_words() / wpm
        return minutes

class PhoneNumber:
    def __init__(self):
        pass
    
    def list_phone_numbers(self):
        # Returns a list of all the entries with phone numbers
        # No side effects

class TodoList:
    def __init__(self):
        self.todo_list = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.todo_list.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        incomplete_list = []
        for task in self.todo_list:
            if task.complete == False:
                incomplete_list.append(task)
        return incomplete_list

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        complete_list = [task for task in self.todo_list if task.complete == True]
        return complete_list

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for task in self.todo_list:
            task.complete = True

class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        self.task = task
        self.complete = False

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        self.complete = True


Integration Tests:
"""
Given a diary
When we add 2 entries
We see those entries reflected in the diary entry list
"""

diary = Diary()
entry1 = DiaryEntry('Day 1', 'I studied coding today')
entry2 = DiaryEntry('Day 2', 'I studied testing today and it was really fun')
diary.add(entry1)
diary.add(entry2)
diary.all() -> [entry1, entry2]

"""
Given a diary
When we add 2 entries
We can see which diary entry is better for a given reading time and wpm
"""

diary = Diary()
entry1 = DiaryEntry('Day 1', 'I studied coding today')
entry2 = DiaryEntry('Day 2', 'I studied testing today and it was really fun')
diary.add(entry1)
diary.add(entry2)
diary.find_best_entry_for_reading_time(3,3) -> entry2

"""
Given a diary
When we add 3 entries
We can see which ones have phone numbers associated with them
"""

diary = Diary()
entry1 = DiaryEntry('Day 1', 'I studied coding today', 12345678)
entry2 = DiaryEntry('Day 2', 'I studied testing today and it was really fun')
entry3 = DiaryEntry('Day 3', 'We did a lot of pair programming today and I made a new friend', 87654321)
diary.add(entry1)
diary.add(entry2)
diary.add(entry3)
diary.list_phone_numbers() -> [entry1, entry3]

"""
Given a todo list
When we add 2 tasks
We can see all tasks and they are initially incomplete
"""

task_list = TodoList()
todo1 = Todo('Do the laundry')
todo2 = Todo('Cook dinner for tonight')
task_list.add(todo1)
task_list.add(todo2)
task_list.incomplete() -> [todo1, todo2]

"""
Given a todo list
When we add 3 tasks and mark 2 as complete
We can see all the tasks that are complete and are not complete
"""

task_list = TodoList()
todo1 = Todo('Do the laundry')
todo2 = Todo('Cook dinner for tonight')
todo3 = Todo('Go walk the dog')
task_list.add(todo1)
task_list.add(todo2)
task_list.add(todo3)
task_list.mark_complete(todo1)
task_list.mark_complete(todo3)
task_list.complete() -> [todo1, todo3]
task_list.incomplete() -> [todo2]

"""
Given a todo list
When we add 3 tasks and give up
We should see all tasks marked as complete
"""

task_list = TodoList()
todo1 = Todo('Do the laundry')
todo2 = Todo('Cook dinner for tonight')
todo3 = Todo('Go walk the dog')
task_list.add(todo1)
task_list.add(todo2)
task_list.add(todo3)
task_list.give_up()
task_list.complete() -> [todo1, todo2, todo3]
task_list.incomplete() -> []


Unit Tests:

"""
Given a title, contents and phone number
We see the phone number represented in the phone number property
"""

entry1 = DiaryEntry('Day 1', 'Studied coding today')
entry2 = DiaryEntry('Day 2', 'Did a lot of pair programming today', 12345678)
entry1.phone_number -> None
entry2.phone_number -> 12345678

"""
Given a diary entry
We can see the reading time for that entry
"""
entry1 = DiaryEntry('Day 1', 'Did a lot of pair programming today too', 12345678)
entry1.reading_time(2) -> 4

"""
Given an empty diary
Check that the diary is empty
"""

diary = Diary()
diary._diary -> []

"""
Given a todo task
We can see the task and complete properties set correctly
"""

todo1 = Todo('Do the laundry')
todo1.task -> 'Do the laundry'
todo1.complete -> False
