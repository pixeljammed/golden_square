from lib.diary import *

def test_diary_entry_create():
    my_diary_entry = DiaryEntry("The Worst Day Ever!", "I peed the bed. Oh noes.")
    assert type(my_diary_entry) == DiaryEntry
    assert my_diary_entry.title == "The Worst Day Ever!"
    assert my_diary_entry.contents == "I peed the bed. Oh noes."
    assert my_diary_entry.reader == 0

"""
format()
returns a nicely formatted string - which is the combined diary entry title and contents
"""
def test_diary_entry_format():
    my_diary_entry = DiaryEntry("qwerty", "aeiou")
    assert my_diary_entry.format() == "qwerty: aeiou"

"""
count_words()
returns the number of words in the diary entry contents
"""
def test_diary_entry_word_count():
    my_diary_entry = DiaryEntry("a lie", "i am a genius")
    assert my_diary_entry.count_words() == 4

"""
reading_time()
returns an integer number of how long it will take to read a diary entry given WPM reading speed
"""
def test_diary_reading_time():
    my_diary_entry = DiaryEntry("kekmaxxing", "poop poop poop poop poop poop poop poop from the butt")
    assert my_diary_entry.reading_time(1) == 11

"""
reading_chunk()
description
"""
def test_diary_entry_reading_chunk():
    my_diary_entry = DiaryEntry("Dear Diary...", "Today a little boy came up to me and said: '67!', so I decided to punch him in his face. He couldn't have been older than 5! Hahahaha! Who's laughing now little bum. Six seven. Sigma nation forever squad.")

    my_reading_chunk = my_diary_entry.reading_chunk(10, 1)
    assert my_reading_chunk == "Today a little boy came up to me and said:"

def test_diary_entry_reading_chunk_multiple():
    my_diary_entry = DiaryEntry("Dear Diary...", "Today a little boy came up to me and said: '67!', so I decided to punch him in his face. He couldn't have been older than 5! Hahahaha! Who's laughing now little bum. Six seven. Sigma nation forever squad.")

    my_reading_chunk = my_diary_entry.reading_chunk(10, 1)
    assert my_reading_chunk == "Today a little boy came up to me and said:"
    my_reading_chunk = my_diary_entry.reading_chunk(10, 1)
    assert my_reading_chunk == "'67!', so I decided to punch him in his face."
    my_reading_chunk = my_diary_entry.reading_chunk(10, 1)
    assert my_reading_chunk == "He couldn't have been older than 5! Hahahaha! Who's laughing"

def test_diary_entry_reading_chunk_overflow():
    my_diary_entry = DiaryEntry("Dear Diary...", "Today a little boy came up to me and said: '67!', so I decided to punch him in his face. He couldn't have been older than 5! Hahahaha! Who's laughing now little bum. Six seven. Sigma nation forever squad.")

    my_reading_chunk = my_diary_entry.reading_chunk(200, 5)
    assert my_reading_chunk == "Today a little boy came up to me and said: '67!', so I decided to punch him in his face. He couldn't have been older than 5! Hahahaha! Who's laughing now little bum. Six seven. Sigma nation forever squad."

def test_diary_entry_reading_chunk_overflow_mutliple():
    my_diary_entry = DiaryEntry("Dear Diary...", "Today a little boy came up to me and said: '67!', so I decided to punch him in his face. He couldn't have been older than 5! Hahahaha! Who's laughing now little bum. Six seven. Sigma nation forever squad.")

    my_reading_chunk = my_diary_entry.reading_chunk(200, 5)
    assert my_reading_chunk == "Today a little boy came up to me and said: '67!', so I decided to punch him in his face. He couldn't have been older than 5! Hahahaha! Who's laughing now little bum. Six seven. Sigma nation forever squad."
    my_reading_chunk = my_diary_entry.reading_chunk(10, 1)
    assert my_reading_chunk == "Today a little boy came up to me and said:"