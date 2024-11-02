class TimeMap:
    '''
        Building a Map that stores value as follows:
        {
            'key': {
                'timestamp': 'value',
                ....,
                'timestamps': [sorted list]
            }
        }
    '''
    def __init__(self):
        self.map = {}

    def __binarySearch(self, key: str, timestamp: int) -> int:
        timestamps = self.map[key]['timestamps']  # Assuming key always exists

        low = 0
        high = len(timestamps) - 1

        mid = (low + high) // 2

        while low <= high:
            mid = (low + high) // 2
            
            if timestamps[mid] < timestamp:
                low = mid + 1
            elif timestamps[mid] > timestamp:
                high = mid - 1
            else:
                return mid

        
        return mid

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = {
                timestamp: value,
                'timestamps': [timestamp]
            }
        else:
            self.map[key][timestamp] = value
            self.map[key]['timestamps'].append(timestamp)
        
    def get(self, key: str, timestamp: int) -> str:
        values = self.map.get(key, None)
        if values is None:
            return ""
        
        closestTimestampIndex = self.__binarySearch(key, timestamp)

        closestTimestamp = values['timestamps'][closestTimestampIndex]

        if closestTimestamp > timestamp:
            if closestTimestampIndex == 0:
                return ""
            else:
                closestTimestamp = values['timestamps'][closestTimestampIndex - 1]
        
        return values[closestTimestamp]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)