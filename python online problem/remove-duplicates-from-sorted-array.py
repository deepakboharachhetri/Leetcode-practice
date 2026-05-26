class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        output_list=list(set(nums))
        len_output=len(output_list)
        for i in range(len_output):
            nums[i]=output_list[i]
        return len_output

