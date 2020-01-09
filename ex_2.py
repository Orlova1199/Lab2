   #!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)

# Реализация задания 2

data11 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
print(list(Unique(data11)))  # будет последовательно возвращать только 1 и 2

print(list(Unique(gen_random(1, 3, 10))))  # будет последовательно возвращать только 1, 2 и 3

data12 = ['S', 'v', 'e', 't', 'a', 'a', 'a', 'A']
print(list(Unique(data12)))  # будет последовательно возвращать только S, v, e, t, a, A

data13 = ['S', 'v', 'e', 't', 'a', 'a', 'a', 'A']
print(list(Unique(data13, ignore_case=True)))  # будет последовательно возвращать только s, v, e, t, a
