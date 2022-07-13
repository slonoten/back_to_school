// Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public IList<IList<int>> LevelOrder(TreeNode root) {
        var nodeQueue = new Queue<(TreeNode node, int level)>();
        var result = new List<IList<int>>();
        if (root is not null)
        {
            nodeQueue.Enqueue((root, 0));
        }
        var currentLevel = 0;
        var levelNodes = new List<int>();
        while(nodeQueue.Count > 0)
        {
            var (node, level) = nodeQueue.Dequeue();
            if (currentLevel < level)
            {
                currentLevel++;
                result.Add(levelNodes);
                levelNodes = new List<int>();
            }
            levelNodes.Add(node.val);
            if (node.left is not null)
            {
                nodeQueue.Enqueue((node.left, level + 1));
            }
            if (node.right is not null)
            {
                nodeQueue.Enqueue((node.right, level + 1));
            }
        }
        if(levelNodes.Count > 0) 
        {
            result.Add(levelNodes);
        }
        return result;
    }
}


public class SolutionFast {
    public IList<IList<int>> LevelOrder(TreeNode root) {
        var nodes = new TreeNode[2000];
        var levels = new int[2000];
        var values = new int[2000];
        var currentLevel = 0;
        var tailIdx = 0;
        var valIdx = 0;
        var result = new List<IList<int>>();
        if (root is not null)
        {
            nodes[0] = root;
            levels[0] = 0;
            values[0] = root.val;
            tailIdx++;
        }
        for (int headIdx = 0; headIdx < tailIdx; headIdx++)
        {
            var node = nodes[headIdx];
            var level = levels[headIdx];
            if (currentLevel != level)
            {
                currentLevel = level;
                result.Add(new List<int>(values[..valIdx]));
                valIdx = 0;
            }
            values[valIdx++] = node.val;            
            if (node.left is not null)
            {
                nodes[tailIdx] = node.left;
                levels[tailIdx] = level + 1;
                tailIdx++;
            }
            if (node.right is not null)
            {
                nodes[tailIdx] = node.right;
                levels[tailIdx] = level + 1;
                tailIdx++;
            }
        }
        if (valIdx > 0)
        {
            result.Add(new List<int>(values[..valIdx]));
        }
        return result;
    }
}