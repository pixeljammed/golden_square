def includes_todo(note):
    if type(note) is not str:
        raise Exception("you did not give me a string !! >_<")
    return "#TODO" in note
