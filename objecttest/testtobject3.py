#师傅类
class Master():
    def __init__(self):
        self.kongfu='[五香煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作五香煎饼果子配方')
#学校类
class School():
    def __init__(self):
        self.kongfu='[香辣煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作香辣煎饼')

#独创类
class Prentice(Master,School):
    def __init__(self):
        self.kongfu = '[独家煎饼果子配方]'

    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作独创')

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)
    def make_schoole_cake(self):
         School.__init__(self)
         School.make_cake(self)



xiaoming=Prentice()
print(xiaoming.kongfu)
xiaoming.make_cake()
# mst=Master()
# mst.make_cake()
#print(Prentice.__mro__)
xiaoming.make_master_cake()
xiaoming.make_schoole_cake()