class Master():
    def __init__(self):
        self.kongfu='[五香煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
#学校类
class School():
    def __init__(self):
        self.kongfu='[香辣煎饼果子]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
#徒弟类
class Prentice(School,Master):
    def __init__(self):
        self.kongfu='[独创煎饼果子配方]'
        #私有属性
        self.__money=200000
        #获取私有属性
    def get_money(self):
        return self.__money

    def set_money(self):
        self.__money=500

    def __info_print(self):
        print(self.kongfu)
        #私有办法
        print(self.__money)
    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')
    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)
    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

class Tusun(Prentice):
    pass

xiaoming=Prentice()
xiaogang=Tusun()
print(xiaogang.get_money())
print(xiaogang.set_money())
print(xiaogang.get_money())