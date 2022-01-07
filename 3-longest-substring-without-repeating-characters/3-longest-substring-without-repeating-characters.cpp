class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxLength = 0;
        if(s == ""){
            return 0;
        }
        for(int i = 0; i<s.length(); i++){
            vector<char> unique;
            unique.push_back(s[i]);
            int temp = 1;
            for(int j = i+1; j<s.length(); j++){
                if(find(unique.begin(), unique.end(), s[j]) == unique.end()){
                    unique.push_back(s[j]);
                    temp++;
                }
                else{
                    if(temp > maxLength){
                        maxLength = temp;
                    }
                    temp = 1;
                    break;
                }
            }
            if(temp > maxLength){
                maxLength = temp;
            }
        }
        return maxLength;
    }
};