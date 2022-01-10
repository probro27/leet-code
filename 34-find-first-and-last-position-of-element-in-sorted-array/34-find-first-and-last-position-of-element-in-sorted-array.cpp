class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int high = nums.size()-1;
        int low = 0;
        // int mid;
        int flag = 0;
        int resultMid = 0;
        while(high >= low){
            int mid = (high+low)/2;
            if(nums[mid]<target){
                low = mid + 1;
            }
            else if(nums[mid]>target){
                high = mid - 1;
            }
            else{
                flag = 1;
                resultMid = mid;
                break;
            }
        }
        if((flag == 0) && (high < low)){
            vector<int> res{-1, -1};
            return res;
        }
        cout << flag << "\n";
        cout << resultMid << "\n";
        int startPos = resultMid;
        int endPos = resultMid;
        while(startPos >= 0 && nums[startPos] == target){
            startPos--;
        }
        while(endPos < nums.size() && nums[endPos] == target){
            endPos++;
        }
        vector<int> res {startPos+1, endPos-1};
        return res;
    }
};