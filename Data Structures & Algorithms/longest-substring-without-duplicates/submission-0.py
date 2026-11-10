class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # a set for non-repeating char detection
        unique_subS = set()
        l = 0
        res = 0
        for i in range(len(s)):
            # while char in the set
            while s[i] in unique_subS:
                # remove char from set
                unique_subS.remove(s[l])
                # increment length
                l += 1
            # if not in set, add it to the set
            unique_subS.add(s[i])
            # iterative result = max(current res, window size)
            res = max(res, i - l + 1)
        return res