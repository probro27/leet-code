class Solution {
public:
    string intToRoman(int num) {
        int n = num;
        int digits = 0;
        // while(n!=0){
        //     n = n/10;
        //     digits++;
        // }
        // int power = digits - 1;
        // vector<char> symbols{'X', 'C', 'M'};
        string roman = "";
        while(num!=0){
            int d = num%10;
            if(digits == 0){
                if(d < 4){
                    for(int j = 0; j<d; j++){
                        roman = 'I' + roman;
                    }
                }
                else if(d >= 5 && d != 9){
                    roman = 'V' + roman;
                    for(int j = 0; j<d-5; j++){
                        roman = roman + 'I';
                    }
                }
                else if(d == 4){
                    roman = roman + "IV";
                }
                else{
                    roman = roman + "IX";
                }
            }
            else if(digits == 1){
                if(d < 4){
                    for(int j = 0; j<d; j++){
                        roman = 'X' + roman;
                    }
                }
                else if(d >= 5 && d != 9){
                    string temp = "L";
                    for(int j = 0; j<d-5; j++){
                        temp = temp + "X";
                    }
                    roman = temp + roman;
                }
                else if(d == 4){
                    roman = "XL" + roman;
                }
                else{
                    roman = "XC" + roman;
                }
            }else if(digits == 2){
                if(d < 4){
                    for(int j = 0; j<d; j++){
                        roman = "C" + roman;
                    }
                }
                else if(d >= 5 && d != 9){
                    string temp = "D";
                    for(int j = 0; j<d-5; j++){
                        temp = temp + "C";
                    }
                    roman = temp + roman;
                }
                else if(d == 4){
                    roman =  "CD" + roman;
                }
                else{
                    roman =  "CM" + roman;
                }
            }
            else{
                for(int j = 0; j<d; j++){
                    roman = "M" + roman;
                }
            }
            digits++;
            num = num/10;
        }
        return roman;
    }
};