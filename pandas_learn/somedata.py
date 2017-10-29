# coding: utf-8
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

obj = Series([4,5,6,7])
print obj.values
print obj.index

obj2 = Series([4,5,-6,7,8],index=['a','b','c','d','e'])
print obj2
print obj2.index
print obj2['b']
print obj2[obj2 > 0]
print obj2 * 2
print np.exp(obj2)
print 'b' in obj2
print 'f' in obj2



sdata = {'yang':35000,"zhi":23000,"wei":12122}
obj3 = Series(sdata)
print obj3
name = ['yang','zhi','wei','coo']
obj4 = Series(sdata,index=name)
print obj4

print pd.isnull(obj4)
print pd.notnull(obj4)

print obj3 + obj4

obj4.name = 'population'
print obj4.name

obj4.index.name = 'state'
print obj4.index.name
print obj4.index

obj.index = ['bob','steve','jeef','ryan']
print obj
