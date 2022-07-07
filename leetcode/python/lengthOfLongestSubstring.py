"""
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_longest = 0
        unique_start_pos = 0
        char_to_pos = {}
        for i, ch in enumerate(s):
            prev_ch_pos = char_to_pos.get(ch)
            if prev_ch_pos is not None:
                if unique_start_pos == 0:
                    # Нашли первый повтор с начала строки
                    current_longest = i
                else:
                    current_longest = max(current_longest, i - unique_start_pos)
                unique_start_pos = prev_ch_pos + 1
                # Удаляем все символы с позицией до предыдущей позиции ch
                char_to_pos = { c: p for c, p in char_to_pos.items() if p > prev_ch_pos}
            char_to_pos[ch] = i
        return max(current_longest, len(s) - unique_start_pos)


class SolutionEx:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = bytes(s, "ascii")
        current_longest = 0
        unique_start_pos = 0
        char_to_pos = [-1] * 128 # ascii
        for i, ch in enumerate(s):
            prev_ch_pos = char_to_pos[ch]
            if prev_ch_pos >= 0:
                current_longest = max(current_longest, i - unique_start_pos)
                # Удаляем все символы с позицией до предыдущей позиции ch
                for j in range(unique_start_pos, prev_ch_pos + 1):
                    char_to_pos[s[j]] = -1
                unique_start_pos = prev_ch_pos + 1
                # Проверяем условие раннего досрочного завершения
                if current_longest >= len(s) - unique_start_pos:
                    break
            char_to_pos[ch] = i
        return max(current_longest, len(s) - unique_start_pos)


class Solution99PercentFast:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_longest = 0
        unique_start_pos = 0
        str_len = len(s)
        char_to_pos = [-1] * 128 # ascii
        s = bytes(s, "ascii")
        for i in range(str_len):
            ch = s[i]
            prev_ch_pos = char_to_pos[ch]
            if prev_ch_pos >= unique_start_pos:
                if current_longest < i - unique_start_pos:
                    current_longest = i - unique_start_pos
                unique_start_pos = prev_ch_pos + 1
                # Проверяем условие раннего досрочного завершения
                if current_longest >= str_len - unique_start_pos:
                    break
            char_to_pos[ch] = i
        return max(current_longest, str_len - unique_start_pos)        