def f(li):
    nli = []
    for i in range(0, len(li)):
        if li.index(li[i]) == i:
            nli.append(li[i])
    return nli


def sort(li):
    def cmp(e):
        return e[1]
    return sorted(li, key=cmp)


def bai_3():
    for i in range(0, 9):
        if i < 5:
            print('*' * (i + 1))
        else:
            print('*' * (9 - i))


def sort_2(s):
    li = s.split('-')
    return '-'.join(sorted(li))


def dic(d1, d2):
    for x in d2:
        if x in d1:
            d1.update({x: d1[x] + d2[x]})
        else:
            d1.update({x: d2[x]})
    return d1


def dic_2(s):
    return dict(zip(list(s), [s.count(x) for x in s]))
