class Solution:
    def isGood(self, nums: List[int]) -> bool:
        maximum=max(nums)
        print(maximum)
        if max !=1:
            
            for i in range(1,len(nums)):
                if  nums.count(i) == 1:
                    continue

                else :
                    return False
        print(nums.count(max))
        if nums.count(max) == 2:
            return True
        
        return False
        
s=Solution()
print(s.isGood(nums=[1,1]))        