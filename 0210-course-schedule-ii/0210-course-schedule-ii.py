from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 0:
            return [x for x in range(numCourses)]
        start = 0
        colour = [-1 for _ in range(numCourses)]
        pred = [-1 for _ in range(numCourses)]
        discovery = [0 for _ in range(numCourses)]
        finish = [0 for _ in range(numCourses)]
        time = 0
        DAG = True
        stack = deque([])

        adjMap = {}

        for prereq in prerequisites:
            if prereq[0] in adjMap.keys():
                adjMap[prereq[0]].append(prereq[1])
            else:
                adjMap[prereq[0]] = [prereq[1]]

        def DFSVisit(start: int):
            nonlocal time
            nonlocal DAG

            colour[start] = 0 # grey
            time += 1
            discovery[start] = time

            for v in adjMap.get(start, []):
                if colour[v] == -1:
                    pred[v] = start
                    DFSVisit(v)
                elif colour[v] == 0:
                    DAG = False

            colour[start] = 1
            stack.append(start)
            time += 1
            finish[start] = time
        
        for v in range(numCourses):
            if colour[v] == -1:
                DFSVisit(v)
        if DAG:
            return stack
        else:
            return []