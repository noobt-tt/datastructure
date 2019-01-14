# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:09:53 2019

@author: qwer_mt
"""
from typing import List
import itertools

def counting_sort(a: List[int]):
    if len(a) <= 1: return
    counts = [0]*(max(a)+1)
    for num in a:
        counts[num] += 1
    counts = list(itertools.accumulate(counts))
    
    a_sorted = [0] * len(a)
    i = len(a)-1
    while i >= 0:
        num = a[i]
        index = counts[num] - 1
        a_sorted[index] = num
        counts[num] -= 1
        i -= 1
    a[:] = a_sorted

if __name__ == "__main__":
    a1 = [1, 2, 3, 4]
    a2 = [1, 1, 1, 1]
    a3 = [4, 5, 0, 9, 3, 3, 1, 9, 8, 7]
    counting_sort(a1)
    print(a1)
    counting_sort(a2)
    print(a2)
    counting_sort(a3)
    print(a3)    
        
    