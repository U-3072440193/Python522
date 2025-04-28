# import geometry.rect
# import geometry.sq
# import geometry.trian

from geometry import rect, sq, trian

r1 = rect.Rectangle(1, 2)
r2 = rect.Rectangle(8, 4)

s1 = sq.Square(1)
s2 = sq.Square(8)

t1 = trian.Triangle(3, 4, 8)

shape = [r1, r2, s1, s2, t1]

for _ in shape:
    print(_.get_perimeter())
