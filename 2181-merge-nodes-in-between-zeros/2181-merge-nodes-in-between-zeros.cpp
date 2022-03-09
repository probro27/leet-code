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
    ListNode* mergeNodes(ListNode* head) {
        ListNode* res = head->next;
        ListNode* curr = res;
        ListNode* lst = head->next;
        int sum = 0;
        // lst = lst->next;
        while(lst){
            if(lst->val != 0){
                sum = sum + lst->val;
            }
            else{
                res->val = sum;
                res->next = lst->next;
                res = res->next;
                sum = 0;
            }
            lst = lst->next;
        }
        return head->next;
        // return &curr;
    }
};