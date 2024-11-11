
def get_dup(s: str):
    t = []
    i = 0
    for l in s: # noqa
        if l not in t:
            t.append(l)
        else:
            i += 1
    return [i, t]

# print(get_dup('446890912aAAfFtt'))
