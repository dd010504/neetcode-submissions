from typing import List # used to add type hint for List

def count_x(nums: List[int], x: int) -> int:
    val = 0
    for i in range(len(nums)):
        if x == nums[i]:
            val += 1
        
    return val



# do not modify below this line
print(count_x([1, 2, 5, 6, 5], 5))
print(count_x([4, 3, 6, 1, 6], 5))
print(count_x([4, 7, 7, 6, 7, 6], 7))
