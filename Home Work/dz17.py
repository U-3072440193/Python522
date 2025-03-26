def under_zero(lst, index=0, count=0):
    if index >= len(lst):
        return count
    elif lst[index] < 0:
        return under_zero(lst, index + 1, count + 1)
    else:
        return under_zero(lst, index + 1, count)


s = [-2, 3, 8, -11, -4, 6]
print(under_zero(s))
