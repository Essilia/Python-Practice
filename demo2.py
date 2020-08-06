#三种判断方式
#if； if else； if elif else
# a=int(input("请输入你的年龄："))
# if a<=1:  #判断的条件后面必须加冒号
#     print("你是一个宝宝")
# else:
#     print("你是一个孩子")

# if a<=3 : 
#     print("你是一个宝宝")
# elif a>3 and a<8:
#     print("你是一个孩子")
# else:
#     print("你是一个青少年")

# a=input("请输入数字：")    in的用法
# if a=="":
#     print("数据不能为空")
#     exit()
# if a in "0123456789":
#     a=int(a)
# else:
#     print("请输入正确的数字！")
#     exit()
# if a>4:
#     print("大")
# else:
#     print("小")

# a=False              #is用来判断数据的数据类型
# if type(a) is int:
#     print("是数字！")
# elif type(a) is str:
#     print("是字符串！")
# else:
#     print("其他")


#循环
#for...in...循环(*1、注意判断语句后面结尾需要加上冒号；2、注意代码之间的主从关系，需要缩进)
#range()可以创建一个整数列表，一般用于for循环中
# for i in list(range(79,101,2)):
#     print(i)

# a=10
# while a>10:
#     print("恭喜发财！")
#     a=a-1

#循环和判断嵌套使用
# name=input("请输入学生姓名：")
# grade=input("请输入学生成绩：")
# userinfo={name:grade}
# if grade>60:
#     print("大于60分的学生有"+str(userinfo))
# else:
#     print("小于于60分的学生有"+str(userinfo))
# while userinfo[name]=10:
#     print(userinfo)

# x=range(10)  
# for i in x:
#     if i==5:
#         break
#     print(i)

# 包-模块-类-方法-变量
"""
try: 
    print(1+"2")         # try/except：捕获异常的方法
except Exception as e:   #Exception是异常类，用来说明捕获到的异常原因
        print("你的代码有错误",e)
"""

#异常的主要作用是处理用户的输入，例如数据库的输入语句
try:
    a=input("请输入你的名字：")
    b=int(input("请输入你的年龄："))
    print(a,b)
except:
    print("请输入正确的姓名和年龄！")



