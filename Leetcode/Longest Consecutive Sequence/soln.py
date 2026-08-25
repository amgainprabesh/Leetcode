class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count=0
        s=set(nums)
        for x in s:
            length=1
            if x-1 not in s:#[1,2,3,4,100,200]
                while x+1 in s:
                    length +=1
                    x+=1
                count=max(count,length)
        return count