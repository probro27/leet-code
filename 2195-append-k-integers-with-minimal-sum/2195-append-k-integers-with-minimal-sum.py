import heapq

class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        queue = nums.copy()
        heapq.heapify(queue)
        total_sum = 0
        current_number = 1
        while k != 0 and len(queue) != 0:
            element = heapq.heappop(queue)
            if element > current_number:
                number_of_elements = element - current_number
                if number_of_elements < k:
                    total_sum += (number_of_elements * (current_number + element - 1)) // 2
                    k -= number_of_elements
                    current_number = element + 1
                else:
                    total_sum += (k * (current_number + current_number + k - 1)) // 2
                    k = 0
                    current_number = current_number + k
            elif current_number == element:
                current_number += 1
                if len(queue) != 0 and queue[0] == element:
                    current_number -= 1
            
        if k != 0:
            total_sum += (k * (current_number + current_number + k - 1)) // 2
            k = 0
            current_number = current_number + k
        return total_sum