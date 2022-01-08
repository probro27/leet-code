/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* recursiveAdd(ListNode* l1, ListNode* l2, int carry){
        if(l1 == NULL && l2 == NULL){
            if(carry != 0){
                return new ListNode(carry);
            }
            else{
                return NULL;
            }
        }
        int sum = 0;
        ListNode* currentNode = new ListNode(0);
        if(l1 == NULL){
            sum = 0 + l2->val + carry;
            carry = sum/10;
            currentNode = new ListNode(sum % 10);
            currentNode->next = recursiveAdd(NULL, l2->next, carry);
        }
        else if(l2 == NULL){
            sum = 0 + l1->val + carry;
            carry = sum/10;
            currentNode = new ListNode(sum % 10);
            currentNode->next = recursiveAdd(l1->next, NULL, carry);
        }
        else{
            sum = l1->val + l2->val + carry;
            carry = sum/10;
            currentNode = new ListNode(sum % 10);
            currentNode->next = recursiveAdd(l1->next, l2->next, carry);
        }
        return currentNode;
    }
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        int sum = l1->val + l2->val + carry;
        carry = sum/10;
        ListNode* rootNode = new ListNode(sum % 10);
        rootNode->next = recursiveAdd(l1->next, l2->next, carry);
        return rootNode;
    }
};