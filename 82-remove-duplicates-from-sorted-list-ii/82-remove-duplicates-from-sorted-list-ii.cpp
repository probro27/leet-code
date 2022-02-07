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
    ListNode* deleteNodes(ListNode* head, int current){
        if(head == NULL){
            return NULL;
        }
        if(head->next != NULL){
            if(head->val == head->next->val){
                current = head->val;
                return deleteNodes(head->next, current);
            }
            else{
                if(head->val == current){
                    return deleteNodes(head->next, current);
                }
                else{
                    ListNode* res = new ListNode(head->val);
                    current = head->val;
                    res->next = deleteNodes(head->next, current);
                    return res;
                }
            }
        }
        else{
            if(head->val == current){
                return deleteNodes(head->next, current);
            }
            else{
                ListNode* res = new ListNode(head->val);
                current = head->val;
                res->next =  deleteNodes(head->next, current);
                return res;
            }
        }
        return deleteNodes(head->next, current);
    }
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* res = new ListNode();
        res = deleteNodes(head, -101);
        return res;
    }
};