"""

Merge Intervals
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). 
You may assume that the intervals were initially sorted according to their start times. 
Example 1: Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9]. 
Example 2: Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16]. 
This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10]. Make sure the returned intervals are also sorted.

"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals
            
        i = 0
        while i < len(intervals):
            if intervals[i].end < newInterval.start:
                i += 1
                
            elif newInterval.end < intervals[i].start:
                intervals.insert(i,newInterval)
                break
            
            else:
                newInterval.start = min(newInterval.start, intervals[i].start)
                newInterval.end = max(newInterval.end, intervals[i].end)
                intervals.pop(i)
                
        if i == len(intervals):
            intervals.append(newInterval)
        
        return intervals
        
