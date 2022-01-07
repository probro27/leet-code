class Solution {
public:
    vector<int> maximumBeauty(vector<vector<int>>& items, vector<int>& queries) {
        vector<int> result(queries.size());
        vector<vector<int>> copy_query(queries.size(), vector(2,0));
        for(int i = 0; i<queries.size(); i++){
            copy_query[i][0] = queries[i];
            copy_query[i][1] = i;
        }
        sort(copy_query.begin(),copy_query.end(),[](vector<int>&a,vector<int>&b){return a[0]<b[0];});
        
        sort(items.begin(),items.end(),[](vector<int>&a,vector<int>&b){return a[0]<b[0];});
        if(items[0][0] == items[items.size()-1][0] && items.size() != 1){
            sort(items.begin(), items.end(), [](vector<int>&a, vector<int>&b){return a[1]<b[1];});
            for(int i = 0; i <queries.size(); i++){
                result[i] = items[items.size()-1][1];
            }
            return result;
        }
        int prevMax = 0;
        int max = 0;
        int x = 0;
        for(int i = 0; i<queries.size(); i++){
            max = 0;
            for(int j = x; j<items.size(); j++){
                if(items[j][0] <= copy_query[i][0]){
                    if(items[j][1] > max){
                       max = items[j][1];
                    }
                }
                else{
                    x = j;
                    break;
                }
            }
            if(max > prevMax){
                result[i] = max;
                // cout << max << "\n";
                prevMax = max;
            }
            else{
                result[i] = prevMax;
            }
        }
        vector<int> answer(result.size());
        for(int k = 0; k<result.size(); k++){
            answer[copy_query[k][1]] = result[k];
        }
        return answer;
    }
};