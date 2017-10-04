# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-09-25 21:40:27
# @Last Modified by:   jerry
# @Last Modified time: 2017-09-25 21:45:54

class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self,numbers,target):
        ret = []
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i] + numbers[j] == target:
                    ret.append(i)
                    ret.append(j)

        return ret

if __name__ == '__main__':
    a = Solution()
    numbers = [98,23,3,4,5]
    target = 26
    c = a.twoSum(numbers,target)
    print c

