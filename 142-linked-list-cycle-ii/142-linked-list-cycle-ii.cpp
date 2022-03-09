/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
    unordered_map<ListNode*, int> hash;
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode* lst = head;
        if(!lst || !lst->next){
            return NULL;
        }
        int index = 0;
        while(lst){
            if(hash.find(lst) == hash.end()){
                hash[lst] = index;
            }
            else{
                return (lst);
            }
            lst = lst->next;
            ++index;
        }
        return NULL;
    }
};