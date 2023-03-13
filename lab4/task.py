from random import random


N = 1

a, b,  k, k1, k2 = map(int, input().split())

set_u = { k * (x ** N)  for x in range(a, b + 1) }
print('full:', set_u)

class fullSet(set):
    def setext(self):
        return fullSet(set_u - self)


set_a = fullSet({ x for x in set_u if random() < 0.5 })
print('A:', set_a)
set_b = fullSet({ x for x in set_u if (lambda x: (x % k1 == 0 or x % k2 == 0))(x) })
print('B:', set_b)

res1 = fullSet(set_a | set_b).setext()

res2 = (set_a.setext() & set_b.setext())
print('check expression: ', res1 == res2, 'set:', res1, res2)
print('5:', {x for x in res1 if x % 2 == 0})
