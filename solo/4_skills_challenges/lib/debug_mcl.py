from collections import Counter
def get_most_common_letter(text):
    text = text.replace(" ", "")
    counter = Counter()
    for char in text:
        counter[char] = counter.get(char, 0) + 1
    letter = counter.most_common(1)[0][0]
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")