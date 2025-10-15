from lib.diary import Diary
from lib.diary_entry import DiaryEntry

def test_diary_integration():
    diary = Diary()

    assert type(diary) == Diary
    assert diary.entries == []

    diary_entry_1 = DiaryEntry("World's Best Story", "Number one. Steady hand. One day, Kim Jong Un need new heart. I do operation. But mistake! Kim Jong Un die! SSD very mad! I hide fishing boat, come to America. No English, no food, no money. Darryl give me job. Now I have house, American car and new woman. Darryl save life. My big secret. I kill Kim Jong Un on purpose. I good surgeon. The best!")
    diary_entry_2 = DiaryEntry("Six Seven", "Six seven... six seven... six seven... hahaha... me too funny!")
    diary_entry_3 = DiaryEntry("Poop from Butt", "Dear diary, today I poop bed, now have to clean bed. Not happy.")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)

    assert diary.entries == [diary_entry_1, diary_entry_2, diary_entry_3]

    assert diary.count_words() == 91 # https://files.catbox.moe/p0cpbn.png

    assert diary.reading_time(1) == 91 # if you read 1 word a minute, it would take you 91 minutes to read everything
    assert diary.reading_time(5) == 17 # if you read 5 words a minute, it would take you 17 minutes to read everything

    assert diary.find_best_entry_for_reading_time(1, 100) == diary_entry_1
    assert diary.find_best_entry_for_reading_time(5, 3) == diary_entry_2
    assert diary.find_best_entry_for_reading_time(1, 14) == diary_entry_3
    assert diary.find_best_entry_for_reading_time(15, 2) == diary_entry_2