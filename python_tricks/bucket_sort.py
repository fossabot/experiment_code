#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/5 18:15
# @Author  : Zhiwei Yang
# @File    : bucket_sort.py.py

def bucketSort(nums):
    max_number = max(nums) #选择待排序的list里面的一个最大的数
    #接着创建一个元素全是0的列表，当做桶
    print (max_number)
    bucket = [0]*(max_number+1)
    print (bucket)
    #接着把所有元素放入桶中，即把对应的元素个数加1
    for i in nums:
        bucket[i] +=1
    print (bucket)

    sort_nums = []
    for j in range(len(bucket)):
        print (j)
        if bucket[j] !=0:
            sort_nums.append(j)

    return sort_nums

nums = [5,6,2,1,65,9]
print (bucketSort(nums))
