#!/bin/bash

"""
Problem Statement:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. 
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

Example 2:
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]
 
Constraints:
    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 
Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

"""


class Solution:
    def __init__(self, ):
        pass 

    # naive Approach
    def productExceptSelfApproach1(self, nums: list[int]) -> list[int]:
        result = []
        len_nums = len(nums)
        for i in range(len_nums):
            output = 1 
            for j in range(len_nums):
                if i != j:
                    output *= nums[j]
            result.append(output)
        return result

    # Pefix, Suffix Approach
    def productExceptSelfApproach2(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        result = [0] * n 

        # Prefix
        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]

        # Suffix
        for j in range(n - 2, -1, -1):
            suffix[j] = nums[j + 1] * suffix[j + 1]

        # Merge
        for i in range(n):
            result[i] = prefix[i] * suffix[i]
        return result


# driver
nums = [1,2,3,4]
obj = Solution()
#result = obj.productExceptSelfApproach1(nums)
result = obj.productExceptSelfApproach2(nums)
print(result)
