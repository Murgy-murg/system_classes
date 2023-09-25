class Diary:
    def __init__(self):
        self._diary_list = []

    def add(self, entry):
        self._diary_list.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self._diary_list

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        total = 0
        for entry in self._diary_list:
            total += entry.count_words() 
        return total

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        self.wpm = wpm
        return self.count_words() // self.wpm

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
        words_read_in_time = wpm * minutes
        most_readable = None
        longest_entry = 0
        for entry in self._diary_list:
            if entry.count_words() <= words_read_in_time:
                if entry.count_words() > longest_entry:
                    most_readable = entry
                    longest_entry = entry.count_words()
        return most_readable



