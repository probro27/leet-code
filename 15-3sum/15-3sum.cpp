class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        int sum = 0;
        if(nums.size() == 0 || nums.size()==1 || nums.size()==2){
            return result;
        }
        sort(nums.begin(), nums.end());
        for(int i = 0; i<nums.size()-2; i++){
            if(i > 0 && nums[i] == nums[i-1])
                continue;
            sum = 0;
            int high = nums.size()-1;
            int low = i+1;
            while(high > low){
                if(high < nums.size()-1 && nums[high] == nums[high+1]){
                    high--;
                    continue;
                }
                sum = nums[i] + nums[high] + nums[low];
                if(sum > 0){
                    high--;
                }
                else if(sum < 0){
                    low++;
                }
                else{
                    vector<int> temp = {nums[low], nums[i], nums[high]};
                    result.push_back(temp);
                    high--;
                }
            }
        }
        
        return result;
    }
};