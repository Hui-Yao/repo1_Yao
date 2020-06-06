#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

class Student:
    '''定义学生类'''
    def __init__(self,name,class_obj,balance):
        self.name = name
        self.class_obj = class_obj
        self.balance = balance

    def pay_tuition(self,class_obj):    #交学费并入学
        self.balance -= class_obj.course_obj.price
        print('{0} learns {1}(price:{2}),now he is one of the {3} members'.format\
                  (self.name,class_obj.course_obj.name,class_obj.course_obj.price,class_obj.name))

        class_obj.stu_list.append(self.name)    #加入班级学生列表
        self.class_obj.school_obj.stu_list.append(self.name)    #加入分校学生列表
        self.class_obj.school_obj.headquater.stu_list.append(self.name)     #加入总校区学生列表

    def query_balance(self):
        print('{}`s balance left {}...'.format(self.name,self.balance))

    def drop_out(self):
        print('i hate study...,now i`m free...')
        self.class_obj.stu_list.remove(self.name)

    def change_school(self):
        pass


class Teacher:
    '''定义老师类'''
    def __init__(self,name,salary,account):
        self.name = name
        self.salary = salary
        self.account = account

    def teaching(self):
        print('{} is teching class'.format(self.name))


class Staff:
    '''定义员工类'''
    def __init__(self,name,dept,school_obj,salary):
        self.name = name
        self.salary = salary
        self.dept = dept
        self.school_obj = school_obj

    def work(self):
        print('work for the school...')

    def new_staff_enrollment(self):
        print('now,{} has join {},congratulation!'.format(self.name,self.school_obj.name))
        self.school_obj.staff_list.append(self.name)
        self.school_obj.headquater.staff_list.append(self.name)

class Class_obj:
    '''课程'''
    stu_list = []
    def __init__(self,name,course_obj,school_obj):
        self.name = name
        self.course_obj = course_obj
        self.school_obj = school_obj
        self.school_obj.class_list.append(self.name)     #将本班级加入所在校区的班级列表
        self.school_obj.headquater.class_list.append(self.name)     #将本班级加入总校区班级列表

    def create_teach_record(self):
        pass


    # def new_stu_enrollment(self,student):
    #     print('{} has join {}...'.format(student.name,self.class_num))
    #     self.stu_list.append(student.name)
    def count_stu_num(self):
        print('there are {} students in {}'.format(len(self.stu_list),self.name))

class Course:
    '''课程'''
    def __init__(self,name,price):
        self.name = name
        self.price = price
    # def python(self):
    #     name = 'python'
    #     price = 5000
    #
    #
    # def java(self):
    #     name = 'java'
    #     price = 4000


class School:
    '''总部'''
    stu_num = 0
    staff_num = 0
    class_num = 0
    stu_list = []
    staff_list = []
    teacher_list = []
    class_list = []

    def __init__(self,name,address):
        self.name = name
        self.address = address

    def pay_roll(self):
        pass

    def count_staff_num(self):
        staff_num = len(self.staff_list)
        print('there are {} staff in this branchschool...'.format(staff_num))

    def count_class_stu_num(self):
        class_num = len(self.class_list)        #统计班级数

        for i in self.class_list:       #统计学生人数
            self.stu_num += len(self.class_list)
        print('there is {} class,{} students in this branchschool...'.format(class_num,self.stu_num))


class BranchSchool:
    '''分校'''
    stu_num = 0     #学生的初始人数为0
    staff_num = 0   #员工的初始人数为0
    stu_list = []   #学生列表
    staff_list = []     #员工列表
    teacher_list = []   #老师列表
    class_list = []     #班级列表

    def __init__(self,name,address,headquater):
        self.name = name
        self.address = address
        self.headquater = headquater


    def kick_out(self, student_name):
        self.stu_list.remove(student_name)
        print('student {} broken the role ,so he is expeled...'.format(student_name))

    def count_class_stu_num(self):
        class_num = len(self.class_list)  # 统计班级数
        for i in self.class_list:  # 统计学生人数
            self.stu_num += len(self.class_list)
        print('there is {} class,{} students in this branchschool...'.format(class_num, self.stu_num))

blue_grassland = School('blue_grassland','shanghai')    #总校区
wolf_castle = BranchSchool('wolf_castle','shenzhen',blue_grassland)    #分校
goat_village = BranchSchool('goat_village','beijing',blue_grassland)

python = Course('python',5000)  #课程
java = Course('java',4000)

class1 = Class_obj('class1',python,wolf_castle)   #创建班级
class2 = Class_obj('class2',java,goat_village)

stu1 = Student('mike',class1,10000)  #生成学员
stu2 = Student('jack',class2,20000)

teacher1 = Teacher('peter',8000,100000)      #生成老师
teacher2 = Teacher('benjamin',9000,50000)

staff1 = Staff('white','clean',wolf_castle,5000)    #生成工作人员
staff2 = Staff('black','cook',goat_village,5500)

wolf_castle.count_class_stu_num()
stu1.pay_tuition(class1)

print(wolf_castle.class_list)
print(goat_village.class_list)




# 如何让分校统计班的数量及人数，如何让总校区统计分校的各类人数






