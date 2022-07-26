"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Binary search for target and estimation for left and right target bounds
        left_bound, right_bound = 0, len(nums)
        while left_bound != right_bound:
            mid_pos = (right_bound + left_bound) // 2 
            val = nums[mid_pos]
            if val == target:
                    break; # target found, bounds esitmated
            elif val > target:
                right_bound = mid_pos
            else:
                left_bound = mid_pos + 1
        else:
            return [-1, -1] # target not found
        
        start_target_left_bound, start_target_right_bound = left_bound, mid_pos + 1
        stop_target_left_bound, stop_target_right_bound = mid_pos, right_bound
        
        # Binary seach for left target bound
        while start_target_left_bound != start_target_right_bound:
            mid_pos = (start_target_right_bound + start_target_left_bound) // 2 
            val = nums[mid_pos]
            if val == target:
                if mid_pos == 0 or nums[mid_pos - 1] < target:
                    break; # found estimation for left and right target bounds
                start_target_right_bound = mid_pos
            elif val > target:
                start_target_right_bound = mid_pos
            else:
                start_target_left_bound = mid_pos + 1
        
        start_target_left = mid_pos
                
        # Binary seach for right target bound    
        while stop_target_left_bound != stop_target_right_bound:
            mid_pos = (stop_target_right_bound + stop_target_left_bound) // 2 
            val = nums[mid_pos]
            if val == target:
                if mid_pos == len(nums) - 1 or nums[mid_pos + 1] > target:
                    break; # found estimation for left and right target bounds
                stop_target_left_bound = mid_pos
            elif val > target:
                stop_target_right_bound = mid_pos
            else:
                stop_target_left_bound = mid_pos + 1
        
        
        return [start_target_left, mid_pos]