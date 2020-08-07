import time     #引入第三方time包
now=time.strftime("%y-%m-%d %H:%M:%S")     #获取当前系统时间：年月日用小写，时分秒用大写
text=input("请输入今天的心情：")
with open("F:\日记.txt","a",encoding="utf-8") as f:
    f.write(now+"\n")
    f.write(text+"\n")
    f.write("......................."+"\n")

