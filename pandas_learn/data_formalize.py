# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-10-18 10:10:04
# @Last Modified by:   jerry
# @Last Modified time: 2017-10-18 14:56:17

import pandas as pd
from pandas import DataFrame

def merge():

    df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                     'data1': range(7)})
    df2 = DataFrame({'key': ['a', 'b', 'd'],
                     'data2': range(3)})

    df = pd.merge(df1,df2, on='key')
    print(df)

def merge_different():
    # 如果两个dataframe列不同
    df3 = DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})
    df4 = DataFrame({'rkey': ['a', 'b', 'd'],
                 'data2': range(3)})
    df = pd.merge(df3, df4, left_on='lkey', right_on='rkey')
    print(df)


def _map():
    """
    如果要添加一列表示该肉类食物来源的动物类型，Series 的 map 方法可以接受一个函数或含有映射关系的字典对象
    """
    meat_to_animal = {
                      'bacon': 'pig',
                      'pulled pork': 'pig',
                      'pastrami': 'cow',
                      'corned beef': 'cow',
                      'honey ham': 'pig',
                      'nova lox': 'salmon'
                    }
    data = DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami',
                           'corned beef', 'Bacon', 'pastrami', 'honey ham',
                           'nova lox'],
                  'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

    data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
    # 也可以传入一个能够完成全部工作的函数：
    data['animal'] = data['food'].map(lambda x: meat_to_animal[x.lower()])

    print(data)

def _map_2():
    raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
        'age': [42, 52, 36, 24, 73],
        'city': ['San Francisco', 'Baltimore', 'Miami', 'Douglas', 'Boston']}
    df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'city'])
    print(df)
    print("\n")
    city_to_state = { 'San Francisco' : 'California',
                  'Baltimore' : 'Maryland',
                  'Miami' : 'Florida',
                  'Douglas' : 'Arizona',
                  'Boston' : 'Massachusetts'}
    df['state'] = df['city'].map(city_to_state)
    print(df)


def _cut():
    ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
    bins = [18, 25, 35, 60, 100]
    cats = pd.cut(ages, bins)
    print(cats)
    print(cats.codes)
    print(cats.categories)
    print(pd.value_counts(cats))
if __name__ == '__main__':
    _map_2()
    # merge_different()
    # _map()
    # _cut()
