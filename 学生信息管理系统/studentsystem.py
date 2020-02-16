# _*_ coding=utf-8 _*_
#开发者：3singlewolf
#开发时间：2020-02-13
#开发工具：pycharm

import  re  #导入正则表达式模块
import os   #导入操作系统模块

filename="student.txt"


def menu():
# 显示功能菜单
    print('''
    ╔—————————————————学生信息管理系统—————————————————╗
    ┃     ================功能菜单================      
    ┃                                                 
    ┃  选项                                           
    ┃   1    录入学生信息                              
    ┃   2    查找学生信息                               
    ┃   3    删除学生信息                              
    ┃   4    修改学生信息                              
    ┃   5    排序                                               
    ┃   6    统计学生人数                              
    ┃   7    显示所有学生信息                         
    ┃   0    退出系统                                 
    ┃                                               
    ┃   ========================================     
    ┃   说明：通过数字或↑↓方向键选择菜单                
    ╚———————————————————————————————————————————————╝    
    ''')

#主函数
def main():
    ctrl=True
    while(ctrl):
        menu()  #显示
        option= input("请选择：")  #选择菜单项
        option_str= re.sub("[^0-9]","",option)
        #正则表达式匹配，功能：删除非数字内容，提取数字
        if option_str in ['0','1','2','3','4','5','6',"7"]:
            option_int = int(option_str)
            if option_int == 0:
                print("您已退出学生成绩管理系统")
                ctrl=False
            elif option_int == 1:  #录入
                insert()
            elif option_int == 2:  #查找
                search()
            elif option_int == 3:  #删除
                delete()
            elif option_int == 4:  #修改
                modify()
            elif option_int == 5:  #排序
                sort()
            elif option_int == 6:  #统计学生总数
                total()
            elif option_int == 7:  #显示所有学生信息
                show()



'''   1    录入信息'''

# 录入信息
def insert():
   stdentList = []  #保存学生信息的列表
   mark = True  #是否继续添加
   while mark :
       id = input("请输入ID 如（1001）：")
       if not id : #id 为空，跳出循环
         break
       name = input("请输入名字：")
       if not name:
           break
       try:
           english = int(input("请输入英语成绩："))
           python = int (input("请输入python成绩："))
           c =int(input("请输入C语言成绩："))
       except:
           print("输入无效，不是整数数值........请您重新录入信息")
           continue
       #将输入的学生信息保存到字典
       stdent = {"id":id,"name":name, "english":english,"python":python,"c":c}
       stdentList.append(stdent)#将学生字典添加到列表中
       inputMark=input("是否继续添加？（y/n）:")
       if inputMark=="y": #继续添加
           mark =True
       else: #不继续添加
           mark =False
   save(stdentList)
   print("学生信息录入完毕！！！")


#保存信息
def save(student):
    try:
        student_txt=open(filename,"a")
    except Exception as e:#万能异常Exception，只要有异常就触发
        student_txt=open(filename,"w") #文件不存在，创建文件并打开
    for info in student:
        student_txt.write(str(info)+"\n") #按行存储，添加换行符# write（）将一个字符串或字符流写入
    student_txt.close()#关闭文件



'''  2 查找学生成绩信息  '''

# 查找信息
def search():
    mark = True
    student_query = [] #保存查询结果的学生列表
    while mark:
        id = ""
        name = ""
        if os.path.exists(filename): #判断文件是否存在
            mode =input("按ID查输入1；按姓名查询输入2：")
            if mode  == "1":
               id =input("请输入学生ID：")
            elif mode =="2":
                name =input("请输入学生姓名：")
            else:
                print("您输入有误，请重新输入！")
                search() #重新查询
            with open(filename,"r") as file: #打开文件
                student = file.readlines() # 读取全部内容
                for list in student :
                    d = dict(eval(list)) #字符串转字典
                    if id != "":#判断是否按ID查
                       if d["id"] == id:
                           student_query.append(d)#将找到的学生信息保存到列表中
                    elif name != "":  # 判断是否按姓名查
                        if d["name"]==name:
                            student_query.append(d)#将找到的学生信息保存到列表中
                show_stdent(student_query)# 显示查询结果
                student_query.clear() #清空列表
                inputMark = input(" 是否继续查询？（y/n）:")
                if inputMark == "y":
                    mark = True
                else:
                    mark =False
        else:
            print("数据为空，暂未保存信息......")
            return  # 结束执行退出函数


''' 3 删除学生成绩信息 '''

# 删除信息
def delete():
   mark =True
   while mark:
       studentId=input("请输入要删除的学生ID：")
       if studentId !="":
           if  os.path.exists(filename):
               with open(filename,"r") as rfile:
                   student_old = rfile.readlines()
           else:
               student_old =[]
           ifdel =False
           if student_old:
               with open(filename,"w") as wfile:
                   d={}
                   for list in student_old:
                       d=dict(eval(list))
                       if d["id"] != studentId:
                           wfile.write(str(d)+"\n")#不是删除的id就覆盖写入
                       else:
                           ifdel =True
                   if ifdel:
                       print("ID为%s 的学生信息已经被删除..."% studentId)
                   else:
                       print("没有找到ID为%s的学生信息..."%studentId)

           else:
               print("无学生信息...")
               break #跳出当前循环
           show()
           inputMark = input("是否继续删除？（y/n）:")
           if inputMark == "y":
               mark = True
           else:
               mark = False


# 修改信息
def modify():
   show()
   if os.path.exists(filename):
       with open(filename,"r") as rfile:
           student_old = rfile.readlines()
   else:
       return  #遇到return函数就结束了
   studentid = input("请输入要修改的学生ID：")
   with open(filename,"w") as wfile:
       for student in student_old:
           d =dict(eval(student))
           if d["id"] == studentid:
               print("找到了这名学生，可以修改他的信息！")
               while True:
                   try:
                       d["name"]=input("请输入姓名：")
                       d["english"]=int(input("请输入英语成绩："))
                       d["python"]=int(input("请输入python成绩："))
                       d["c"]=int(input("请输入C语言成绩："))
                   except:
                       print("您的输入有误，请重新输入：")
                   else:
                       break
               student = str(d)
               wfile.write(student+"\n")
               print("修改成功！")

           else:
               wfile.write(student)
       mark = input("是否继续修改其他学生信息？（y/n）：")
       if mark =="y":
           modify()
       else:
           return




# 排列信息
def sort():
   show()
   if os.path.exists(filename):
       with open(filename,"r") as file:
           student_old = file.readlines()
           student_new =[]
       for list in student_old:
            d= dict(eval(list))#eval能去除\n
            student_new.append(d)
   else:
       return
   paixu =input("请选择 （0 升序；1降序）：")
   if paixu == "0":
       paixub1=False
   elif paixu == "1":
       paixub1 =True
   else:
       print("您的输入有误，请重新输入！")
       sort()
   mode = input("请选择排序方式（1按英语成绩排序；2按Python成"
                "绩排序；3按C语言成绩排序；0按总成绩排序）："
                )
   if mode == "1":
       student_new.sort(key=lambda x:x["english"],reverse=paixub1)
   elif mode =="2":
       student_new.sort(key=lambda x:x["python"],reverse=paixub1)
   elif mode == "3":  # 按C语言成绩排序
       student_new.sort(key=lambda x: x["c"], reverse=paixub1)
   elif mode == "0":  # 按总成绩排序
       student_new.sort(key=lambda x: x["english"] + x["python"] + x["c"], reverse=paixub1)
   else:
       print("您的输入有误，请重新输入！")
       sort()
   show_stdent(student_new)


''' 6 统计学生总数'''


def total():
    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, 'r') as rfile:  # 打开文件
            student_old = rfile.readlines()  # 读取全部内容
            if student_old:
                print("一共有 %d 名学生！" % len(student_old))
            else:
                print("还没有录入学生信息！")
    else:
        print("暂未保存数据信息...")


''' 7 显示所有学生信息 '''

def show():
    student_new =[]
    if os.path.exists(filename):
        with open(filename,"r") as rfile:
            student_old = rfile.readlines()
        for list in student_old:
            student_new.append(eval(list))
        if student_new:
            show_stdent(student_new)
    else:
        print("暂未保存数据信息...")




#将保存在列表中的学生信息显示出来
def show_stdent(studentList):
    if not studentList:
        print("(o@.@o) 无数据信息 (o@.@o) \n")
        return
    format_title="{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
    print(format_title.format("ID", "名字", "英语成绩", "Python成绩", "C语言成绩", "总成绩"))
    format_data = "{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}"
    for info in studentList:
        print(format_data.format(
            info.get("id"), info.get("name"),
            str(info.get("english")), str(info.get("python")),
            str(info.get("c")),
            str(info.get("english") + info.get("python") + info.get("c")).center(12)))


if __name__ == "__main__":
   main()
