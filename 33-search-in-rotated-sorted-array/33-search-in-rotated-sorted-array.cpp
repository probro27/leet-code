class Solution {
public:
    int findPivot(vector<int>& nums, int high, int low){
        if(high < low){
            // cout <<-1 << "\n";
            return -1;
        }
        if(high == low){
            // cout << "low " << low << "\n";
            return low;
        }
        int mid = (high+low)/2;
        if(mid < high && nums[mid]>nums[mid+1]){
            // cout << "mid " << mid << "\n";
            return mid;
        }
        else if(mid > low && nums[mid] < nums[mid-1]){
            return (mid-1);
        }
        else if(nums[mid] <= nums[low]){
            return findPivot(nums, mid-1, low);
        }
        else{
            return findPivot(nums, high, mid+1);
        }
    }
    int binarySearch(vector<int>& nums, int high, int low, int key){
        while(high >= low){
            int mid = (high+low)/2;
            if(nums[mid] > key){
                high = mid-1;
            }
            else if(nums[mid] < key){
                low = mid+1;
            }
            else{
                // cout << "search mid " << mid << "\n";
                return mid;
            }
        }
        return -1;
    }
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        int pivot = findPivot(nums, n-1, 0);
        // int index = 0;
        if(pivot == -1){
            return binarySearch(nums, n-1, 0, target);
        }
        else{
            if(nums[pivot] == target){
                return pivot;
            }
            else{
                if(nums[0] <= target){
                    return binarySearch(nums, pivot-1, 0, target);
                }
                else{
                    return binarySearch(nums, n-1, pivot+1, target);
                }
            }
        }
    }
};