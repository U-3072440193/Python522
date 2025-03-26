from random import randint

print("Домашнее задание")


def do_tuple(start, end):
    return tuple(randint(start, end) for _ in range(10))


tuple1 = do_tuple(0, 5)
tuple2 = do_tuple(-5, 0)
print(tuple1)
print(tuple2)

tuple3 = tuple1 + tuple2
print(tuple3, "\n", 0, "=", tuple3.count(0))
