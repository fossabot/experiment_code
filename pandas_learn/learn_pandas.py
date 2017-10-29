#coding: utf-8

"""
url: http://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/

"""
import pandas as pd
from pandas import DataFrame
import dateutil

data = pd.DataFrame.from_csv('/Users/jerry/Documents/mycode/pandas_learn/phone_data.csv')
data['date'] = data['date'].apply(dateutil.parser.parse, dayfirst=True)
# print data['date']
print data['item'].count()

print data['duration'][data['item']=='call'].sum()

print data['duration'].mean()

print data['month'].value_counts()
print data['network'].nunique()

print data.groupby('network').groups.keys()
print data.groupby('month').groups.keys()
print data.groupby('month').first()
print data.groupby('month')['duration'].sum()

print data.groupby(['month','item']).agg({'duration':"sum",'network_type':"count",'date':'first'})
aggregations = {
    'duration':'sum',
    'date': lambda x: max(x)

}
print data.groupby('month').agg(aggregations)

aggregations_2 = {
    'duration':{
    'total_duration':'sum',
    'average_duration':'mean',
    'num_calls':'count'
    },
    'date':{
        'max_date':'max',
        'min_date':'min',
        'num_days': lambda x:max(x) - min(x)
    },
    'network':["count","max"]
}
print data[data['item'] == "call"].groupby('month').agg(aggregations_2)
d = data[data['item'] == "call"].groupby('month')
# print dir(d)
print "-"*40
data[data['item'] == "call"].groupby('month').agg(aggregations_2).to_csv('~/111.csv')

print "-"*40
print data.groupby('month',axis=1).groups

