class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        time = 0
        color = [-1 for _ in range(numCourses)]
        pred = [-1 for _ in range(numCourses)]
        discovery = [0 for _ in range(numCourses)]
        finish = [0 for _ in range(numCourses)]
        DAG = True

        adjMap = {}

        for item in prerequisites:
            if item[1] in adjMap:
                adjMap[item[1]].append(item[0])
            else:
                adjMap[item[1]] = [item[0]]
        print(adjMap)
        def dfsVisit(start: int):
            nonlocal time
            nonlocal DAG
            color[start] = 0
            time += 1
            discovery[start] = time

            for v in adjMap.get(start, []):
                if color[v] == -1:
                    pred[v] = start
                    dfsVisit(v)
                elif color[v] == 0:
                    DAG = False

            color[start] = 1
            time += 1
            finish[start] = time
        
        for v in range(numCourses):
            if color[v] == -1:
                dfsVisit(v)
        
        return DAG

