from collections import deque

class Solution:
    def __init__(self):
        self.graph = {}
        self.color = {}
        self.dist = {}
        self.pred = {}

    def isGeneDifferByOne(self, gene1: str, gene2: str) -> bool:
        diff = 0
        for idx in range(8):
            if gene1[idx] != gene2[idx]:
                diff += 1
        return diff == 1
    
    def constructGraph(self, bank: List[str]):
        adjMap = {}
        for i, gene in enumerate(bank):
            for gene2 in bank[i + 1:]:
                if self.isGeneDifferByOne(gene, gene2):
                    if gene in adjMap.keys():
                        adjMap[gene].append(gene2)
                    else:
                        adjMap[gene] = [gene2]
                    if gene2 in adjMap.keys():
                        adjMap[gene2].append(gene)
                    else:
                        adjMap[gene2] = [gene]
        return adjMap

    def BFS(self, startGene: str, endGene: str):
        if startGene == endGene:
            return
        queue = deque([startGene])
        self.color[startGene] = 0
        self.dist[startGene] = 0

        while len(queue) != 0:
            current = queue.popleft()
            for nbr in self.graph[current]:
                if self.color[nbr] == -1:
                    queue.append(nbr)
                    self.color[nbr] = 0
                    self.dist[nbr] = self.dist[current] + 1
                    self.pred[nbr] = current
            self.color[current] = 1
                    

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        newBank = [startGene]
        newBank.extend(bank)
        self.graph = self.constructGraph(newBank)
        if endGene not in self.graph.keys():
            return -1
        for node in self.graph.keys():
            self.color[node] = -1
            self.pred[node] = ""
        
        self.BFS(startGene, endGene)
        return self.dist.get(endGene, -1)
        
        

        