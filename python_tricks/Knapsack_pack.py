# -*- coding: utf-8 -*-
# @Author: jerry
# @Date:   2017-09-28 17:40:44
# @Last Modified by:   jerry
# @Last Modified time: 2017-09-28 18:12:08

def pack_result():
    """最简单的背包问题，背包最大容量是10  总共4件物品，价值和重量分别如下
        Knapsack Max weight : W = 10 (units)
        Total items         : N = 4
        Values of items     : v[] = {10, 40, 30, 50}
        Weight of items     : w[] = {5, 4, 6, 3}
    """

    V = [10,40,30,50]
    W = [5,2,8,7]
    MAX = 9
    print getValue(W,V,MAX,4)


def getValue(W,V,MAX,i):
    if i>1:
        #不放第i件物品最大价值
        DoNotPutThe_indexi_goods_in_bag_Value,\
        DoNotPutThe_indexi_goods_in_bag_Weight = getValue(W,V,MAX,i-1)
        #如果第i件物品的重量大于背包最大容量
        if W[i-1] > MAX: # 如果这个地方为真，那就不能放i进去了，因为放i进去，背包就装不下了，既然不放i，那就是返回上面不放i的值，
            return DoNotPutThe_indexi_goods_in_bag_Value,DoNotPutThe_indexi_goods_in_bag_Weight
        else: #如果第i件物品的重量小于背包最大容量，那就可以把i放进去了。那把i放进去了后，包包剩下的重量就是max减去i的重量，
            changed_Value,changed_Weight = getValue(W,V,MAX-W[i-1],i-1)
            if changed_Value + V[i-1] > DoNotPutThe_indexi_goods_in_bag_Value:
                return changed_Value + V[i-1],changed_Weight
            else:
                return DoNotPutThe_indexi_goods_in_bag_Value,DoNotPutThe_indexi_goods_in_bag_Weight
    else:
        if W[0] > MAX:
            return 0,MAX
        else:
            return V[0],MAX - W[0]
if __name__ == '__main__':
    pack_result()
