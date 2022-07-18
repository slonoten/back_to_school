/*
Given a matrix and a target, return the number of non-empty submatrices that
sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with 
x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if 
they have some coordinate that is different: for example, if x1 != x1'.
*/

public class NaiveSolution {
    public int NumSubmatrixSumTarget(int[][] matrix, int target) 
    {
        var matchCounter = 0;
        var n = matrix.Length;
        var m = matrix[0].Length;
        for(var i = 0; i < n; i++)
        {
            for (var j = 0; j < m; j++)
            {
                for (var k = i + 1; k < n + 1; k++)
                {
                    for (var l = j + 1; l < m + 1; l ++)
                    {
                        var sum = SumSubmatrix(matrix, j, i, l, k);
                        if (sum == target)
                        {
                            matchCounter++;
                        }
                    }
                }
            }
        }
        
        return matchCounter;
        
        int SumSubmatrix(int[][] matrix, int x1, int y1, int x2, int y2)
        {
            var sum = 0;
            for (var i = y1; i < y2; i++)
            {
                for (var j = x1; j < x2; j++)
                {
                    sum += matrix[i][j];
                }
            }
            
            return sum;
        }
    }
}


public class SumIncrementSolution {
    public int NumSubmatrixSumTarget(int[][] matrix, int target) 
    {
        var matchCounter = 0;
        var n = matrix.Length;
        var m = matrix[0].Length;
        for(var i = 0; i < n; i++)
        {
            for (var j = 0; j < m; j++)
            {
                for (var k = i + 1; k < n + 1; k++)
                {
                    var sum = 0;
                    for (var l = j ; l < m; l++)
                    {
                        sum += SumSubcolumn(matrix, l, i, k);
                        if (sum == target)
                        {
                            matchCounter++;
                        }
                    }
                }
            }
        }
        
        return matchCounter;
        
        int SumSubcolumn(int[][] matrix, int x, int y1, int y2)
        {
            var sum = 0;
            for (var i = y1; i < y2; i++)
            {
                sum += matrix[i][x];
            }
            
            return sum;
        }
    }
}


public class IncrementalPlusPrefixSumSolution {
    public int NumSubmatrixSumTarget(int[][] matrix, int target) 
    {
        var matchCounter = 0;
        var n = matrix.Length;
        var m = matrix[0].Length;
        
        var sumMatrix = new int[n, m + 1];
        
        for(var i = 0; i < n; i++)
        {
            var sum = 0;
            for (var j = 0; j < m; j++)
            {
                sum += matrix[i][j];
                sumMatrix[i, j + 1] = sum;
            }
        }
        
        
        for(var i = 0; i < n; i++)
        {
            for (var j = 0; j < m; j++)
            {
                for (var k = j + 1; k < m + 1; k++)
                {
                    var sum = 0;
                    for (var l = i ; l < n; l++)
                    {
                        sum += sumMatrix[l, k] - sumMatrix[l, j];
                        if (sum == target)
                        {
                            matchCounter++;
                        }
                    }
                }
            }
        }
        
        return matchCounter;
    }
}


public class PlusSubrowsSumHashmapSolution {
    public int NumSubmatrixSumTarget(int[][] matrix, int target) 
    {
        var matchCounter = 0;
        var n = matrix.Length;
        var m = matrix[0].Length;
        
        var sumMatrix = new int[n, m + 1];
        
        for(var i = 0; i < n; i++)
        {
            var sum = 0;
            for (var j = 0; j < m; j++)
            {
                sum += matrix[i][j];
                sumMatrix[i, j + 1] = sum;
            }
        }
        
        
        for(var i = 0; i < m; i++)
        {
            for (var j = i + 1; j < m + 1; j++)
            {
                // i to j - all rows combinations
                var sumCounts = new Dictionary<int, int>();
                sumCounts[0] = 1;
                var sum = 0;
                for (var k = 0; k < n; k++)
                {
                    sum += sumMatrix[k, j] - sumMatrix[k, i];

                    var count = 0;
                    if (sumCounts.TryGetValue(sum - target, out count))
                    {
                        matchCounter += count;
                    }

                    count = 0;
                    sumCounts.TryGetValue(sum, out count);
                    sumCounts[sum] = count + 1;
                }
            }
        }
        
        return matchCounter;
    }
}