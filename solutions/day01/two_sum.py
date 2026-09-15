"""
Two Sum - LeetCode #1
https://leetcode.com/problems/two-sum/

Problem: Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

Approach: Use a hash map to store numbers we've seen so far along with their indices.
For each number, check if its complement (target - current number) exists in the hash map.

Time Complexity: O(n) - We traverse the list once
Space Complexity: O(n) - We store up to n elements in the hash map
"""

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find two numbers that add up to target and return their indices.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List containing the indices of the two numbers
    """
    # Hash map to store number -> index mapping
    num_map = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement we need
        complement = target - num
        
        # Check if complement exists in our map
        if complement in num_map:
            # Found the pair!
            return [num_map[complement], i]
        
        # Store current number and its index
        num_map[num] = i
    
    # According to problem constraints, we should always find a solution
    # But returning empty list as fallback
    return []

# Alternative brute force approach for comparison (O(n^2) time, O(1) space)
def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Brute force approach - check all pairs.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {two_sum(nums1, target1)}")  # Expected: [0, 1]
    print()
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {two_sum(nums2, target2)}")  # Expected: [1, 2]
    print()
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {two_sum(nums3, target3)}")  # Expected: [0, 1]
    print()