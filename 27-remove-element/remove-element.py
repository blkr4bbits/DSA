#if val != any elements in the list nums , remove all elements != val

class Solution(object):
    def removeElement(self, nums, val):

        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums [k] = nums [i]
                k += 1
        return k

#blkr4bbits