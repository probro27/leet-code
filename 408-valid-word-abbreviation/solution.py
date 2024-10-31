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

        if current_number != 0:
            abbrSplit.append(current_number)
        
        wordLength = len(word)
        current_index = 0
        for element in abbrSplit:
            if isinstance(element, int):
                if current_index + element > wordLength:
                    return False
                else:
                    current_index += element
            else:
                if element != word[current_index]:
                    return False
                current_index += 1
        
        if current_index != len(word):
            return False
        
        return True

    def test(self):
        assert self.validWordAbbreviation('internationalization', 'i12iz4n') == True
        assert self.validWordAbbreviation('apple', 'a2e') == False
        assert self.validWordAbbreviation('substitution', 's10n') == True
        assert self.validWordAbbreviation('substitution', 'sub4u4') == True
        assert self.validWordAbbreviation('substitution', '12') == True
        assert self.validWordAbbreviation('substitution', 'su3i1u2on') == True
        assert self.validWordAbbreviation('substitution', 'substitution') == True
        assert self.validWordAbbreviation('substitution', 's55n') == False
        assert self.validWordAbbreviation('substitution', 's010n') == False
        assert self.validWordAbbreviation('substitution', 's0ubstitution') == False
        assert self.validWordAbbreviation('substitution', 's12') == False
        
        
if __name__ == '__main__':
    solution = Solution()
    solution.test()
    