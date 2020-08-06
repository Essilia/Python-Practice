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


"""
练习3：获取用户输入的信息，并且存储到字典中
个人信息包括：name、age、sex
"""
name=input("请输入姓名：")
age=input("请输入年龄：")
sex=input("请输入性别：")
userinfo={"姓名":name,"年纪":age,"性别":"sex}
# userinfo.update(name=name,age=age,sex=sex)
print("您的用户信息为："+str(userinfo))

"""
1、九九乘法表
2、判断和循环语句的案例练习
(1)通过print打印，模拟一个红绿灯的功能，用倒计时的方式输出：红灯30次，绿灯35次，黄灯3次
(2)使用代码实现一个注册功能：用户输入账号和密码，要求账号长度在5-8位，密码6-12位，并且账号必须小写开头
"""

#3、定义一个方法，用来判断用户输入的用户名和密码是否正确
def userinfo(username,password):
    if len(username)>=5 and len(username)<=8:
        if username[0] in "qwertyuiopasdfghjklzxcvbnm":
            if len(str(password))>=6 and len(str(password))<=12:
                return True
            else:
                return "请输入正确的密码长度！"
        else:
            return "账号首位要以小写开头！"
    else:
        return "请输入正确的账号长度！"
        
print(userinfo("q111111",111112222))