class Dog():
    def work(self):
        print('指哪打那')

class ArmyDog(Dog):
    def work(self):
        print('追击敌人')

class DrugDog(Dog):
    def work(self):
        print('追查毒品')


class Person():
    def work_with_dog(self,dog):
        dog.work()

ad=ArmyDog()
dd=DrugDog()
daqiu=Person()
daqiu.work_with_dog(ad)
daqiu.work_with_dog(dd)