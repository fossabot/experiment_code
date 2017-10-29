#coding: utf-8
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

def frame():
    data = {'state':['hubei','sichuan','guangzhou'],'year':[2015,2016,2017],'pop':[6,7,8]}
    frame = DataFrame(data)
    print frame

    print DataFrame(data,columns=['year','state','pop','debt'])
    print frame.columns
    print frame['state']
    print frame['pop']
    print frame['year']

    frame['debt'] = 16.5
    print frame

    frame['debt'] = np.arange(3.)
    print frame

    frame2 = DataFrame(data,columns=['year','state','pop','debt'],index=['one','two','three'])
    print frame2
    val = Series([-1.2,-1.3,-1.4],index=['two','three','one'])
    frame2['debt'] = val
    print frame2

    frame2['eastern'] = frame2.state == 'hubei'
    print frame2
    print frame2.index

def frame3():
    pop = {'hubei':{2001:2.4,2002:2.5}, "guangdong":{2000:2.6,2001:2.7}}
    frame3 = DataFrame(pop)
    print frame3
    print frame3.T
    print DataFrame(pop,index=[2001,2000,2002])

    pdata = {'hubei':frame3['hubei'][:-2],'guangdong':frame3['guangdong'][:-2]}
    print pdata


if __name__ == '__main__':
    frame3()
