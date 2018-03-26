class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        for i in range(0, len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return nums.index(nums[i])

        return len(nums)