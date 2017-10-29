#coding: utf-8
import pandas as pd
import numpy as np

dates = pd.date_range('20170101',periods=6)
print dates
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print df.head()

print df.tail(2)
print df.describe()

print df.T
print df.sort_index(axis=1,ascending=False)

print df['A']