#1.定义一个类
class Washer():
    # width=200
    # height=300
    #初始化功能函数
    def __init__(self,width,height):
        #添加属性
        # self.width=200
        # self.height=300
        self.width=width
        self.height=height

    # 打印对象时，默认返回return中的数据
    def __str__(self):
        return '这是海尔洗⾐机的说明书'
    def __del__(self):
        print(f'{self}对象已经被删除')
    #方法
    def wash(self):
        print('我会洗衣服')
        print(self)
    def print_info(self):
        print(f'haier1洗⾐机的宽度是{self.width}')
        print(f'haier1洗⾐机的⾼度是{self.height}')


#2.创建对象--实例化
haier1 = Washer(100,200)
#print(haier1)#打印对象在内存中的地址
haier1.wash()
# haier2=Washer()
# print(haier2)
# haier1.width=500
# haier1.height=800
# print(f'haier1洗⾐机的宽度是{haier1.width}')
# print(f'haier1洗⾐机的⾼度是{haier1.height}')
#haier1.print_info()