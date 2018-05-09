# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-09-09 21:03:21
# @Last Modified by:   jerry
# @Last Modified time: 2017-09-23 17:09:41

import pandas as pd

def get_csv(filename,path=None):
    df = pd.read_csv(filename)
    return df


def pandas_apply(data):
    # Convert date from string to date times
    data['date'] = pd.to_datetime(data['date'])
    return data

def main():
    filename = 'phone_data.csv'
    df = get_csv(filename)
    data  = pandas_apply(df)
    
    print data['item'].count()
    
    print zzdata['duration'].max()
    print data['duration'][data['item']=='call'].sum() # How many seconds of phone calls are recorded in total?
    print data['month'].value_counts() # How many entries are there for each month?
    print data['network'].nunique() # Number of non-null unique network entries
    print data.groupby('month').first() # Get the first entry for each month
    print data.groupby('month')['duration'].sum() # Get the sum of the durations per month
    print data.groupby('month')['date'].count() # Get the number of dates / entries in each month
    print data[data['item']=='call'].groupby('network')['duration'].sum()# What is the sum of durations, for calls only, to each network
    print data.groupby(['item','month'])['date'].count()  # How many calls, sms, and data entries are in each month?
    print data.groupby(['month','item'])['date'].count()  # How many calls, sms, and data entries are in each month?
    print data.groupby(['month','network_type'])['duration'].count() # How many calls, texts, and data are sent per month, split by network_type?
    print data.groupby('month')['duration'].sum()  # produces Pandas Series
    print data.groupby('month')[['duration']].sum() # Produces Pandas DataFrame
    print data.groupby('month',as_index=False).agg({"duration":"sum"})

    d = {"duration":"sum","network_type":"count","date":"first"}
    print data.groupby(['month','item']).agg(d)

    aggegation = {
    "duration":"sum",
    "date":lambda x:max(x)
    }
    print data.groupby('month').agg(aggegation)

    print "."*40
    print data.groupby(['month','item']).agg({'duration':[min,max,sum],'network_type':"count",
        "date":[min,"first","nunique"]})

    print "-"*40
    print data.groupby('month').agg({"duration":[min,max,"mean"]})


if __name__ == '__main__':
    main()
