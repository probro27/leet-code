class Solution {
    typedef unordered_map<int, int> hashmap;
    hashmap mymap;
public:
    int fib(int n) {
        if(n <= 1){
            return n;
        }
        if(mymap.find(n) == mymap.end()){
            mymap[n] = fib(n - 1) + fib(n - 2);
        }
        return mymap[n];
    }
};