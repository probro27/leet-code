class Solution {
public:
    bool squareIsWhite(string coordinates) {
        char letter = coordinates[0];
        int number = int(coordinates[1]);
        if(int(letter - 'a') % 2 == 0){
            if(number % 2 == 0){
                return true;
            }
            else {
                return false;
            }
        }
        else {
            if(number % 2 == 0){
                return false;
            }
            else {
                return true;
            }
        }
    }
};