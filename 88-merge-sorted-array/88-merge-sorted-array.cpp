class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int total_length = n + m;
        vector<int> final_array (total_length);
        if(m!=0 && n!= 0){
            int i = 0;
            int j = 0;
            for(int k = 0; k < total_length; k++){
                if((j >= n) || ((nums1[i] <= nums2[j]) && (i < m) )){
                    final_array[k] = nums1[i];
                    i++;
                }
                else{
                    final_array[k] = nums2[j];
                    j++;
                }
            }
            for(int l = 0; l < total_length; l++){
                nums1[l] = final_array[l];
            }
        }
        else if(m == 0 && n!= 0){
            for(int i = 0; i < total_length; i++){
                nums1[i] = nums2[i];
            }
        }
    }
};