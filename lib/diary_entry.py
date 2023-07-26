class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        self.title = title
        self.contents = contents
        self.previous_chunk = 0

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        return f"My {self.title}: {self.contents}"

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        title_list = self.title.split()
        contents_list = self.contents.split()
        return len(title_list) + len(contents_list)

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        minutes = len(self.contents.split()) / wpm
        return minutes

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        chunk_of_contents_length = wpm * minutes
        contents_words = self.contents.split()
        if self.previous_chunk >= len(contents_words):
            self.previous_chunk = 0

        chunk_start = self.previous_chunk
        chunk_end = self.previous_chunk + chunk_of_contents_length 
        chunk_words = contents_words[chunk_start:chunk_end]
        self.previous_chunk = chunk_end
        return ' '.join(chunk_words)