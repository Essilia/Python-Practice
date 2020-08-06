"""print("Hello World!")
print(1,123.12,False)
print(())#元组
print([])#数组
print({})#字典

锄禾日当午，汗滴禾下土

print("哈哈"+"嘻嘻")
print("嘻嘻"*100)
print((1+2)*9/2)
print(1>2)
print(1<2)
print(0<1<2)
print(3<1<2)
#变量
#赋值
name="张三" #把张三这个值赋值给了名字叫name的变量
print(name)

#input()方法所获取的值的数据类型固定为字符串，可以根据实际需求转化数据类型
a=input("请输入：")
print("input获取到的内容：",a)

a=float(input("请输入："))
b=float(input("请输入："))
print("input获取到的内容：",a+b)

#len()方法只能用于数据类型为字符串、元组、数组、字典
a="{1,2,3}"
print(len(a))

# 练习：通过代码获取两段内容，并且计算他们长度的和
a=len(input("请输入："))
b=len(input("请输入："))
print("input获取到的两个数据长度的和为",a+b)
"""
#元组 下标（从0开始编号）
# a=(1,2,3,4,"嘻嘻","嘻嘻","嘻嘻","嘻嘻","哈哈")
# print(a[-2])
#切片
# print(a[0:4])#左闭右开
# print(a[4:8])
# print(a[:])
# print(a[8:])
# print(a.index("嘻嘻"))#index()方法里面只能填一个数值，查找数据的下标
# print(a.count(0))#count()方法统计数量
#二维元组
# b=(a,"嘻嘻","哈哈")
# print(b[0][4])
#元组的数据具有不可修改性，它的好处在于它的不可修改性
#当元组只有一个元素时，例:t=(1),定义的不是tuple，而是"1"这个数，所以必须加一个逗号t=(1，)来消除歧义


#数组/列表(list)
# 1、增加数据
# 2、修改数据
# 3、剪切数据
# 4、删除数据
# a=[1,2,3,4,"嘻嘻","嘻嘻","嘻嘻","嘻嘻","哈哈"]
# print(a[2])
# a.append("append") #在数组的尾端增加数据
# a.append("append2")
# a.insert(0,"insert") #在数组的某个位置插入数据

# b=a.pop(0) #剪切
# c=a.pop(0) pop也可以用作删除指定序号的内容
# print(b+c)

# a.clear()  clear删除所有数据
# dd=[1,2,3,4]

#del a[0] 删除指定序号的内容，index方法必须是整数或者是切片

# a.extend(dd) #合并数组
# print(a+dd)

# a.remove("哈哈") #删除某个值
# print(a)

# xx=[0,1,False,True]
# a=xx.count(1)
# print(a)

"""
字典的特点
1、字典中的值没有顺序
2、字典的结构必须是 键对值的结构。eg：key:value 
3、字典的取值是通过key去定义value
4、字典的作用是：
  1、增加数据
  2、修改数据
  3、剪切数据
  4、删除数据	
"""
# a={"name":"张三",
# "age":45,
# "sex":"男"}
# #取值
# print(a["name"])
# #新增
# a["high"]=183
# print(a)
# #修改
# a["name"]="李四"
# print(a)

# b=a.get("name11") #get()方法如果取一个不存在的值会返回一个空值，而key会报错
# print(b)
# print(a["name11"])

# b=a.pop("name")
# print(b)
# print(a)

# a.update(name=1111) #这里的name相当于一个变量
# print(a)
# a.update({"name":1111})
# print(a)

# del a["age"]  字典的删除
# print(a)

# del a[0]  数组的删除
# print(a)

#不可变对象：整数、字符串
#不可变是指变量指向的对象内容不变
# a=['2','3','1']
# b=a.sort()
# print(b)
# student={"name1":"一一","name2":"二二","name3":"三三"}
# print("name1" in student)

#abs：绝对值
# print(abs(-1))

#max、min：最大值和最小值
# a={1,2,3}
# print(min(a))



#占位符%（常见的占位符有：%d(整数),%s(字符串),%f(浮点数)）
# 方法一：print("你好,%s,你的成绩比上次提高了%.1f %%,恭喜你！" % ("Essilia",1.8))
# 方法二：print('你好，{0},你的成绩对比上次提升了{1:.1f}%,{2}{3}'.format("Essilia",17.152,"请继续加油！","特别棒！"))
