class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        # Map difficulty to number of tasks
        task_map = dict()

        for task in tasks:
            if task_map.get(task) is None:
                task_map[task] = 1
            else:
                task_map[task] += 1
        
        total_rounds = 0
        for level, task in task_map.items():
            if task <= 1:
                return -1
            total_rounds += (task // 3) + (1 if task % 3 != 0 else 0)
        
        return total_rounds
