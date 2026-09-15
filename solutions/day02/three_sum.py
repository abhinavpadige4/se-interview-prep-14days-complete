"""
3Sum - LeetCode #15
https://leetcode.com/problems/3sum/

Problem: Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Approach: 
1. Sort the array
2. Fix one element and use two pointers to find pairs that sum to -fixed_element
3. Skip duplicates to avoid duplicate triplets

Time Complexity: O(n^2) - Sorting (O(n log n)) + nested loops (O(n^2))
Space Complexity: O(1) or O(n) - Depending on sorting algorithm (excluding output storage)
"""

from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Find all unique triplets that sum to zero.
    
    Args:
        nums: List of integers
        
    Returns:
        List of lists containing unique triplets that sum to zero
    """
    # Sort the array to make it easier to avoid duplicates
    nums.sort()
    result = []
    n = len(nums)
    
    # Iterate through the array, fixing one element at a time
    for i in range(n - 2):
        # Skip duplicate elements for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Two pointers approach for the remaining part
        left, right = i + 1, n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum < 0:
                # Need larger sum, move left pointer right
                left += 1
            elif current_sum > 0:
                # Need smaller sum, move right pointer left
                right -= 1
            else:
                # Found a triplet that sums to zero
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for the second number
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                # Skip duplicates for the third number
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # Move both pointers to find next potential triplet
                left += 1
                right -= 1
    
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1: Standard case
    nums1 = [-1, 0, 1, 2, -1, -4]
    print(f"Input: nums = {nums1}")
    print(f"Output: {three_sum(nums1)}")  # Expected: [[-1, -1, 2], [-1, 0, 1]]
    print()
    
    # Test case 2: All zeros
    nums2 = [0, 0, 0, 0]
    print(f"Input: nums = {nums2}")
    print(f"Output: {three_sum(nums2)}")  # Expected: [[0, 0, 0]]
    print()
    
    # Test case 3: No solution
    nums3 = [0, 1, 1]
    print(f"Input: nums = {nums3}")
    print(f"Output: {three_sum(nums3)}")  # Expected: []
    print()
    
    # Test case 4: Empty array
    nums4 = []
    print(f"Input: nums = {nums4}")
    print(f"Output: {three_sum(nums4)}")  # Expected: []
    print()