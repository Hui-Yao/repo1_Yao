'''
题目描述：给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2**31,  2**31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

例子：
输入：123    -123    120
输出：321    -321    21
'''

# method1：字符串反转法
# class Solution:
#     def reverse(self, x: int) -> int:
#         x_ = str(x)
#         result = int(x_[1:][::-1] if x_.startswith('-') else x_[::-1])
#         return (result if result <= 2 ** 31 - 1 else 0) if x > 0 else (-result if -result >= -2 ** 31 else 0)
'''
1.通过str.startwith()方法识别数字转化成的字符串是否为负数
2.x_[1:][::-1]通过双重切片去除掉负数前的负号，并且得到一个与原字符串反序的字符串
    x_[1:]去除掉负数前的负号，str[::-1]不改变原字符串，并且返回一个与原字符串反序的字符串
3.三目运算符双重嵌套。需要注意的是内层三目中用来做判别条件的变量要符合外层的的判断结果，所指定的定义域。
    比如在return语句之前，得到的result的值为正，那么通过外层x>0的判决，执行左边括号的内容，在这个括号内，result与正数的2**31比较，result本身也为正值，
    所以不用对result进行操作。但是如果x<0，进入右边括号，那么说明原数为负数，则result前应加一个负号。
4. int(0012) = int(12)   int函数会直接去除前面的0

'''


# method2:除法计算法
# class Solution:
#     def reverse(self, x: int) -> int:
#         y, res = abs(x), 0
#         while y != 0:
#         res = res * 10 + y % 10
#         y //= 10
#         return (res if res <= 2 ** 31 - 1 else 0) if x > 0 else (-res if -res >= -(2 ** 31) else 0)
'''
1. %  取余，  //  取整
2.通过取余由低到高得到y各个位置上的数，逐轮乘10，使得y原本低位上的数升高到高位。

'''
