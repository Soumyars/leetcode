#!/bin/bash

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
