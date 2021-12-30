#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool isValid(string s){
    vector<char> paranthesis(s.length());
    int len = 0;
    int flag = 0;
    for(int i = 0; i<s.length(); i++){
        if(s[i] == '[' || s[i] == '{' || s[i] == '('){
            paranthesis[len] = s[i];
            len++;
        }
        else{
            if(len == 0){
                flag = -1;
                break;
            }
            else if(paranthesis[len-1] == '('){
                if(s[i] == ')'){
                    len--;
                }
                else{
                    flag = -1;
                    break;
                }
            }
            else if(paranthesis[len-1] == '{'){
                if(s[i] == '}'){
                    len--;
                }
                else{
                    flag = -1;
                    break;
                }
            }
            else if(paranthesis[len-1] == '['){
                if(s[i] == ']'){
                    len--;
                }
                else{
                    flag = -1;
                    break;
                }
            }
            else {
                flag = -1;
                break;
            }
        }
    }
    if((flag != -1) && (len == 0)){
        return true;
    }
    else {
        return false;
    }
}

int main(){
    string s;
    cin >> s;
    cout << isValid(s) << "\n";
    return 1;
}