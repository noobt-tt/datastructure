# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 10:44:22 2019

@author: qwer_mt
"""
from typing import List

def bsearch_left(nums: List[int], target:int) -> int:
    low, high = 0, len(nums)-1
    while low <= high:
        mid = low + ((high-low)>>1)
        if nums[mid] >= target:
            high = high - 1
        else:
            low = low + 1
    return low if nums[low] == target else -1

def bsearch_right(nums: List[int], target:int) -> int:
    low, high = 0, len(nums)-1
    while low <= high:
        mid = low + ((high-low)>>1)
        if nums[mid] <= target:
            low = low + 1
        else:
            high = high - 1
    return high if nums[high] == target else -1

def bsearch_left_not_less(nums: List[int], target:int) ->int:
    low, high = 0, len(nums)-1
    while low <= high:
        mid = low + ((high-low)>>1)
        if nums[mid] >= target:
            high = high - 1
        else:
            low = low + 1
    return low if low<len(nums) else -1

def bsearch_right_not_greater(nums: List[int], target:int) -> int:
    low, high = 0, len(nums)-1
    while low <= high:
        mid = low + ((high-low)>>1)
        if nums[mid] <= target:
            low = low + 1
        else:
            high = high - 1
    return high if high>0 else -1

if __name__ == "__main__":
    a = [0, 1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 8, 10, 10, 10]
    b = [11, 12, 12, 13, 14, 14, 15, 15]
    
    print(bsearch_left(a,10))  #12
    print(bsearch_right(a,6))   #8
    print(bsearch_left_not_less(a,11))#-1
    print(bsearch_right_not_greater(b,17))#7
    

































