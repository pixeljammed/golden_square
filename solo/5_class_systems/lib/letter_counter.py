from collections import Counter

class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        cntr = Counter()
        for char in self.text:
            cntr[char] = cntr.get(char, 0) + 1
        letter = cntr.most_common(1)[0]
        return letter