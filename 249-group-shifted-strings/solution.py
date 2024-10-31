class Solution:
    def encodeShiftedString(self, word: str) -> str:
        if word == '':
            return ''

        encodedString = '0,'

        for idx, ch in enumerate(word[:len(word) - 1]):
            encodedString += f'{((ord(word[idx + 1]) - ord(ch)) % 26)},'

        return encodedString

    def groupShiftedStrings(self, words: list[str]) -> list[list[str]]:
        encodeToStringMap = {}
        
        for word in words:
            encodedString = self.encodeShiftedString(word)
            if encodedString in encodeToStringMap:
                encodeToStringMap[encodedString].append(word)
            else:
                encodeToStringMap[encodedString] = [word]
        
        return [val for val in encodeToStringMap.values()]
    
    def test(self):
        assert self.groupShiftedStrings(["abc","bcd","acef","xyz","az","ba","a","z"]) == [['abc', 'bcd', 'xyz'], ['acef'], ['az', 'ba'], ['a', 'z']]
        assert self.groupShiftedStrings(["a"]) == [['a']]
        
if __name__ == '__main__':
    solution = Solution()
    solution.test()
