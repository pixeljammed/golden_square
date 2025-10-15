class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        vowelless = self.text
        for vowel in self.vowels:
            vowelless = vowelless.replace(vowel, "")
        return vowelless