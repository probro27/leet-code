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
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if(root == NULL){
            TreeNode* head = new TreeNode(val);
            return head;
        }
        else if(root->val < val){
            TreeNode* head = new TreeNode(root->val, root->left, insertIntoBST(root->right, val));
            return head;
        }
        else if(root->val > val){
            TreeNode* head = new TreeNode(root->val, insertIntoBST(root->left, val), root->right);
            return head;
        }
        else{
            return root;
        }
    }
};