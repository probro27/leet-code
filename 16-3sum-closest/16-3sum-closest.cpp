class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int closest = 0;
        int dev = INT_MAX; 
        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size()-2; i++){
            if(i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            int sum = 0;
            int temp_dev = 0;
            int high = nums.size() - 1;
            int low = i + 1;
            while(low < high){
                if(high < nums.size()-1 && nums[high] == nums[high+1]){
                    high--;
                    continue;
                }
                sum = nums[i] + nums[low] + nums[high];
                temp_dev = abs(target-sum);
                // cout << temp_dev << "\n";
                if(temp_dev < dev){
                    // cout << "hello" << sum << "\n";
                    if(temp_dev == 0){
                        return target;
                    }
                    
                    closest = sum;
                    dev = temp_dev;
                }
                if(sum < target){
                    low++;
                }
                else{
                    high--;
                }
            }
        }
        return closest;
    }
};