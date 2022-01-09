class Solution {
public:
    int addOvf(int* result, int a, int b)
    {
        *result = a + b;
        if(a > 0 && b > 0 && *result < 0)
            return -1;
        if(a < 0 && b < 0 && *result > 0)
            return -1;
        return (a+b);
    }
    int myAtoi(string s) {
        int n = 0;
        int flag = 0;
        int sign = 0;
        int done = -1;
        for(int i = 0; i<s.length(); i++){
            if(s[i] == ' '){
                if(flag == 0){
                    continue;
                }
                else{
                    break;
                }
            }
            if(s[i] == '-'){
                if(done != -1){
                    break;
                }
                if(flag == 1){
                    break;
                }
                sign = 1;
                done = 1;
                flag = 1;
                continue;
            }
            if(s[i] == '+'){
                if(done != -1){
                    break;
                }
                if(flag == 1){
                    break;
                }
                sign = 0;
                done = 1;
                flag = 1;
                continue;
            }
            if(isdigit(s[i])){
                long long temp = (long long)n * 10 + (long long)(int(s[i]))-48;
                // int *res = new int[(sizeof(int))];
                
                // n = n*10 + int(s[i])-48;
                if(sign == 0){
                    if(temp >= pow(2.0, 31.0)-1){
                        return (int)(pow(2.0, 31.0)-1);
                    }
                    else{
                        n = (int)temp;
                    }
                }
                else{
                   if(temp >= pow(2.0, 31.0)){
                        return (int)(-pow(2.0, 31.0));
                    } 
                    else{
                        n = (int)temp;
                    }
                }
                cout << n << "\n";
                flag = 1;
                continue;
            }
            else{
                break;
            }
        }
        if(sign == 0){
            return n;
        }
        else{
            return -n;
        }
    }
};