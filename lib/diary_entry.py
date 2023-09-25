class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        self.title = title
        self.contents = contents
        self.chunks_read = 0
    
    def count_words(self):
        return len(self.contents.split())
        #print(result)
        

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        self.wpm = wpm
        return self.count_words() // self.wpm
        

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
        self.wpm = wpm
        self.minutes = minutes
        self.chunks_read += 1
        print(self.chunks_read)
        words_read_in_time = self.wpm * self.minutes
        formatted_list = self.format().split()
        result = ' '.join(formatted_list[:words_read_in_time])
        if self.chunks_read == 2:
            result = ' '.join(formatted_list[words_read_in_time:words_read_in_time * 2])
            
        return result
