class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> output(2);
        for(int i = 0; i<nums.size()-1; i++){
            for(int j = i+1; j<nums.size(); j++){
                int sum = 0;
                sum = nums[i] + nums[j];
                if(sum == target){
                    output[0] = i;
                    output[1] = j;
                    break;
                }
            }
        }
        return output;
    }
};