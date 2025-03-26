print("Домашнее задание")
li = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
for i in range(len(li)):
    if li.count(i) == 1:
        print(li, end=" ")