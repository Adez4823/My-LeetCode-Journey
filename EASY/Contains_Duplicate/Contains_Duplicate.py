class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_map = set()
        for num in nums:
            if num in num_map:
                return True
            else:
                num_map.add(num)

        return False