class Car:
    def __init__(self, color:str, typ:type, year:int) -> None:
        self.color = color
        self.typ = typ
        self.year = year
    def run(self):
        print('Автомобиль заведен')
    def stop(self):
        print('Автомобиль заглушен')
    def change_year(self, q:int) -> None:
        if self.year != q:
            self.year = q
    def change_color(self, q:str) -> None:
        if self.color != q:
            self.color = q
    def change_typ(self, q:str) -> None:
        if self.typ != q:
            self.typ = q