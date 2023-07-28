from lib.diary_entry_2 import *

class Diary:
    def __init__(self):
        self._diary = []
        pass

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self._diary.append(entry)
        pass

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self._diary
        pass

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
            total_reading_time += entry.reading_time(2)
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