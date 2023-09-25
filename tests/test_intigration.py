from lib.diary import Diary
from lib.diary_entry import DiaryEntry

'''Given I add two diary entries, I see them back in a list'''
def test_add_two_entries_and_see_them_in_list():
    diary = Diary()
    entry_1 = DiaryEntry('My title 1 ', 'My contents 1')
    entry_2 = DiaryEntry('My title 2', 'My contents 2')
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]

'''Given I add two diary entries, I see the word count of the list'''

def test_return_word_count_of_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry('My title 1 ', 'My contents 1')
    entry_2 = DiaryEntry('My title 2', 'My contents 2')
    diary.add(entry_1)
    diary.add(entry_2)
    diary.all()
    assert diary.count_words() == 6

'''give I add two diary entries, how many long would it take user to read all entries'''    

def test_return_time_to_read_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry('My title 1 ', 'My contents 1 2 3')
    entry_2 = DiaryEntry('My title 2', 'My contents 4 5 6')
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(2) == 5

'''Given 2 entries of different lengths, get back entry that can be read in given time and wpm'''

def test_return_best_entry_given_wpm_and_time():
    diary = Diary()
    entry_1 = DiaryEntry('My title 1 ', 'My contents 1 ')
    entry_2 = DiaryEntry('My title 2', 'My contents 4 5 6 7 8 ')
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 4) == entry_2







    