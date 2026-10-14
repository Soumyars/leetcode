#!/bin/bash

"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        plen = len(p)
        slen = len(s)
        x = slen - plen
        sorted_p = "".join(sorted(p))
        result = []
        for i in range(0, x+1):
            wstr = s[i:i+plen]
            sorted_wstr = "".join(sorted(wstr))
            if sorted_wstr == sorted_p:
                result.append(i)
        return result
   

# Driver Code
s = "cbaebabacd"
p = "abc"
ob = Solution()
print(ob.findAnagrams(s,p))