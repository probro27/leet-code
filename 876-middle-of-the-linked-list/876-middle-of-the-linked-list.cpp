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
    ListNode* findNode(ListNode* head, int n){
        if(n == 0){
            return head;
        }
        return findNode(head->next, n-1);
    }
    ListNode* middleNode(ListNode* head) {
        int l = length(head, 0);
        int n = 0;
        if(l % 2 == 0){
            n = l/2;
        }else{
            n = l/2;
        }
        ListNode* result = findNode(head, n);
        return result;
    }
};