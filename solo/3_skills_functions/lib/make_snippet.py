def make_snippet(text):
    words = text.split()
    snippet = f"{' '.join(words[:5])}..."
    return snippet