import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        p=1
        for i in range(len(nums)):
           answer[i] = p
           p= p * nums[i]
        p=1
        for i in range(len(nums)-1 ,-1,-1):
            answer[i]*=p
            p=p*nums[i]
        return answer

#time complexity o(n) :: Optimized method.
#By ::Prabesh Amgain.
#date :: 2026-08-25.
