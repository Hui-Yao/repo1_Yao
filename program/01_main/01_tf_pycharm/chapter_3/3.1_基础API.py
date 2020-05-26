import numpy as np
import tensorflow as tf
from tensorflow import keras

#tf.constant
#
const = tf.constant([[1., 2., 3., 4., ], [5., 6., 7., 8., ]])

#索引方法
print('索引方法'.center(50,'*'))

print(const)  #constant创建的对象是tf.tensor类型的
print(const[:,1:3])
print(const[...,1:]) #省略号  ‘...’ 代表前面所有的引号


#算术操作
#加减乘除是对每个元素进行的；平方是每个元素平方；通过tf.tranpose函数求转置。
print('算术操作'.center(50,'*'))

print(const+10)
print(const*2)
print(const/3)
print(tf.square(const))
print(const@tf.transpose(const))


#将np.ndarray数据转化为constant类型
print('转换'.center(50,'*'))

np_ = np.arange(8).reshape(2,4)
np_c = tf.constant(np_)
print(type(np_))    #<class 'numpy.ndarray'>
print(type(np_c))   #<class 'tensorflow.python.framework.ops.EagerTensor'>


#0维数据（scalar）
print('0维数据'.center(50,'*'))

scalar_constant = tf.constant(3.14)
print(type(scalar_constant))
print(scalar_constant.shape)

# strings
print('字符串'.center(50,'*'))

strings_constant = tf.constant("cafe")
print(strings_constant)
print(tf.strings.length(strings_constant))
print(tf.strings.length(strings_constant, unit="UTF8_CHAR"))
print(tf.strings.unicode_decode(strings_constant, "UTF8"))
'''
tf.strings.length(input, unit='BYTE')
    函数的作用是统计字符串的长度。
    input：可以使一个字符串，也可以是字符串列表
    unit：长度的单位。默认是BYTE（for the number of bytes in each string）；
          ‘UTF8_CHAR’表示用编码后的utf8码（for the number of UTF-8 encoded Unicode code points in each string）

'''


# string array
print('字符串数组'.center(50,'*'))

t = tf.constant(["cafe", "coffee", "咖啡"])
print(tf.strings.length(t, unit="UTF8_CHAR"))
r = tf.strings.unicode_decode(t, "UTF8")
print(r)
'''
上面第二个输出语句输出的结果是一个二维数据，但是每一行的数据的元素个数不相同，那么把这种数据类型就叫做RaggedTensor
<tf.RaggedTensor [[99, 97, 102, 101], [99, 111, 102, 102, 101, 101], [21654, 21857]]>
'''

# ragged tensor
print('ragged tensor'.center(50,'*'))
r = tf.ragged.constant([[11, 12], [21, 22, 23], [], [41]])
# index op
print(r)
print(r[1])
print(r[1:2])

#concatenate of ragged tensor
r1 = tf.ragged.constant([[1, 2], [3, 5, 6], [], [7, 8]])
r2 = tf.ragged.constant([[9, 10,], [11, 12 ,13 ,], [], [14, 15, 16]])
r3 = tf.concat([r1, r2], axis = 0) #在零轴上进行拼接即为行的累叠
r4 = tf.concat([r1, r2], axis = 1) #在1轴上进行拼接即为宽度上的延伸，能进行拼接的前提是两个对象的行数相同
print('r3:',r3)
print('r4:',r4)

#convert ragged tensor to tensor
t5 = r1.to_tensor()
print('t5:',t5)
#ragged.to_tensor（）方法会把宽度小的行自动补零，以达到和最宽的行一样的宽度，但是实数全都在0的前面。

#sparse tensor
s1 = tf.sparse.SparseTensor()



'''tf.sparse.SparseTensor(indices, values, dense_shape)
    作用是创建稀疏tensor。

    

'''

