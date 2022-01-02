class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int len = digits.size();
        vector<int> result(len);
        for(int i = 0; i<len; i++){
            result[i] = digits[i];
        }
        if(result[len-1] != 9){
           result[len-1]++;
        }
        else {
            int i = len-1;
            while(i >= 0 && result[i] == 9){
                result[i] = 0;
                i--;
            }
            if(i == -1){
                result.insert(result.begin(), 1);
            }
            else{
                result[i]++;
            }
        }
        return result;
    }
};