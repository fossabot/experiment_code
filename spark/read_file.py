# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-07-17 21:37:38
# @Last Modified by:   jerry
# @Last Modified time: 2017-07-17 22:11:08

from pyspark.sql import SparkSession

logFile = "readme.md"
appName = 'SimpleApp'
master = 'local'
spark = SparkSession.builder.appName(appName).master(master).getOrCreate()
logData = spark.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()

print("%i,%i" % (numAs,numBs))
spark.stop()
