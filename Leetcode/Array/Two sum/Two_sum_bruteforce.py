class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i,j]
                    break
        
#time complexity o(n^2) :: Bruteforce method
#By ::Prabesh Amgain
#Timeframe :: 2026-08-13