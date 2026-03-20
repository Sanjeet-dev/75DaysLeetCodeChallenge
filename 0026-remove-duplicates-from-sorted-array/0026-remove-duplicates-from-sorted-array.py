class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer1 = 0

        for pointer2 in range(1,len(nums)):
            if nums[pointer2] != nums[pointer1]:
                pointer1+=1
                nums[pointer1]=nums[pointer2]
        return pointer1+1

        