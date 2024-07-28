### this code attempt evolved over two days, passing test cases, but failing specific tests.  window logic worked until multiples of same character.
### also note this code does not properly handle the sliding window pointers well. this approach costs an n*n space and time complexity.
### this problem is known to have a solution of O(n+m) which I find after abondonment of the below code block.



class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        if t == s:
            return s
        if len(t) == 1 and t in s:
            return t

        # Create frequency dictionaries for t and the current window in s
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        window_count = {}
        have, need = 0, len(t_count)
        res, res_len = [-1, -1], float('inf')
        l = 0

        for r in range(len(s)):
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1

            if char in t_count and window_count[char] == t_count[char]:
                have += 1

            while have == need:
                # Update the result if this window is smaller
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = (r - l + 1)

                # Pop from the left of the window
                left_char = s[l]
                window_count[left_char] -= 1
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r + 1] if res_len != float('inf') else ""
    

### the following solution was attempted, and abandoned, as the time complexity and space complexity are too high.
### both are on the n*n complexities, and when t becomes large the time limit is exceeded.  this is working and brute force, but will not satisfy under the bar for time and space.
### it passed 264 out of 268 cases.  good attempt but crushing that it fails.

#new approach found.


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        if t == s:
            return s
        if len(t) == 1 and t in s:
            return t

        # Create frequency dictionaries for t and the current window in s
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        window_count = {}
        have, need = 0, len(t_count)
        res, res_len = [-1, -1], float('inf')
        l = 0

        for r in range(len(s)):
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1

            if char in t_count and window_count[char] == t_count[char]:
                have += 1

            while have == need:
                # Update the result if this window is smaller
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = (r - l + 1)

                # Pop from the left of the window
                left_char = s[l]
                window_count[left_char] -= 1
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r + 1] if res_len != float('inf') else ""




###  the folowing code focused on efficient use of memory and computaton by using the two pointer approach to the sliding window.
### this solution is O(m+n) or idealized.  Online CHAT GPT wants to use the counter method, but I used proper linear logic to evaluate the dictionaries manually rather than obfuscating somewhat in the counter method.



class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        if t == s:
            return s
        if len(t) == 1 and t in s:
            return t

        # Create frequency dictionaries for t and the current window in s
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        window_count = {}
        have, need = 0, len(t_count)
        res, res_len = [-1, -1], float('inf')
        l = 0

        for r in range(len(s)):
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1

            if char in t_count and window_count[char] == t_count[char]:
                have += 1

            while have == need:
                # Update the result if this window is smaller
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = (r - l + 1)

                # Pop from the left of the window
                left_char = s[l]
                window_count[left_char] -= 1
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r + 1] if res_len != float('inf') else ""

