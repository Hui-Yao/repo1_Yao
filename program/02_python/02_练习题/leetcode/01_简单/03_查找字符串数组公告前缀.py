# 正向方法，逆向方法，zip+set

# def min_prefix(strs):
#     result = ''
#     if strs == []:
#         return ''
#     for i,j in enumerate(strs[0]):
#         result += j
#         for k in range(1,len(strs)):
#             # if len(result) > len(strs[k]) or result != strs[k][:i+1]:
#             if len(result) > len(strs[k]) or j != strs[k][i]:
#                 return result[:-1]


# print(min_prefix(["flower","flow","flight"]))

# ["morning","dog","racecar","car"]

def min_prefix(strs):
    if len(strs) == 0:
        return ''
    for i in range(len(strs[0])):
        c = strs[0][i]
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != c:
                return strs[0][0:i]
    return strs[0]

print(min_prefix(['','']))