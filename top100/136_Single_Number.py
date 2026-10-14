#!/bin/python3

"""
Problem Statement:(LC136)
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
    Input: nums = [2,2,1]
    Output: 1

Example 2:
    Input: nums = [4,1,2,1,2]
    Output: 4

Example 3:
    Input: nums = [1]
    Output: 1

Constraints:
    1 <= nums.length <= 3 * 104
    -3 * 104 <= nums[i] <= 3 * 104
    Each element in the array appears twice except for one element which appears only once.
"""

class Solution:
    # Naive Approach
    def singleNumberA(self, nums: list[int]) -> int:
        output_arr = []
        for num_l1 in nums:
            count = 0
            for num_l2 in nums:
                if num_l1 == num_l2:
                    count += 1
            if count == 1:
                output_arr.append(num_l1)
        if len(output_arr) == 1:
            return output_arr[0]
    
    # XOR Approach
    def singleNumberB(self, nums: list[int]) -> int:
        output = 0
        for num in nums:
            output ^= num
        return output
