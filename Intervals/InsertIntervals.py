class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #if no interval exists
        if len(intervals)==0:
            return [newInterval]
        
        #if new interval is greater than all
        if newInterval[0]>intervals[-1][1]:
            return intervals + [newInterval]

        ans = []
        ind = 0
        flag=False
        while ind<len(intervals):
            #if interval does not cause any merging
            if not flag and intervals[ind][0]>newInterval[1]:
                ans.append(newInterval)
                flag=True
                continue
            
            if flag or intervals[ind][1]<newInterval[0]:
                ans.append(intervals[ind])
                ind+=1
            else:
                flag=True
                mergedInterval = [min(intervals[ind][0], newInterval[0]), max(intervals[ind][1], newInterval[1])]
                while ind<len(intervals):
                    if intervals[ind][0]<=mergedInterval[1]:
                        mergedInterval[1] = max(intervals[ind][1], newInterval[1])
                        ind+=1
                    else:
                        break
                ans.append(mergedInterval)
        return ans

                