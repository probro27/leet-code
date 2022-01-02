class Solution {
public:
    int lengthOfLastWord(string s) {
       string word = "";
        vector<string> words;
        int len = 0;
        int x = 0;
        s.erase(s.find_last_not_of(" \n\r\t")+1);
        s = s+ ' ';
        for(int i = 0; i<s.length(); i++){
            char ch = s[i];
            if(ch!=' '){
                word = word + ch;
            }
            else{
                words.push_back(word);
                word = "";
                len++;
            }
        }
        string lastWord = words[len-1];
        return lastWord.length();
    }
};