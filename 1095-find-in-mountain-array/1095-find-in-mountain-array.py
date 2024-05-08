# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def binarySearch(self, target: int, mountain_arr: 'MountainArray', low: int, high: int, straight: bool) -> int:
        while low <= high:
            mid = (low + high) // 2
            element = mountain_arr.get(mid)
            if element < target:
                if straight:
                    low = mid + 1
                else:
                    high = mid - 1
            elif element > target:
                if straight:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                return mid
        return -1
    
    def findPivotElement(self, length: int, mountain_arr: 'MountainArray') -> Tuple[int, int]:
        low = 0
        high = length - 1
        while low <= high:
            mid = (low + high) // 2
            element = mountain_arr.get(mid)
            if mid < length - 1:
                next_element = mountain_arr.get(mid + 1) # assuming mid + 1 exists
                
                if element < next_element:
                    low = mid + 1
                elif element > next_element:
                    prev_element = mountain_arr.get(mid - 1) # assuming mid - 1 exists
                    if prev_element < element:
                        return (mid, element)
                    high = mid - 1
                else:
                    print("should not arise since 2 adjacent numbers cannot be same")
                    return (-1, -1)
            else:
                print("idk why this would arise")
        
        print("no pivot found")
        return (-1, -1) # should never reach here
        

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        pivotIndex, pivot = self.findPivotElement(length, mountain_arr)
        if pivotIndex == -1:
            return -1 # should not arise since pivot does exist
        if pivot == target:
            return pivotIndex
        searchIndex = self.binarySearch(target, mountain_arr, 0, pivotIndex - 1, True)
        if searchIndex == -1:
            searchIndex = self.binarySearch(target, mountain_arr, pivotIndex + 1, length - 1, False)
        return searchIndex