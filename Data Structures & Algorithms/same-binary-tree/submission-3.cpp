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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        stack <TreeNode*> a;
        stack <TreeNode*> b;
        if (p==nullptr && q==nullptr)
            return true;
        else if (p!=nullptr && q!=nullptr)
        {
            a.push(p);
            b.push(q);
        }
        else
        {
            return false;

        }

        while( !a.empty() && !b.empty())
        {
            TreeNode* node1 = a.top();
            a.pop();
            TreeNode* node2 = b.top();
            b.pop();
            if(node1->val!=node2->val)
                return false;
            if(node1->right!= nullptr && node2->right != nullptr)
            {
                    a.push(node1->right);
                    b.push(node2->right);
            }
            else if(node1->right!= nullptr or node2->right != nullptr)
                return false;


            if(node1->left!= nullptr && node2->left != nullptr)
            {
                    a.push(node1->left);
                    b.push(node2->left);

            }
            else if(node1->left!= nullptr or node2->left != nullptr)
                return false;


        }
        return true;
    }
};
