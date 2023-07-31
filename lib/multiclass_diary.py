from lib.multiclass_diary_entry import *
from lib.multiclass_phone_number import PhoneNumber

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
    
    def list_phone_numbers(self):
        entries_with_phone_numbers = []
        for entry in self._diary:
            if entry.phone_number == None:
                continue
            elif entry.phone_number.has_a_phone_number_check() == True:
                entries_with_phone_numbers.append(entry)
        return entries_with_phone_numbers