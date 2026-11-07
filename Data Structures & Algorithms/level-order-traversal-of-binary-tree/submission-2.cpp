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
    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<TreeNode*> q;
        vector<vector<int>> result;
        if (root == nullptr)
            return result;

        q.push(root);
        vector<int> tmp = {root->val};
        result.push_back(tmp);
        
        int level = 0;
        while(!q.empty())
        {
            vector<int> tmp;
            int levelSize = q.size();
            for (int i=0; i<levelSize; i++)
            {
                TreeNode* node = q.front();
                q.pop();

                if (node->left != nullptr )
                {
                    tmp.push_back(node->left->val);
                    q.push(node->left);
                }

                if (node->right != nullptr )
                {
                    tmp.push_back(node->right->val);
                    q.push(node->right);
                }


            }
            if(!tmp.empty())

                result.push_back(tmp);
            
        }
    return result;
    }
};
