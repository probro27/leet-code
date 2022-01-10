class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int flag = 0;
        int j = 1;
        for(int i = 1; i<nums.size(); i++){
            if(nums[i-1] == nums[i]){
                if(flag == 0){
                    nums[j++] = nums[i];
                    flag = 1;
                }
            }
            else{
                nums[j++] = nums[i];
                flag = 0;
            }
        }
        return j;
    }
};