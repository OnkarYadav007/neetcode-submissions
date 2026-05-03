class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        is_more=False
        if len(set(nums)) < len(nums):
            is_more=True
        else:
            is_more=False
        return is_more