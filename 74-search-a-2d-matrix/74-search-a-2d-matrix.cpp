class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int highI = matrix.size()-1;
        int lowI = 0;
        int highJ = matrix[0].size()-1;
        int lowJ = 0;
        int midI = 0;
        if(target < matrix[0][0]){
            return false;
        }
        else if(target > matrix[highI][highJ]){
            return false;
        }
        while(highI >= lowI){
            midI = (highI + lowI)/2;
            if(matrix[midI][0] > target){
                highI = midI-1;
            }
            else if(matrix[midI][0] < target){
                lowI = midI+1;
            }
            else{
                return true;
            }
        }
        cout << midI << "\n";
        if(target < matrix[midI][0] && midI != 0){
            midI--;
        }
        if(midI < matrix.size()-1){
            if(target > matrix[midI+1][0]){
                midI++;
            }
        }
        while(highJ >= lowJ){
            int midJ = (highJ + lowJ)/2;
            if(matrix[midI][midJ] > target){
                highJ = midJ-1;
            }
            else if(matrix[midI][midJ] < target){
                lowJ = midJ + 1;
            }
            else{
                return true;
            }
        }
        return false;
    }
};