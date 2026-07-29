class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uni1= sorted(set(nums))
        nums[:len(uni1)]=uni1
        return len(uni1)