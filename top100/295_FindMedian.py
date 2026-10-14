#!/bin/bash 

"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 

Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""

class MedianFinder:
    def __init__(self, ):
        pass

    def addNum(self, num: int) -> None:
        arr.append(num)
        return None

    def findMedian(self) -> float:
        mid_pos = len(arr) // 2
        if len(arr) % 2 == 0:
            return float((arr[mid_pos -1] + arr[mid_pos])/2)
        else:
            return float(arr[mid_pos])


# Driver 
ip_str1 = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
ip_str2 = [[], [1], [2], [], [3], []]
obj = MedianFinder()
arr = []
result = []
for i in range(0, len(ip_str1)):
    if ip_str1[i] == "addNum":
        result_num = obj.addNum(ip_str2[i][0])
        if result_num is None:
            result_num = "null"
        result.append(result_num)
    elif ip_str1[i] == "findMedian": 
        result_med = obj.findMedian()
        result.append(result_med)
    else:
        result.append("null")

print(result)