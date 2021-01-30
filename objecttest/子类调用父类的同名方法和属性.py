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
class Prentice(Master,School):
    def __init__(self):
        self.kongfu='[独创煎饼果子配方]'
    def make_cak3e(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')
    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)
    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

xiaoming=Prentice()
print(xiaoming.kongfu)
xiaoming.make_cake()
xiaoming.make_master_cake()
xiaoming.make_school_cake()
xiaoming.make_cake()
#子类和父类具有同名属性和方法，默认使用子类的同名属性和方法