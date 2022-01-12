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
    int length(ListNode* head, int count){
        if(head == NULL){
            return count;
        }
        return length(head->next, count+1);
    }
    ListNode* deleteNode(ListNode* head, int n, ListNode* store){
        ListNode* tempList = new ListNode();
        if(head == NULL){
            return NULL;
        }
        if(n == 1){
            tempList->val = head->val;
            if(head->next != NULL){
                ListNode* temp = head->next;
                tempList->next = deleteNode(temp->next, n-1, store);
            }
            else{
                tempList->next = NULL;
            }
        }
        else{
            tempList->val = head->val;
            tempList->next = deleteNode(head->next, n-1, store);
        }
        return tempList;
        // return (deleteNode(head->next, n-1, store));
    }
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int l = length(head, 0);
        int startPos = l-n;
        if(startPos == 0){
            if(head != NULL){
                return head->next;
            }
            else{
                return NULL;
            }
        }
        ListNode* store = new ListNode();
        ListNode* result = deleteNode(head, startPos, store);
        return result;
    }
};