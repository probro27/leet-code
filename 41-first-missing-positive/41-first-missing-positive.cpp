class Solution {
    map<int, int> hash;
public:
    int firstMissingPositive(vector<int>& nums) {
        int size = nums.size();
        for(int i = 1; i <= size; ++i){
            hash[i] = 0;
        }
        for(int i = 0; i <size; ++i){
            if(hash.find(nums[i]) != hash.end()){
                hash[nums[i]] = 1;
            }
        }
        for(auto i = hash.begin(); i != hash.end(); ++i){
            if(i->second == 0){
                return i->first;
            }
        }
        return (nums.size() + 1);
    } 
};