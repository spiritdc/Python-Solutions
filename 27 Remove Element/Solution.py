class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
            else:
                i += 1

        return len(nums)

l = [3,2,2,3]
Solution().removeElement(l, 3)
print(l)