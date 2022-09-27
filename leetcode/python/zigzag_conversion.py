"""The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        row_idx = 0
        down = True
        for c in s:
            rows[row_idx].append(c)          
            if down:
                row_idx += 1
                if row_idx == numRows:
                    row_idx -= 2
                    down = False
            else:
                row_idx -= 1
                if row_idx < 0:
                    row_idx = 1
                    down = True
        return "".join("".join(row) for row in rows)


class SolutionSlicesToLines:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        step = (numRows - 1) * 2
        
        lines = [None] * numRows
        lines[0] = s[::step]
        lines[-1] = s[numRows - 1::step]
        for j in range(1, numRows - 1):
            lines[j] = "".join((f + s) for f, s in zip(s[j::step], s[step - j::step] + " ")).rstrip() 
        return "".join(lines)


class SolutionSlicesToSlices:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        s = bytes(s, "ascii")    
        step = (numRows - 1) * 2
        length = len(s)
        res = [0] * length
        head = s[::step]
        res[:len(head)] = head 
        tail = s[numRows - 1::step]
        if tail:
            res[-len(tail):] = tail
        pos = len(head)
        for j in range(1, numRows - 1):
            odds = s[j::step]
            evens = s[step - j::step]
            res[pos: pos + len(odds) * 2:2] = odds
            res[pos + 1: pos + len(evens) * 2 + 1:2] = evens
            pos += len(odds) + len(evens)
        return "".join(res)