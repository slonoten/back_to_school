/*
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif
*/

public class Solution {
    public IList<IList<int>> Generate(int numRows) {
        var result = new List<IList<int>>();
        var last = new List<int>();
        last.Add(1);
        result.Add(last);
        for (var i = 1; i < numRows; i++)
        {
            var current = new List<int>(i + 1);
            current.Add(1);
            for(var j = 0; j < i - 1; j++)
            {
                current.Add(last[j] + last[j+1]);
            }
            current.Add(1);
            result.Add(current);
            last = current;
        }
        return result;
    }
}