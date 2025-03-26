print("Домашнее задание")
# нелокальная s


def rect_paral(a, b, c):
    s = 0

    def inner(i, j):
        nonlocal s
        s += 2 * (i * j)

    inner(a, b)
    inner(a, c)
    inner(b, c)

    return s


print(rect_paral(2, 4, 6))
print(rect_paral(5, 8, 2))
print(rect_paral(1, 6, 8))


# глобальная s
s = 0


def rect_paral(a, b, c):
    global s
    s = 0

    def inner(i, j):
        global s
        s += 2 * (i * j)

    inner(a, b)
    inner(a, c)
    inner(b, c)


rect_paral(2, 4, 6)
print(s)
