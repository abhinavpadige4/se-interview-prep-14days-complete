"""
Valid Palindrome - LeetCode #125
https://leetcode.com/problems/valid-palindrome/

Problem: A phrase is a palindrome if, after converting all uppercase letters 
into lowercase letters and removing all non-alphanumeric characters, it reads 
the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Approach: Use two pointers - one at start, one at end. Move them towards each 
other, skipping non-alphanumeric characters and comparing lowercase versions.

Time Complexity: O(n) - We traverse the string once with two pointers
Space Complexity: O(1) - We only use two pointers and constant extra space
"""

def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome after removing non-alphanumeric characters 
    and converting to lowercase.
    
    Args:
        s: Input string
        
    Returns:
        True if string is palindrome, False otherwise
    """
    # Initialize two pointers
    left, right = 0, len(s) - 1
    
    # Continue until pointers meet
    while left < right:
        # Move left pointer to next alphanumeric character
        while left < right and not s[left].isalnum():
            left += 1
        
        # Move right pointer to previous alphanumeric character
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        # Move pointers towards center
        left += 1
        right -= 1
    
    return True

# Alternative approach: Preprocessing (O(n) space)
def is_palindrome_preprocess(s: str) -> bool:
    """
    Alternative approach: Preprocess string first.
    Time Complexity: O(n)
    Space Complexity: O(n) - For the filtered string
    """
    # Filter alphanumeric characters and convert to lowercase
    filtered = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if filtered string is palindrome
    return filtered == filtered[::-1]

# Test cases
if __name__ == "__main__":
    # Test case 1: Valid palindrome
    s1 = "A man, a plan, a canal: Panama"
    print(f"Input: s = \"{s1}\"")
    print(f"Output: {is_palindrome(s1)}")  # Expected: True
    print()
    
    # Test case 2: Not a palindrome
    s2 = "race a car"
    print(f"Input: s = \"{s2}\"")
    print(f"Output: {is_palindrome(s2)}")  # Expected: False
    print()
    
    # Test case 3: Empty string
    s3 = " "
    print(f"Input: s = \"{s3}\"")
    print(f"Output: {is_palindrome(s3)}")  # Expected: True
    print()
    
    # Test case 4: Single character
    s4 = "a"
    print(f"Input: s = \"{s4}\"")
    print(f"Output: {is_palindrome(s4)}")  # Expected: True
    print()