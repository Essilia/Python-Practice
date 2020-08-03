# import time
# import random


# a=random.randint(1,4)
# print(a)


# 定义方法
#def 方法名(参数1，参数2)：   //参数可加可不加
#逻辑代码块
def jiafa(a,b):
    return a+b       #return返回值
a=jiafa(1,2)
print(1,"+",a,"=")

#定义类
#class 类名():  //类名的首字母要大写
# 面向对象编程
class Car():
    def __init__(self,pinpai,yanse,neishi,jilun):
        self.pinpai=pinpai
        self.yanse=yanse
        self.neishi=neishi
        self.jilun=jilun
    def bianxing(self):
        print("车子会变成喜羊羊")
    def fly(self):
        print("车子开始起飞！")

Essilia=Car("劳斯莱斯","红色","豪华","四轮")

   