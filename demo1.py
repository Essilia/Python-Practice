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
"""


#元组的数据具有不可修改性
"""
数组/列表(list)
1、增加数据
2、修改数据
3、剪切数据
4、删除数据
StudentName=["一一","二二","三三","四四","五五","六六","七七","八八","九九","十十"]
# StudentName.append("增加")
# StudentName.insert(1,"增加")
# StudentName[0]="修改"
# StudentName.remove("一一") remove删除具体的数据
# StudentName.pop(0) pop删除指定序号的内容
# StudentName.clear() clear删除所有数据
#del StudentName[0] 删除指定序号的内容 
"""

"""
字典（1、字典没有顺序这个概念 2、字典是以键值对的形式出现的）
1、增加数据
2、修改数据
3、剪切数据
4、删除数据

StudentName={"key1":"一一","key2":"二二","key3":"三三","key4":"四四","key5":"五五"}
# StudentName["Key6"]="增加"
# xx={"Key6":"增加"}
# StudentName.update(xx)
# StudentName["Key6"]="修改"
# StudentName.pop("key1")
# del StudentName["key1"]
# StudentName.clear()
print(StudentName)
"""
#for循环(*1、注意判断语句后面结尾需要加上冒号；2、注意代码之间的主从关系，需要缩进)
#range()可以创建一个整数列表，一般用于for循环中
# for i in list(range(79,101,2)):
#     print(i)

