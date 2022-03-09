/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
    unordered_map<ListNode*, ListNode*> hash;
public:
    bool hasCycle(ListNode *head) {
        ListNode *lst = head;
        while(lst){
            if(hash.find(lst) == hash.end()){
                hash[lst] = lst->next;
            }
            else{
                return true;
            }
            lst = lst->next;
        }
        return false;
    }
};