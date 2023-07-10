#!/usr/bin/env python

from typing import List

'''
    LeetCode #4
    https://leetcode.com/problems/median-of-two-sorted-arrays/
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
      
        nums1.extend(nums2)
        nums1.sort()
        array_length = len(nums1)
      
        if array_length % 2 == 0:
            # array is even 
            midpoint = array_length // 2 # floor division
            value = (nums1[midpoint - 1] + nums1[midpoint]) / 2 # average of values
            return value
        else: 
            # array is odd 
            value =  nums1[(array_length // 2)] # floor division 
            return value

# Driver code
if __name__ == '__main__':
    nums1 = [1,4,7,10,12]
    nums2 = [2,3,6,15]

    soulution = Solution()
    print(f'findMedianSortedArrays:')
    print(f'Input: {nums1}  {nums2}')
    print(f'Answer: {soulution.findMedianSortedArrays(nums1, nums2)}')
    