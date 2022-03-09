class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int low = 0;
        int high = nums.size()-1;
        while(high >= low){
            int mid = (high + low)/2;
            int temp = nums[mid];
            if(mid > 0 && mid < nums.size()-1){
                if(nums[mid-1] == temp || nums[mid + 1] == temp){
                    return temp;
                }
            }
            else if(mid == nums.size()-1){
                if(nums[mid-1] == temp){
                    return temp;
                }
            }
            else{
                if(nums[mid+1] == temp){
                    return temp;
                }
            }
            if(mid+1 <= temp){
                low = mid + 1;
            }
            else{
                high = mid - 1;
            }
        }
        return -1;
    }
};