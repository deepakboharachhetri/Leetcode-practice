class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      difference={}
      for index,value in enumerate(nums):
        diff=target-value
        if diff in difference:
            return [difference.get(diff),index]
        difference[value]=index



s=Solution()
print(s.twoSum([2,7,11,15],9))

# diff ={7: 0, 2: 1, -2: 2}
# print("dif",diff.get(7))