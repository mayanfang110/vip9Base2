# class A():
#     def __init__(self):
#         self.num=1
#     def info_print(self):
#         print(self.num)
# class B(A):
#     pass
#
# result=B()
# result.info_print()


class Master():
    def __init__(self):
        self.kongfu='[五香煎饼果子配方]'
    def make_cake(self):
        print(f'运用{self.kongfu}制作五香煎饼果子配方')

class Prentice(Master):
    pass
xiaoming=Prentice()
print(xiaoming.kongfu)
xiaoming.make_cake()
mst=Master()
mst.make_cake()