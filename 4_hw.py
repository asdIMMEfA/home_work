class rectangle:
    def __init__(self, q, w):
        self.q = q
        self.w = w
    def s(self):
        return self.q * self.w
    def p(self):
        return 2 * (self.q + self.w)

asdf = rectangle(4, 5)
print(asdf.s())
print(asdf.p())

asdf1 = rectangle(4, 10)
print(asdf1.s())
print(asdf1.p())

asdf2 = rectangle(123, 10)
print(asdf2.s())
print(asdf2.p())

class Math:
    def __init__(self, a:int, b:int) -> None:
        self.a = a
        self.b = b
    def addition(self):
        return self.a + self.b
    def subtraction(self):
        return self.a - self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        return self.a / self.b

class Button:
    def __init__(self, a:str, type:str = 'Кнопка', locator = '') -> None:
        self.a = a
        self.type = type
    def display_text(self):
        print(self.a)
    def click(self):
        if self.type == 'Кнопка':
            Button.display_text(self)
            print('Клик!')

