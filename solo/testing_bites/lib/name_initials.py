def name_initials(name):
    names = name.split()
    return(f"{names[0][0]}.{names[-1][0]}")