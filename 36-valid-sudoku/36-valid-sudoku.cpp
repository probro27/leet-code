class Solution {
public:
    bool checkRows(vector<vector<char>>& board, int size){
        for(int i = 0; i<size; i++){
            vector<char> temp;
            // int len = 0;
            int flag = 0;
            for(int j = 0; j<size; j++){
                if(board[i][j] == '.'){
                    continue;
                }
                if(find(temp.begin(), temp.end(), board[i][j]) == temp.end()){
                    temp.push_back(board[i][j]);
                }
                else{
                    return false;
                }
            }
        }
        return true;
    }
    bool checkColumns(vector<vector<char>>& board, int size){
         for(int i = 0; i<size; i++){
            vector<char> temp;
            // int len = 0;
            int flag = 0;
            for(int j = 0; j<size; j++){
                if(board[j][i] == '.'){
                    continue;
                }
                if(find(temp.begin(), temp.end(), board[j][i]) == temp.end()){
                    temp.push_back(board[j][i]);
                }
                else{
                    return false;
                }
            }
        }
        return true;
    }
    bool isValidSudoku(vector<vector<char>>& board) {
        bool checkRow = checkRows(board, 9);
        bool checkColumn = checkColumns(board, 9);
        if(checkRow && checkColumn){
            int i = 0;
            int j = 0;
            // cout << "Rows and columns checked" << "\n";
            while(i < 9){
                j = 0;
                while(j < 9){
                    vector<char> tempBoard;
                    for(int k = i; k<i+3; k++){
                        for(int l = j; l<j+3; l++){
                            if(board[k][l] == '.'){
                                continue;
                            }
                            tempBoard.push_back(board[k][l]);
                        }
                    }
                    // bool checkSubRow = checkRows(tempBoard, 3);
                    // bool checkSubColumns = checkColumns(tempBoard, 3);
                    bool wasUnique;
                    if(tempBoard.size() == 0){
                        wasUnique = true;
                        cout << i << " " << j  << "\n";
                    }
                    else{
                        sort(tempBoard.begin(), tempBoard.end());
                        auto it = unique(tempBoard.begin(), tempBoard.end());
                        wasUnique = (it == tempBoard.end());
                        for(int m = 0; m <tempBoard.size(); m++){
                            cout << tempBoard[m] << " ";
                        }
                        cout << "\n";
                        cout << i << " " << j << " " << wasUnique << "\n";
                    }
                    if(wasUnique){
                        // i = i + 3;
                        j = j + 3;
                    }
                    else{
                        return false;
                    }
                }
                cout << "i incremented" << "\n";
                i = i +3;
                
            }
            return true;
        }
        else{
            return false;
        }
        
    }
};