class Master():
    def __init__(self):
        self.kongfu='[五香煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
#学校类
class School(Master):
    def __init__(self):
        self.kongfu='[香辣煎饼果子]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
        super().__init__()
        super().make_cake()
#徒弟类
class Prentice(School):
    def __init__(self):
        self.kongfu='[独创煎饼果子配方]'
    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')
    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)
    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)
    def make_old_cake(self):
        super().__init__()
        super().make_cake()


xiaoming=Prentice()
xiaoming.make_old_cake()
print(Prentice.__mro__)

