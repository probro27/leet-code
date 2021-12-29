class Solution {
public:
    int romanToInt(string s) {
        int sum = 0;
        for(int i = 0; i<s.length(); i++){
            char ch = s[i];
            if(ch == 'M'){
                sum = sum + 1000;
                continue;
            }
            else if(ch == 'C'){
                if(s.substr(i+1) != ""){
                    char c = s[i+1];
                    if(c == 'M'){
                        sum = sum + 900;
                        i++;
                        continue;
                    }
                    else if(c == 'D'){
                        sum = sum + 400;
                        i++;
                        continue;
                    }
                    else{
                        sum = sum + 100;
                        continue;
                    }
                }
                else{
                    sum = sum + 100;
                    continue;
                }
            }
            else if(ch == 'D'){
                sum = sum + 500;
                continue;
            }
            else if(ch == 'X'){
                if(s.substr(i+1) != ""){
                    char c = s[i+1];
                    if(c == 'C'){
                        sum = sum + 90;
                        i++;
                        continue;
                    }
                    else if(c == 'L'){
                        sum = sum + 40;
                        i++;
                        continue;
                    }
                    else{
                        sum = sum + 10;
                        continue;
                    }
                }
                else{
                    sum = sum + 10;
                    continue;
                }
            }
            else if(ch == 'L'){
                sum = sum + 50;
                continue;
            }
            else if(ch == 'I'){
                if(s.substr(i+1) != ""){
                    char c = s[i+1];
                    if(c == 'X'){
                        sum = sum + 9;
                        i++;
                        continue;
                    }
                    else if(c == 'V'){
                        sum = sum + 4;
                        i++;
                        continue;
                    }
                    else{
                        sum = sum + 1;
                        continue;
                    }
                }
                else{
                    sum = sum + 1;
                    continue;
                }
            }
            else if(ch == 'V'){
                sum = sum + 5;
            }
        }
        return sum;
    }
};