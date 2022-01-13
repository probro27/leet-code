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
    TreeNode* insert(TreeNode* root, int val){
        if(root == nullptr){
            return new TreeNode(val);
        }
        else{
            if(root->val < val){
                return new TreeNode(root->val, root->left, insert(root->right, val));
            }
            else if(root->val > val){
                return new TreeNode(root->val, insert(root->left, val), root->right);
            }
            else{
                return root;
            }
        }
    }
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        if(preorder.size() == 0){
            return nullptr;
        }
        TreeNode* root = new TreeNode(preorder[0]);
        for(int i = 1; i <preorder.size(); i++){
            root = insert(root, preorder[i]);
        }
        return root;
    }
};