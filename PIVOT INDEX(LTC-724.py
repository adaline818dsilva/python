class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            right = right-nums[i]
            if left == right:
                return i
            left =left + nums[i]
        return -1