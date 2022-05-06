class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for i in s:
            if i.isalnum():
                word += i
        # print(str)
        word = word.lower()
        print(word)
        res = ""
        for i in word:
            res = i + res
        print(res)
        if res == word:
            return True
        else:
            return False
        