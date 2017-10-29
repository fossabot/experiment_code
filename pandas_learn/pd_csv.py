#coding: utf-8
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import sys

df = pd.read_csv('ex1.csv')
print df


df_read_table = pd.read_table('ex1.csv',sep=',')
print df_read_table

nohead_csv = pd.read_csv('no_head_csv.csv',header=None)
print nohead_csv


nohead_csv = pd.read_csv('no_head_csv.csv',names=['a','b','c','d','message'])
print nohead_csv

names = ['a','b','c','d','message']
nohead_csv = pd.read_csv('no_head_csv.csv',names=names,index_col='message')
print nohead_csv


parsed = pd.read_csv('csv_mindex.csv',index_col=['key1','key2'])
print parsed

result = pd.read_csv('big_csv.csv',nrows=5)
print result

chunker = pd.read_csv('big_csv.csv',chunksize=500)
print chunker

tot = Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(),fill_value=0)

tot = tot.sort_values(ascending=True)
print tot



data = pd.read_csv('ex1.csv')
print data
data.to_csv('out.csv')
data.to_csv(sys.stdout,sep='|')
print data.to_csv('out2.csv',index=False,header=False)

dates = pd.date_range('1/1/2017',periods=7)
ts = Series(np.arange(7),dates)
print ts
ts.to_csv('tseries.csv')

