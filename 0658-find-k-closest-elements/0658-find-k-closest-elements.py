class Solution:

    def checkCloser(self, a: int, b: int, x: int) -> bool:
        return abs(a - x) < abs(b - x) or (abs(a - x) == abs(b - x) and a < b)

    def binarySearch(self, arr: List[int], x: int) -> int:
        high = len(arr) - 1
        low = 0

        mid = (low + high) // 2

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                return mid  # element found
        
        return mid  # return approximate position of element if it existed

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr

        currentOrApproxPosition = self.binarySearch(arr, x)

        left = currentOrApproxPosition - 1
        count = 0
        results = []
        if arr[currentOrApproxPosition] == x:
            right = currentOrApproxPosition + 1
            count = 1
            results.append(x)
        else:
            checks = []
            if currentOrApproxPosition == 0:
                checks = [currentOrApproxPosition, currentOrApproxPosition + 1]
            elif currentOrApproxPosition == len(arr) - 1:
                checks = [currentOrApproxPosition - 1, currentOrApproxPosition]
            else:
                checks = [currentOrApproxPosition - 1, currentOrApproxPosition, currentOrApproxPosition + 1]
            closer = checks[0]
            for check in checks[1:]:
                if self.checkCloser(arr[check], arr[closer], x):
                    closer = check
            
            results.append(arr[closer])
            count = 1

            if closer == currentOrApproxPosition:
                right = currentOrApproxPosition + 1
            elif closer == currentOrApproxPosition - 1:
                left = currentOrApproxPosition - 2
                right = currentOrApproxPosition
            else:
                left = currentOrApproxPosition
                right = currentOrApproxPosition + 2
        


        while count < k:
            if left < 0:
                results.append(arr[right])
                right += 1
                count += 1
            elif right >= len(arr):
                results.append(arr[left])
                left -= 1
                count += 1
            else:
                compare = self.checkCloser(arr[left], arr[right], x)
                if compare:
                    results.append(arr[left])
                    left -= 1
                else:
                    results.append(arr[right])
                    right += 1
                count += 1
    
        return sorted(results)
                