class Solution {
public:
    int strStr(string haystack, string needle) {
        int len = needle.length();
        if(len == 0){
            return 0;
        }
        else if(haystack.length()<len){
            return -1;
        }
        else if(haystack.length() == len){
            if(haystack == needle){
                return 0;
            }
            else{
                return -1;
            }
        }
        for(int i = 0; i<haystack.length()-len+1; i++){
            string temp = haystack.substr(i, len);
            //cout << temp << "\n";
            if(temp == needle){
                return i;
            }
        }
        return -1;
    }
};