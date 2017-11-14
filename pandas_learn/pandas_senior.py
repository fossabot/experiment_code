

import pandas as pd
import numpy as np
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))


df['E'] = np.where(df['D'] >= 0, '>=0', '<0')
df['F'] = np.random.randint(0, 2, 6)
df.assign(G = df.A * df.D) # 或者
df['F'] = df['F'].apply(str) #针对单列的
df.applymap(str) #这个相当于是mutate_each

pd.value_counts(df["E"])
pd.pivot_table(df,index=['E','F'])


df.set_index(['A'], drop = 0, append = 1) # 把已有的列设置为index，可保留之前的index，也可以把新的index在原数据中删除
df['dates'] = df.index # 新生成一列dates



df2 = df.drop('dates', axis = 1) # 可以删除多列

df3 = df.drop(df.index[[1,3]])

df2.columns
df2.columns = ['a', 'b', 'c', 'e', 'd', 'f'] # 重命名

df2 = df2.rename(columns = {'a':'aa','b':'bb', 'c':'cc', 'd':'dd', 'e':'ee', 'f':'ff'})


pd.Series(['a|b', np.nan, 'a|c']).str.get_dummies()


df.values
df.get_values()

df.describe() # 只会针对数值型变量做计算

df4=pd.DataFrame([[5,6],[7,8]],columns=list('AB'))
df.append(df4, ignore_index=True)

df.groupby(['E','F']).mean()
df.groupby(['E','F']).agg(['sum', 'mean'])
pd.pivot_table(df,index=['E','F'], aggfunc=[np.sum, np.mean])
df.pivot_table(index=['E','F'], aggfunc=[np.sum, np.mean]) # 同上
df.groupby(['E','F']).agg({'A':['mean','sum'], 'B':'min'}) # groupby 也可以这样写

df.sort_values(['A','B'],ascending=[1,0]) # 按列排序，na_position控制NAN的位置
df.sort_index(ascending=0) # 按index排序

df[(df.A >= -1) & (df.B <= 0)] # 值筛选
df[df.E.str.contains(">")] # 包含某个字符，contains筛选的其实是正则表达式
df[df.F.isin(['1'])] # 在列表内

df['A'] # 单个的列
df[0:3] # 行
df['20130102':'20130104'] # 按index筛选
df.loc[:,] # 类似于R里面的dataframe选行和列的方法
print(df.iloc[:,]) # iloc只能用数字了
