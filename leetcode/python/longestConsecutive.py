"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""
from typing import List


def longestConsecutive(self, nums: List[int]) -> int:
    first_to_last = {}
    last_to_first = {}
    processed = set()
    for n in nums:
        if n in processed:
            continue
        processed.add(n)
        right_range_last = first_to_last.get(n + 1)
        left_range_first = last_to_first.get(n - 1)
        if right_range_last is not None and left_range_first is not None:
            # n is missing link between two ranges
            # del first_to_last[n + 1]
            # del last_to_first[n - 1]
            first_to_last[left_range_first] = right_range_last
            last_to_first[right_range_last] = left_range_first
            continue
        if right_range_last is not None:
            #extend right range
            # del first_to_last[n + 1]
            first_to_last[n] = right_range_last
            last_to_first[right_range_last] = n
            continue
        if left_range_first is not None:
            # extend left range
            # del last_to_first[n - 1]
            last_to_first[n] = left_range_first
            first_to_last[left_range_first] = n
            continue
        #create new range
        first_to_last[n] = n
        last_to_first[n] = n
    return max(last - first + 1  for first, last in first_to_last.items()) if first_to_last else 0


def longestConsecutive_cheat(self, nums: List[int]) -> int:
    nums.sort()
    longest = 0
    current_seq_len = 1
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i - 1]
        if diff < 2:
            current_seq_len += diff
        else:
            if longest < current_seq_len:
                longest = current_seq_len
            current_seq_len = 1
    return max(longest, current_seq_len) if nums else 0