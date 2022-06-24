class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        startLimit = newInterval[0]
        endLimit = newInterval[1]
        
        lengthOfList = len(intervals)
        
        if lengthOfList == 0:
            intervals.append(newInterval)
            return intervals
        
        if endLimit <= intervals[0][0]:
            intervals.insert(0, newInterval)
            resultIntervals = intervals
            for i in range(len(resultIntervals) - 1):
                if resultIntervals[i][1] >= resultIntervals[i + 1][0]:
                    resultIntervals[i][1] = resultIntervals[i + 1][1]
                    resultIntervals.remove(resultIntervals[i + 1])
            return resultIntervals
        
        newIntervals = []
        
        startIndex = -1
        endIndex = -1
        
        tag = False
        
        if startLimit == endLimit:
            tag = True
        
        flag = False
        
        for index in range(lengthOfList):
            interval = intervals[index]
            if interval[0] <= startLimit and interval[1] >= endLimit:
                return intervals
            elif interval[1] >= startLimit:
                if tag:
                    if interval[0] <= startLimit:
                        return intervals
                    else:
                        intervals.insert(index, newInterval)
                        resultIntervals = intervals
                        for i in range(len(resultIntervals) - 1):
                            if resultIntervals[i][1] >= resultIntervals[i + 1][0]:
                                resultIntervals[i][1] = resultIntervals[i + 1][1]
                                resultIntervals.remove(resultIntervals[i + 1])
                        return resultIntervals
                if startIndex == -1:
                    startIndex = index
                if interval [1] > endLimit:
                    if interval[0] <= endLimit:
                        endIndex = index
                        break
                    else:
                        endIndex = index - 1
                        break
        
        
        if startIndex == -1:
            intervals.append(newInterval)
            resultIntervals = intervals
            for i in range(len(resultIntervals) - 1):
                if resultIntervals[i][1] >= resultIntervals[i + 1][0]:
                    resultIntervals[i][1] = resultIntervals[i + 1][1]
                    resultIntervals.remove(resultIntervals[i + 1])
            return resultIntervals
        if endIndex == -1:
            newIntervals.append(min(intervals[startIndex][0], startLimit))
            newIntervals.append(endLimit)
            flag = True
            endIndex = lengthOfList
        
        if not flag:
            newIntervals.append(min(intervals[startIndex][0], startLimit))
            newIntervals.append(max(intervals[endIndex][1], endLimit))
        
        resultIntervals = []
        
        # print(intervals[startIndex][0])
        
        for i in range(startIndex):
            resultIntervals.append(intervals[i])
        
        resultIntervals.append(newIntervals)
        
        for j in range(endIndex + 1, lengthOfList):
            resultIntervals.append(intervals[j])
        
        for i in range(len(resultIntervals) - 1):
            if resultIntervals[i][1] >= resultIntervals[i + 1][0]:
                resultIntervals[i][1] = resultIntervals[i + 1][1]
                resultIntervals.remove(resultIntervals[i + 1])
        
        return resultIntervals