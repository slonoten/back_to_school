class Solution:
    @staticmethod
    def squeeze_pattern(p: str) -> Tuple[Tuple[str, bool]]:
        pattern_full = [(f, s == '*') for f, s in  [*zip(p, p[1:] + " ")] if f != '*']       
        pattern = []
        prev_any = None
        for ch, is_any in pattern_full:
            if is_any and prev_any in (ch, "*"):
                continue
            prev_any = ch if is_any else None
            pattern.append((ch, is_any))
        return tuple(pattern)
    
    @staticmethod
    def trim_back(s: str, p: List[Tuple[str, bool]]) -> Tuple[bool, int]:
        for i, (s_ch, (p_ch, is_any)) in enumerate(zip(s[::-1],  p[::-1])):
            if is_any: 
                break
            if p_ch == '.' or s_ch == p_ch:
                continue
            return False, 0
        return True, i
            
    def isMatch(self, s: str, p: str) -> bool:
        pattern = self.squeeze_pattern(p)
        match_possible, n_matched = self.trim_back(s, pattern)
        if not match_possible:
            return False
        candidates = [(s[:-n_matched], pattern[:-n_matched]) if n_matched else (s, pattern)]
        #candidates = [(s, pattern)]
        #candidate_idx = 0
        checked = set()
        while candidates:
            s, p = candidates.pop()
            if (s, p) in checked:
                continue
            #candidate_idx += 1
            if not s and not p:
                return True 
            i = 0
            for i, (s_ch, (p_ch, is_any)) in enumerate(zip(s,  p)):
                if is_any:
                    break
                if not (p_ch == '.' or p_ch == s_ch):
                    break
            else:
                if len(s) == len(p):
                    return True # Pattern and string finished
                if len(s) > len(p):
                    continue # Pattern is over but we have not matched symbols
                i = len(s) # String is over but ramaining pattern can match empty string
            if not p[i][1]:
                checked.add((s, p))
                continue
            if (s[i:], p[i + 1:]) not in checked:
                candidates.append((s[i:], p[i + 1:])) # * means 0 matches too
            p_ch = p[i][0]
            for j in range(i, len(s)):
                ch = s[j]
                if p_ch == '.' or p_ch == ch:
                    if ((s[j + 1:], p[i + 1:]) not in checked):
                        candidates.append((s[j + 1:], p[i + 1:]))
                else:
                    break
            checked.add((s, p))
        return False