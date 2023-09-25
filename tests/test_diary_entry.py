from lib.diary_entry import DiaryEntry

'''When I initialise contetns and title, I get
that contents and title back'''

def test_return_contents_and_title_when_given():
    diary_entry = DiaryEntry('My title', 'My contents')
    assert diary_entry.title == 'My title'
    assert diary_entry.contents == 'My contents'

'''Given multiple entries, I get back the word count of these entries'''

def test_return_word_count_of_entries():
    diary_entry = DiaryEntry('My title is only', 'One two three')
    assert diary_entry.count_words() == 3
