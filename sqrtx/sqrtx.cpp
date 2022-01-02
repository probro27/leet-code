class Solution {
public:
    int mySqrt(int x) {
        int result = 0;
        for(long i = 0; i<=x; i++){
            if(i*i <= x && (i+1)*(i+1) > x){
                result = int(i);
                break;
            }
        }
        return result;
    }
};