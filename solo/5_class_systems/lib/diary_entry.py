class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.reader = 0

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        return (self.count_words() // wpm)

    def reading_chunk(self, wpm, minutes):
        words = self.contents.split(" ")[self.reader: self.reader + wpm * minutes]
        self.reader = self.reader + wpm * minutes
        if self.reader > self.count_words():
            self.reader = 0
        return " ".join(words)