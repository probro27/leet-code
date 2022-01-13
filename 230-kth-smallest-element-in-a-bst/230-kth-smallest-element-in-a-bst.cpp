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
    int size(TreeNode* root, int count){
        if(root == nullptr){
            return count;
        }
        else{
            return (size(root->left, 0) + size(root->right, 0) + 1);
        }
    }
    int kthSmallest(TreeNode* root, int k) {
        int l = size(root->left, 0);
        // cout << k << " " << l << "\n";
        if(k > l+1){
            // cout << "case 1" << "\n";
            return kthSmallest(root->right, k-l-1);
        }
        else if(k < l+1){
            // cout << "case 1" << "\n";
            return kthSmallest(root->left, k);
        }
        else{
            return root->val;
        }
    }
};