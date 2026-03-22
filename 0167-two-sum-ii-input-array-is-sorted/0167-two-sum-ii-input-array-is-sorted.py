class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        color={}

        for i,num in enumerate(numbers):
            needed = target-num
            if needed in color:
                return [color[needed]+1,i+1]
            
            color[num] = i
        