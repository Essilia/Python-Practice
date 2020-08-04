class Car():
    # def __init__(self,pinpai,yanse,neishi,jilun):   #默认属性方法_init_
    #     self.pinpai=pinpai
    #     self.yanse=yanse
    #     self.neishi=neishi
    #     self.jilun=jilun
    def bianxing(self,xi,lan,zhuang):
        self.xi=xi
        self.lan=lan
        self.zhuang=zhuang
    def fly(self):
        print("车子开始起飞！")

# Essilia=Car("劳斯莱斯","红色","豪华","四轮")  #实例化对象，Essilia变量指向的就是一个Car的实例化
# Essilia=Car("喜羊羊","懒羊羊","壮羊羊")
# print(Essilia.xi)
Essilia=Car()
Essilia.fly()