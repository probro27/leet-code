class Solution:
    def partition(self, nums: List[int], idx: int) -> Tuple[int, List[int]]:
        print(f'{idx}, {len(nums)}')
        value = nums[idx]
        lesser = []
        greater = []
        equal = []
        for i in range(0, len(nums)):
            if i != idx:
                if nums[i] < value:
                    lesser.append(nums[i])
                elif nums[i] > value:
                    greater.append(nums[i])
                else:
                    equal.append(nums[i])
        partition_idx = len(greater) + 1
        nums = greater + [value] + equal + lesser
        print(nums)
        return (partition_idx, nums)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        rand_idx = randint(0, len(nums) - 1)
        part_idx, nums = self.partition(nums, rand_idx)
        part_val = nums[part_idx - 1]
        if k == part_idx:
            return part_val
        elif k < part_idx:
            print(f'smaller array: {nums[0:part_idx - 1]}')
            return self.findKthLargest(nums[0:part_idx - 1], k)
        else:
            print(f'larger array: {nums[part_idx: len(nums)]}')
            return self.findKthLargest(nums[part_idx: len(nums)], k - part_idx)
            