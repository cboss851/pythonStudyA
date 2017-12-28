def hideName(name):
    if len(name)==1:
        return "*"+name[-1:]
    if len(name)==2:
        return "*"+name[-2:]
    if len(name)>=2:
        return "**"+name[-2:]


# print(hideName("xxx"))