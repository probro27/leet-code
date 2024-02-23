import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        used_set = []
        prev_profit = -1
        total_profit = w
        
        def check(idx: int) -> bool:
            return capital[idx] <= total_profit and capital[idx] > prev_profit
        
        available_projects = []
        heapq.heapify(available_projects)

        capacity_heap = [(cap, idx) for idx, cap in enumerate(capital)]
        heapq.heapify(capacity_heap)

        while len(used_set) < k:
            while len(capacity_heap) > 0:
                current_cap = heapq.heappop(capacity_heap)
                if current_cap[0] > total_profit:
                    heapq.heappush(capacity_heap, current_cap)
                    break
                idx = current_cap[1]
                heapq.heappush(available_projects, (-1 * profits[idx], idx))
            
            if len(available_projects) == 0:
                break
            max_profit_project = heapq.heappop(available_projects)
            prev_profit = total_profit
            total_profit += (max_profit_project[0] * -1)
            used_set.append(max_profit_project[1])
        
        return total_profit
