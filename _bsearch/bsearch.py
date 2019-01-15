# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 11:01:04 2019

@author: qwer_mt
"""
from typing import List

def bsearch(nums: List[int], target:int) -> int:
    low, high = 0, len(nums)-1
    while low <= high:
        mid = low + ((high-low)>>1)
        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    nums = [1,2,3,4,5,6]
    target = 7
    a = bsearch(nums,target)
    print(a)