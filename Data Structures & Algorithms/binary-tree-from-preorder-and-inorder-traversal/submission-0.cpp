/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int preIdx = 0;
    unordered_map<int, int> positionInIO;
    TreeNode* dfs(vector<int>& preorder, int l, int r)
    {
        if (l>r) return nullptr;
        int rootVal = preorder[preIdx];
        preIdx++;
        TreeNode* root = new TreeNode(rootVal);
        int mid = positionInIO[rootVal];
        root->left = dfs(preorder, l, mid-1);
        root->right = dfs(preorder, mid+1, r);
        return root;
    }
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        // if(preorder.empty() || inorder.empty())
        //     return nullptr;
        
        // TreeNode* root = new TreeNode(preorder[0]);
        // auto mid = find(inorder.begin())

        for (int i = 0; i<inorder.size(); i++)
        {
            positionInIO[inorder[i]] = i;
        }
                return dfs(preorder, 0, inorder.size() - 1);


        

        
    }
};
