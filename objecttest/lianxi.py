# # # class Washer():
# # #     def __init__(self,width,height):
# # #         self.width=width
# # #         self.height=height
# # #
# # #     def __del__(self):
# # #
# # #         print(f'{self}对象已经被删除')
# # # hair1=Washer(10,20)
# # # del hair1
# #
# #
# # #地瓜属性
# # class SweetPotato():
# #     def __init__(self):
# #         #被烤的时间
# #         self.cook_time=0
# #         #地瓜的状态
# #         self.cook_static=0
# #         #调料列表
# #         self.condiments=[]
# #
# #     def cook(self,time):
# #         self.cook_time+=time
# #         if 0<=self.cook_time<3:
# #             self.cook_static='生的'
# #         elif 3<=self.cook_time<5:
# #             self.cook_static='半生不熟'
# #         elif 5<=self.cook_time<8:
# #             self.cook_static='熟了'
# #         elif self.cook_time>=8:
# #             self.cook_static='烤糊了'
# #     def __str__(self):
# #         return f'这个地瓜烤了{self.cook_time},状态是{self.cook_static}'
# #
# #     def add_condiments(self, condiment):
# #         self.condiments.append(condiment)
# #
# #     def __str__(self):
# #         return f'这个地瓜烤了{self.cook_time}分钟,状态是{self.cook_static},添加的调料是是{self.condiments}'
# #
# # digua1=SweetPotato()
# #
# #
# # digua1.cook(2)
# # digua1.add_condiments('酱油')
# # print(digua1)
# #
# #
# # digua1.cook(2)
# # digua1.add_condiments('辣椒面')
# # print(digua1)
# #
# #
# # digua1.cook(2)
# # print(digua1)
#
#
#
# # 第二题
# class Ming():
#     def __init__(self,weight,weight1):
#         self.weight = weight
#         self.weight1 =weight1
#     def run(self):
#         print(f"小明爱跑步，爱吃东西")
#     def ming1(self):
#         print(f"小明体重是{self.weight}公斤")
#     def jianfei(self):
#         jianfei1 = self.weight - 0.5
#         print(f"每次跑步会减肥,减肥后是{jianfei1}公斤")
#     def chi(self):
#         chi1 = self.weight + 1
#         print(f"每次吃东西体重会增加，增加后体重是{chi1}公斤")
#     def mei(self):
#         print(f"小美体重是{self.weight1}公斤")
# ming2 = Ming(75,45)
# ming2.run()
# ming2.ming1()
# ming2.jianfei()
# ming2.chi()
# ming2.mei()
#
#
#


class Furniture():
    def __init__(self,name,area):
        #家具名字
        self.name=name
        #家具占地面积
        self.area=area

class Home():
    def __init__(self,address,area):
        #地理位置
        self.address=address
        #房屋面积
        self.area=area
        #剩余面积
        self.free_area=area
        self.furniture=[]

    def __str__(self):
        return f'房子坐落于{self.address},占地面积{self.area},剩余面试{self.free_area},家具有{self.furniture}'

    def add_furnitue(self,item):
        if self.free_area >item.area:
            self.furniture.append(item.name)
            self.free_area-=item.area
        else:
            print('家具太多，剩余积不⾜，⽆法容纳')

bed=Furniture('双人床',6)
jia1=Home('北京',1200)
print(jia1)
sofa=Furniture('沙发',10)
jia1.add_furnitue(sofa)
print(jia1)

ball=Furniture('篮球场',1500)
jia1.add_furnitue(ball)
print(jia1)

