class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> results;
        sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size(); i++){
             if(i > 0 and nums[i] == nums[i - 1])
                 continue;
            int target1 = target - nums[i];
            for(int j = i + 1; j < nums.size()-1; j++){
                if(j > i + 1 and nums[j] == nums[j - 1]) 
                    continue;
                int low = j + 1;
                int high = nums.size()-1;
                int target2 = target1 - nums[j];
                while(high > low){
                    // if(high < nums.length()-1 && nums[high] == nums[high+1]){
                    //     high--;
                    //     continue;
                    // }
                    int sum = nums[high] + nums[low];
                    if(sum > target2){
                        high--;
                    }
                    else if(sum < target2){
                        low++;
                    }
                    else{
                        vector<int> temp = {nums[i], nums[j], nums[low], nums[high]};
                        results.push_back(temp);
                        while(low < high and nums[low] == temp[2]) 
                            low++;
                        while(high > low and nums[high] == temp[3]) 
                            high--;
                    }
                }
            }
        }
        return results;
    }
};