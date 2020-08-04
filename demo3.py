# import time
# import random


# a=random.randint(1,4)
# print(a)


# 定义方法
#def 方法名(参数1，参数2)：   //参数可加可不加
#逻辑代码块
def jiafa(a,b):
    return a+b       #return返回值
c=jiafa(1,2)
print(1,"+",c,"=")

#定义类
#class 类名():  //类名的首字母要大写
#定义方法/函数   //类中的函数和普通函数的区别是第一个参数永远是self，并且调用时不用传递该参数
# 面向对象编程

class Car():
    def __init__(self,pinpai,yanse,neishi,jilun):   #默认属性方法_init_
         """
        车子的属性
        """
        print(""你"+self.yanse+"为红色的样式特别"+self.neishi+"盘带着"+self.jilun+self.pinpai")
        self.pinpai=pinpai
        self.yanse=yanse
        self.neishi=neishi
        self.jilun=jilun
    def bianxing(self,num):
        print(""你"+self.yanse+"为红色的样式特别"+self.neishi+"盘带着"+self.jilun+self.pinpai")
        if num==1:
            print("车子会变成喜羊羊")
        elif num==2:
            print("车子会变成懒羊羊")
        else:
            print("车子会变成壮羊羊")
    def fly(self):
        """
        车子会飞
        """
        print(""你"+self.yanse+"为红色的样式特别"+self.neishi+"盘带着"+self.jilun+self.pinpai")
        print("车子开始起飞！")

Essilia=Car("劳斯莱斯","红色的","豪华","四轮")  #实例化对象，Essilia变量指向的就是一个Car的实例化

Essilia.bianxing("666")
Essilia.fly()
print(Essilia.pinpai)


