class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int min = strs[0].length();
        for(int i = 0; i<strs.size(); i++){
            if (strs[i].length()< min){
                min = strs[i].length();
            }
        }
        string prefix = "";
        for(int i = 0; i<min; i++){
            char ch = strs[0][i];
            int flag = 0;
            for(int j = 0; j<strs.size(); j++){
                if(ch != strs[j][i]){
                    flag = -1; 
                    break;
                }
            }
            if(flag == -1){
                break;
            }
            prefix = prefix + ch;
        }
        return prefix;
    }
};