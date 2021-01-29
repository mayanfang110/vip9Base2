# 1、打印小猫爱吃鱼，小猫要喝水
# 2、小明爱跑步，爱吃东西。
# 1）小明体重75.0公斤
# 2）每次跑步会减肥0.5公斤
# 3）每次吃东西体重会增加1公斤
# 4）小美的体重是45.0公斤
#1.定义一个猫类，方法：小猫爱吃鱼，小猫爱喝水
# class Cat():
#
#     def eat(self):
#         print('小猫爱吃鱼',end=',')
#
#     def drink(self):
#         print('小猫爱喝水')
#
# xiaohua=Cat()
# xiaohua.eat()
# xiaohua.drink()
#2.定义一个人类，
# 属性：体重
# 方法：小明爱跑步，爱吃东西
# class Person():
#     def __init__(self):
#         self.weight=75.0
#
#     #类里面获取对方属性
#     def tizhong(self):
#         print(f'小明的体重是{self.weight}公斤')
#     def xiaomei(self,):
#         print(f'小美的体重是{self.weight1}公斤')
#
#     def run(self):
#         print('小明爱跑步',end=',')
#     #定义吃东西的方法
#     def eat(self):
#         print('爱吃东西')
#     def runjianfei(self):
#         print(f'每次跑步会减肥0.5公斤，减肥后{self.weight-0.5}公斤')
#     def eatzengjia(self):
#         #b=self.weight+1
#         print(f'每次吃东西，体重会增加{self.weight+1}')
#
# #实例化对象
# xiaozhang=Person()
#
# xiaozhang.run()
# xiaozhang.eat()
# xiaozhang.tizhong()
# xiaozhang.runjianfei()
# xiaozhang.eatzengjia()
# xiaomei=Person()
# xiaomei.weight1=45.0
# xiaomei.xiaomei()
# # 3、摆放家具
# 需求：
# 1）.房子有户型，总面积和家具名称列表
#    新房子没有任何的家具
# 2）.家具有名字和占地面积，其中
#    床：占4平米
#    衣柜：占2平面
#    餐桌：占1.5平米
# 3）.将以上三件家具添加到房子中
# 4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表

# class Furniture():
#     def __init__(self,name,area):
#         #家具名字
#         self.name=name
#         #家具占地面积
#         self.area=area
#房子类
# class Home():
#     def __init__(self,house,area):
#         #地理位置
#         self.house=house
#         #总面积
#         self.area=area
#         #剩余面积
#         self.free_area=area
#         #家具名称列表
#         self.furniture=[]
#
#     def __str__(self):
#         return f'房子户型{self.house},总面积{self.area},剩余面积{self.free_area},家具有{self.furniture}'
#
#     def add_furnitue(self,item):
#         if self.free_area >item.area:
#             self.furniture.append(item.name)
#             self.free_area-=item.area
#         else:
#             print('家具太多，剩余积不⾜，⽆法容纳')
#
#
# jia1=Home('三室一厅',1200)
# print(jia1)
# bed=Furniture('床',4)
# jia1.add_furnitue(bed)
# print(jia1)
# yigui=Furniture('衣柜',2)
# jia1.add_furnitue(yigui)
# print(jia1)
# table=Furniture('餐桌',1.5)
# jia1.add_furnitue(table)
# print(jia1)
#4.士兵开枪
# 需求：
# 1）.士兵瑞恩有一把AK47
# 2）.士兵可以开火(士兵开火扣动的是扳机)
# 3）.枪 能够 发射子弹(把子弹发射出去)
# 4）.枪 能够 装填子弹 --增加子弹的数量
#类：士兵类，墙类
#士兵类：方法：开火
#枪类：方法：可以发射子弹，装填子弹
class Soldier():
    def hava(self):
        print('士兵瑞恩有一把AK47')
    def fire(self):
        print('士兵可以开火')
class gun():
    def transmit(self):
        print('枪能够发射子弹')
    def fill(self):
        print('枪能够装填子弹')
a=Soldier()
a.hava()
a.fire()
b=gun()
b.transmit()
b.fill()



