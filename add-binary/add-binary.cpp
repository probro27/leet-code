class Solution {
public:
    string addBinary(string a, string b) {
        string s = "";
        int flag = 0;
        string rev_a = "";
        string rev_b = "";
        for(int i = a.length()-1; i>=0; i--){
            rev_a = rev_a + a[i];
        }
        for(int i = b.length()-1; i>=0; i--){
            rev_b = rev_b + b[i];
        }
        if(a.length() < b.length()){
            for(int j = 0; j<b.length()-a.length(); j++){
                rev_a = rev_a + '0';
            }
        }
        else{
            for(int j = 0; j<a.length()-b.length(); j++){
                rev_b = rev_b + '0';
            }
        }
        int maxlength = max(a.length(), b.length());
        for(int i = 0; i<maxlength; i++){
            if(rev_a[i] == '0' && rev_b[i] == '0'){
                if(flag == 1){
                    s = s + '1';
                    flag = 0;
                }
                else{
                    s = s + '0';
                }
            }
            else if((rev_a[i] == '1' && rev_b[i] == '0') || (rev_a[i] == '0' && rev_b[i] == '1')){
                if(flag == 1){
                    s = s + '0';
                }
                else{
                    s = s + '1';
                }
            }
            else {
                if(flag == 1){
                    s = s + '1';
                }
                else {
                    s = s + '0';
                    flag = 1;
                }
            }
        }
        if(flag == 1){
            s = s + '1';
        }
        string result = "";
        for(int i = s.length()-1; i>=0; i--){
            result = result + s[i];
        }
        return result;
    }
};