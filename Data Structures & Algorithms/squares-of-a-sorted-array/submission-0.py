class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n

        left = 0
        right = n - 1
        pos = n - 1

        while left <= right:

            leftSquare = nums[left] * nums[left]
            rightSquare = nums[right] * nums[right]

            if leftSquare > rightSquare:
                ans[pos] = leftSquare
                left += 1
                
            else:
                ans[pos] = rightSquare
                right-=1
                

            pos-=1
        return ans