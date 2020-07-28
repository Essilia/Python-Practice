# 练习1：通过代码获取两段内容，并且计算他们长度的和
a=len(input("请输入："))
b=len(input("请输入："))
print("input获取到的两个数据长度的和为",a+b)


# 练习2：教务系统需要录入10个学生的成绩
# 这10个学生的姓名分别是一一、二二、三三、四四、五五、六六、七七、八八、九九、十十
# 名字要与成绩对应上
# 同时需要按照大于60和小于60分开存放数据
HighGrape={}
LowGrape={}
StudentName=["一一","二二","三三","四四","五五"]
a=0
while a<len(StudentName):
    StudentGrape=float(input("请输入学生"+StudentName[a]+"的成绩:"))
    if StudentGrape>=60:
        HighGrape[StudentName[a]]=StudentGrape
    else:
        LowGrape[StudentName[a]]=StudentGrape
    a=a+1
print("大于60分：",HighGrape)
print("小于60分：",LowGrape)


#修改代码