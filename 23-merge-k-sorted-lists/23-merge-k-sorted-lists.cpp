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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        vector<int> arr;
        for(int i = 0; i <lists.size(); i++){
            while(lists[i] != NULL){
                arr.push_back(lists[i]->val);
                lists[i] = lists[i]->next;
            }
        }
        sort(arr.begin(), arr.end());
        if(arr.size() == 0){
            return NULL;
        }
        ListNode* res = new ListNode(arr[arr.size()-1]);
        for(int i = arr.size()-2; i >=0 ; i--){
            ListNode* curr = new ListNode(arr[i], res);
            res = curr;
        }
        return res;
    }
};