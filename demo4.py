"""
class 声明类的名字
类名的首字母必须大写
面向对象编程，这里的对象指的就是类
类里面的所有方法，都必须要传一个参数，叫self
封装、继承、重写/多态
"""

class Girlfreind(object): #object:祖师爷类，没有要继承的类，该类是默认值，_init_就是继承object的方法的
    """
    女朋友
    """
    def __init__(self,sex,high,age,weight,hair):
        """
        基本信息
        """
        self.sex=sex
        self.high=high
        self.age=age
        self.weight=weight
        self.hair=hair
    def skill(self,num):
        """
        个人技能
        """
        print("你性别为"+self.sex+"身高"+self.high+"年龄"+self.age+"，"+"体重"+self.weight+"，"+"留着"+self.hair+"的女朋友开始了")
        if num==1:
            print("胸口碎大石")
        elif num==1:
            print("拳击")
        else:
            print("吉他")

    def cooking(self):
        """
        厨艺
        """
        print("你性别为"+self.sex+"身高"+self.high+"年龄"+self.age+"，"+"体重"+self.weight+"，"+"留着"+self.hair+"的女朋友开始了")
        print("八大菜系，样样精通")

    def work(self):
        """
        工作
        """
        print("软件测试工程师")

#类的实例化/实例化对象
# Essilia=Girlfreind("女","160cm","18岁","45kg","黑色短发")
# Essilia.work()
# print(Essilia.sex)
# Essilia.skill(1)

class girlfriend(Girlfreind):  #继承
    pass                       #pass是占位符
zhangsan=girlfriend("男","180cm","18岁","60kg","黑色短发")
zhangsan.cooking()

class girlfriend(Girlfreind):  #重写
    def cooking(self):
        print("全能泡面王")                       
zhangsan=girlfriend("男","180cm","18岁","60kg","黑色短发")
zhangsan.cooking()


