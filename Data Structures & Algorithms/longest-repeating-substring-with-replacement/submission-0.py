class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict

        count = defaultdict(int)
        max_count = 0  # max freq of any char in window
        left = 0
        result = 0

        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(max_count, count[s[right]])

            # If more than k replacements needed, shrink window
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            # Update result with current window size
            result = max(result, right - left + 1)

        return result
