class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:        
        current_number = 0
        abbrSplit = []
        
        for ch in abbr:
            if '0' <= ch <= '9':
                current_number = (current_number * 10) + int(ch)
                if current_number == 0:
                    return False
            else:
                if current_number != 0:
                    abbrSplit.append(current_number)
                current_number = 0
                abbrSplit.append(ch)

        wordLength = len(word)
        current_index = 0
        for element in abbrSplit:
            if isinstance(element, int):
                if current_index + element >= wordLength:
                    return False
                else:
                    current_index += element
            else:
                if element != word[current_index]:
                    return False
                current_index += 1
        
        return True

    def test(self):
        assert self.validWordAbbreviation('internationalization', 'i12iz4n') == True
        assert self.validWordAbbreviation('apple', 'a2e') == False
        
        
if __name__ == '__main__':
    solution = Solution()
    solution.test()
    