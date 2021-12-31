class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size();
        int mid=0;
        while(low <= high){
            mid = (low+high)/2;
            if(mid > nums.size()-1 || mid <0){
                break;
            }
            if(nums[mid] > target){
                high = mid - 1;
            }
            else if(nums[mid] < target){
                low = mid + 1;
            }
            else {
                return mid;
            }
        }
        if(!(mid > nums.size()-1)){
            if(nums[mid] < target){
                mid++;
            }
        }
        return mid;
    }
};