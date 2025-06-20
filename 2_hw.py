def task_1() -> int:
    q :int = 0
    w :float = 0
    e :str = 'asd'
    r :list = [1,2,3]
    t : bool = False
    print(type(q))
    print(type(w))
    print(type(e))
    print(type(r))
    print(type(t))
task_1()

def task2():
    a = [1, 2, 3, 5, 8, 13, 21]
    print(a[0-2])
task2()

def task3(q :int) -> int:
    print('Function task3 called!')
    return q ^ 2
task3(0)