def uas(input):
    alpha = set()
    list1 = list(input.split())
    for i in list1:
        alpha.add(i)
    sort = sorted(alpha)
    string = " ".join(sort)
    return string