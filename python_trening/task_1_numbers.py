from netaddr.strategy.ipv6 import width

a = 2
print(a, "относится к типу", type(a))

b = 15.0001
print(b, "относится к типу", type(b))

#комплексное число
#с = 1 + 2j
#print(c, "Комплексное число?", isinstance(c, complex))

def length(s :str = '``') -> int:
    print(len(s))
    return len(s)

def foo(w, q :list = [1,2,3]) -> list:
    q.append(w)
    return q

def foo2(q :list = [1,2,3,4]) -> int:
    e = 0
    for item in q:
        e += item
    return e

print(foo2())