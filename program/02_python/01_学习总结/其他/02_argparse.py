'''argparse:解析命令行参数
主要流程如下
import argparse  #导入模块

parser = argparse.ArgmentParser()  # 创建一个解释器对象

parser.add_argment('position argments', 'optional argments', \
help = 'the description of this argment', type = '', action = '~', choices = [~])
# 添加参数

args = parser.parse_args()  # 对解析器进行解析，得到参数

argparse.ArgmentParser()
    func:创建一个解析器对象
    params：description：用于插入描述脚本/程序用途的信息，可以为空

parse.add_argment(~)
    func:向解释器对象中添加添加需要的命令行参数和选项
    params：
    位置参数（position argment）：参数前不需要加-，比如
        parse.add_argment(‘epoch’，help = 'the epoch of train' )
        定义了一个变量名为e的参数;help为帮助信息，对参数进行解释
    可选参数(optional argment):参数前要加-/--，对应着缩写与全名，比如：
        parse.add_argment(‘-b’，'--bacth_size', help = 'the batch_size' )
        定义了一个可选参数，其缩写为b，全称为batch_size，从终端中输入时要以如下形式输入：
        python xxx.py -b(--batch_size) = xxx
    布尔值：需要在可选参数的基础上加上，使用参数action =‘xxx’，xxx是什么内容不重要，
            因为这个的用法是，当使用则个参数时，这个可选参数就代表True，不适用就代表False。
            parse.add_argment(‘-b’，'--bacth', action = 'hahaha' )
            python xxx.py -b(--batch)     batch这个参数就代表True，不用给这个可选参数传值
            python xxx.py                 此时batch代表False

    其他参数：
    type = ~， 如果不指定数据类型，则默认为string，
    choices = [x,x,x] ,参数只能从规定的数值中选
    default = None：默认值，当加上了这个选项的参数围在命令行中出现，则采用默认值。
    互斥参数：
        python xxx.py -b(--batch)  就会返回True，不用给这个可选参数传值









'''