def roman_int(s):
    roman2int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    for index in range(len(s) - 1):
        if roman2int[s[index]] < roman2int[s[index + 1]]:
            res -= roman2int[s[index]]
        else:
            res += roman2int[s[index]]
    return res + roman2int[s[-1]]
    # roman_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M', ]
    # int_list = [1, 5, 10, 50, 100, 500, 1000]
    # roman2int = dict(zip(roman_list, int_list))
    # res = 0
    # for index in range(len(s) - 1):
    #     if roman2int[s[index]] < roman2int[s[index + 1]]:
    #         res -= roman2int[s[index]]
    #     else:
    #         res += roman2int[s[index]]
    # res += roman2int[s[index + 1]]              #这一句的错误在于index是for循环中定义的变量，再外层没有定义，所以不能使用
    # return res                                  #应该用 res += roman2int[s[-1]]

print(roman_int('MCMXCIV'))

'''
本体思路：
1.通过定义一个字典，表示罗马数字与数字之间的映射关系
2.通过判断语句考虑罗马数字的特殊情况
3.以一个累加来统计随后的计算结果

'''

