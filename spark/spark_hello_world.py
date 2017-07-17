# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-07-17 16:24:28
# @Last Modified by:   jerry
# @Last Modified time: 2017-07-17 17:19:26

from pyspark import SparkContext
from pyspark import SparkConf

conf = SparkConf().setMaster("local").setAppName("MY First App")
sc = SparkContext(conf = conf)

data = [1, 2, 3, 4, 5]
distData = sc.parallelize(data)
distData.reduce(lambda a, b: a + b)
print distData

