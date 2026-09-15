"""
Contains Duplicate - LeetCode #217
https://leetcode.com/problems/contains-duplicate/

Problem: Given an integer array nums, return true if any value appears 
at least twice in the array, and return false if every element is distinct.

Approach: Use a hash set to track seen elements. If we encounter an element 
that's already in the set, we found a duplicate.

Time Complexity: O(n) - We traverse the list once
Space Complexity: O(n) - We store up to n elements in the set
"""

from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    """
    Check if the array contains any duplicate elements.
    
    Args:
        nums: List of integers
        
    Returns:
        True if duplicates exist, False otherwise
    """
    # Hash set to track seen elements
    seen = set()
    
    # Iterate through the array
    for num in nums:
        # If we've seen this number before, it's a duplicate
        if num in seen:
            return True
        # Add current number to seen set
        seen.add(num)
    
    # No duplicates found
    return False

# Alternative approaches for comparison

def contains_duplicate_sorting(nums: List[int]) -> bool:
    """
    Alternative approach using sorting.
    Time Complexity: O(n log n) - Due to sorting
    Space Complexity: O(1) - If we can modify input, otherwise O(n) for copy
    """
    # Sort the array
    nums_sorted = sorted(nums)
    
    # Check adjacent elements for duplicates
    for i in range(1, len(nums_sorted)):
        if nums_sorted[i] == nums_sorted[i-1]:
            return True
    return False

def contains_duplicate_brute_force(nums: List[int]) -> bool:
    """
    Brute force approach - check all pairs.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False

# Test cases
if __name__ == "__main__":
    # Test case 1: Contains duplicate
    nums1 = [1, 2, 3, 1]
    print(f"Input: nums = {nums1}")
    print(f"Output: {contains_duplicate(nums1)}")  # Expected: True
    print()
    
    # Test case 2: No duplicates
    nums2 = [1, 2, 3, 4]
    print(f"Input: nums = {nums2}")
    print(f"Output: {contains_duplicate(nums2)}")  # Expected: False
    print()
    
    # Test case 3: Multiple duplicates
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"Input: nums = {nums3}")
    print(f"Output: {contains_duplicate(nums3)}")  # Expected: True
    print()