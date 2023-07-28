
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        left = 0
        right = 0
        k = len(p)

        p_count = Counter(p)
        window_count = Counter()

        while right < len(s):
            # Expand the window to the right
            window_count[s[right]] += 1
            
            # Shrink the window from the left if it exceeds the desired size k
            if right - left + 1 > k:
                window_count[s[left]] -= 1
                if window_count[s[left]] == 0:
                    del window_count[s[left]]
                left += 1

            # Check if the current window is an anagram
            if right - left + 1 == k and window_count == p_count:
                res.append(left)

            right += 1

        return res
