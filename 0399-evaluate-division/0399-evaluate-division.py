from collections import deque

class Solution:
    def __init__(self):
        self.colour = {}
        self.pred = {}
        self.dist = {}
    
    def createGraph(self, equations: List[List[str]], values: List[float]):
        adjMap = {}

        for index, eq in enumerate(equations):
            if eq[0] in adjMap.keys():
                adjMap[eq[0]][eq[1]] =  values[index]
            else:
                adjMap[eq[0]] = {eq[0]: 1}
                adjMap[eq[0]][eq[1]] = values[index]
            if eq[1] in adjMap.keys():
                if values[index] == 0:
                    adjMap[eq[1]][eq[0]] = -1
                else:
                    adjMap[eq[1]][eq[0]] = 1 / values[index]
            else:
                adjMap[eq[1]] = {eq[1] : 1}
                if values[index] == 0:
                    adjMap[eq[1]][eq[0]] = -1
                else:
                    adjMap[eq[1]][eq[0]] = 1 / values[index]
        
        return adjMap

    def BFS(self, adjMap, start: str):
        self.colour[start] = 0
        queue = deque([start])
        while len(queue) != 0:
            current_node = queue.popleft()
            node_nbrs = adjMap[current_node].keys()
            for nbrs in node_nbrs:
                if self.colours.get(nbrs, -1) == -1:
                    queue.append(nbrs)
                    self.pred[nbrs] = current_node
                    self.colours[nbrs] = 0
                    if adjMap[current_node][nbrs] == -1 or self.dist[current_node] == -1:
                        self.dist[nbrs] = -1
                    else:
                        self.dist[nbrs] = self.dist[current_node] * adjMap[current_node][nbrs]
            self.colours[nbrs] = 1


    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjMap = self.createGraph(equations, values)
        print(adjMap)
        results = []
        for query in queries:
            self.colours = {}
            self.pred = {}
            self.dist = {
                query[0]: 1
            }
            if query[0] not in adjMap.keys() or query[1] not in adjMap.keys():
                results.append(-1)
            else:
                self.BFS(adjMap, query[0])
                results.append(self.dist.get(query[1], -1))
        return results