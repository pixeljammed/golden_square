class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        self.entries.append(entry)

    def all(self):
        return self.entries

    def count_words(self):
        total_word_count = 0
        for entry in self.entries:
            total_word_count += entry.count_words()
        return total_word_count

    def reading_time(self, wpm):
        total_reading_time = 0
        for entry in self.entries:
            total_reading_time += entry.reading_time(wpm)
        return total_reading_time
    
    def find_best_entry_for_reading_time(self, wpm, minutes):
        best_entry = None
        best_time = 0
        for entry in self.entries:
            current_time = entry.reading_time(wpm)
            if current_time < minutes:
                if best_entry is None or current_time > best_time:
                    best_entry = entry
                    best_time = current_time
        return best_entry