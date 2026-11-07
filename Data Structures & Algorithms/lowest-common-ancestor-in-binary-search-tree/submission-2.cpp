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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode* node = root;
        while(node!=nullptr)
        {
            int value = node->val;
            if(value> p->val && value> q->val)
                node=node->left;
            else if(value< p->val && value< q->val)
                node=node->right;
            else if( value == p->val)
                return p;
            else if( value == q->val)
                return q;
            else
                return node;
            
        }
    return root;   
    }
};
