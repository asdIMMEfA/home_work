def foo(q :int, w:int) -> int:
    return max(q,w)

def foo2(q :int, w:int) -> None:
    if abs(q - w) == 135:
        print('yes')
    else:
        print('no')

def foo3(q :int) -> None:
    match q:
        case 12,1,2:
            print('зима')
        case 3,4,5:
            print('весна')
        case 6,7,8:
            print('лето')
        case 9,10,11:
            print('осень')
        case _:
            print('Укажите номер месяца от 1 до 12')

def foo4(q :int, w:int,e:int) -> None:
    if (q>10) & (w>10) & (e>10):
        print('yes')
    else:
        print('no')

def foo5(q :list = [1,2,3,4,5]) -> int:
    count = 0
    for x in q:
        if x > 0:
            count += 1
    return count

def foo6(q:int,w:int) -> int:
    return q * w * 29
