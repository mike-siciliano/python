#!/usr/bin/env python

from typing import List

'''
    LeetCode #4
    https://leetcode.com/problems/median-of-two-sorted-arrays/
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
      
        test_array = nums1[:]
        test_array.extend(nums2)
        test_array.sort()
        
        array_length = len(test_array)
      
        if array_length % 2 == 0:
            # array is even 
            midpoint = array_length // 2 # floor division
            value = (test_array[midpoint - 1] + test_array[midpoint]) / 2 # average of values
            return value
        else: 
            # array is odd 
            value =  test_array[(array_length // 2)] # floor division 
            return value

# Driver code
if __name__ == '__main__':
    nums1 = [1,4,7,10,12]
    nums2 = [2,3,6,15]

    soulution = Solution()
    print(f'findMedianSortedArrays:')
    print(f'Input: {nums1}  {nums2}')
    print(f'Answer: {soulution.findMedianSortedArrays(nums1, nums2)}')
    