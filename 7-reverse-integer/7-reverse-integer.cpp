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
    int reverse(int x) {
        int rev = 0;
        int num = x;
        int flag =0;
        int tag = 0;
        if(num < 0){
            if(num == int(-pow(2.0, 31.0))){
                flag = 1;
                tag = 1;
                num = int(pow(2.0, 31.0)-1);
            }
            else{
                num = abs(num);
                flag = 1;
            }
        }
        while(num != 0){
            int d = num%10;
            try{
                if(tag == 1 && num == x){
                    int *res = new int[(sizeof(int))];
                    try{
                        long long temp = (long long)rev*10;
                        if(temp > pow(2.0, 31.0)-1){
                            return 0;
                        }
                        else{
                            rev = addOvf(res, rev*10, (d+1));
                        }
                    }
                    catch(...){
                        return 0;
                    }
                }
                else{
                    int *res = new int[(sizeof(int))];
                    try{
                        long long temp = (long long)rev*10;
                        if(temp > pow(2.0, 31.0)-1){
                            return 0;
                        }
                        else{
                            rev = addOvf(res, rev*10, d);
                        }
                    }
                    catch(...){
                        return 0;
                    }
                }
                num = num/10;
            }
            catch(...){
                return 0;
            }
            
        }
        if(flag == 0){
            return rev;
        }
        else{
            return (-1)*rev;
        }
    }
};