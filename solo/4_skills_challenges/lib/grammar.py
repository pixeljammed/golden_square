class GrammarStats:
    def __init__(self):
        self.count = 0
        self.good_count = 0

    def check(self, text):
        self.count += 1
        good = (text[0].isupper() and text[-1] in ".!?")
        if good == True:
            self.good_count += 1
        return good

    def percentage_good(self):
        if self.count != 0:
            return (self.good_count  / self.count) * 100
        else:
            raise Exception("You have not checked at least 1 string for grammar yet!")