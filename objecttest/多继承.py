# class Master():
#     def __init__(self):
#         self.kongfu='[五香煎饼果子配方]'
#     def make_cake(self):
#         print(f'运用{self.kongfu}')
#
#
# class Prentice(Master):
#     pass
# xiaoming=Prentice()
# print(xiaoming.kongfu)
# xiaoming.make_cake()
#师傅类
class Master():
    def __init__(self):
        self.kongfu='[五香煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
#学校类
class School():
    def __init__(self):
        self.kongfu='[香辣煎饼果子]'
    def make_cak3e(self):
        print(f'运用{self.kongfu}制作煎饼果子')
#徒弟类
class Prentice(Master,School):
    pass

xiaoming=Prentice()
print(xiaoming.kongfu)
xiaoming.make_cak3e()
#当一个类有多个父类的时候，默认使用第一个类的属性和方法

#如果调用的时候选择其他的方法，是怎么进行的

