class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        lastSeen = dict()

        for i in range(len(nums)):

            if target - nums[i] in lastSeen:
                return [lastSeen[target-nums[i]], i]
            else:
                lastSeen[nums[i]] = i

        
        