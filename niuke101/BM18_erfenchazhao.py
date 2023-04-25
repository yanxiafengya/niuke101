# -*- coding: utf-8 -*-
# @Time : 2023/4/25 16:05
# @Author : ASUS
# @File : BM12_erfenchazhao.py
# @Software: PyCharm

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @param target int整型
# @return int整型
#
class Solution:
    def search(self , nums: list[int], target: int) -> int:
        # write code here
        # 传入列表长度
        length = len(nums)
        # 左游标
        l = 0
        # 右游标
        r = length-1
        # 循环判断是否等于,取下标
        while l<=r:
            # 二分法中间值
            temp = int((l+r)/2)
            if nums[temp]==target:
                return temp
            if nums[temp]>target:
                r = temp-1
            else:
                l=temp+1
        # 没找到返回-1
        return -1
