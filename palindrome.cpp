#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

bool palindrome(int x){
    if(x<0){
        return false;
    }
    int digits = 0;
    int n  = x;
    while(n != 0){
        digits++;
        n = n/10;
    }
    int divide = 0;
    int flag = 0;
    if(digits % 2 == 0){
        divide = digits/2;
        flag = 0;
    }
    else{
        divide = (digits + 1)/2;
        flag  = 1;
    }
    int factor = pow(10, divide);
    int first_half = x/(factor);
    int second_half = 0;
    if(flag == 1){
        second_half = x%(factor/10);
    }
    else{
        second_half = x%factor;
    }
    int t = second_half;
    int second_digits = 0;
    while(t != 0){
        second_digits++;
        t = t/10;
    }
    int offset = 0;
    if(flag == 1){
        if(second_digits != (divide-1)){
            cout << "reached here for flag =  1" << "\n";
            offset = abs(second_digits - divide + 1);
        }
    }
    else{
        if(second_digits != divide){
            cout << "reached here for flag =  0" << "\n";
            offset = abs(second_digits - divide);
            cout << offset << "\n";
        }
    }
    int rev = 0;
    int num = second_half;
    while(num != 0){
        int d = num%10;
        rev = rev*10 + d;
        num = num/10;
    }
    while(offset != 0){
        rev = rev * 10;
        offset--;
    }
    if(rev == first_half){
        cout << factor << "\n";
        cout << rev << " " << first_half << "\n";
        cout << "true" << "\n";
        return true;
    }
    else{
        cout << factor << "\n";
        cout << rev << " " << first_half << "\n";
        cout << "false" << "\n";
        return false;
    }
}

int main(){
    int n;
    cin >> n;
    cout << palindrome(n) << "\n";
    return 1;
}