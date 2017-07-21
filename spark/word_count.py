# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-07-17 17:20:09
# @Last Modified by:   jerry
# @Last Modified time: 2017-07-18 17:39:30

from __future__ import print_function

import sys
from operator import add
from pyspark.sql import SparkSession

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)

    spark = SparkSession.builder.appName("PythonWordCount").getOrCreate()

    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])
    counts = lines.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)) \
                .reduceByKey(add)
    output = counts.collect()
    print(output)
    for (word, count) in output:
        print("%s: %i" % (word, count))

    spark.stop()
