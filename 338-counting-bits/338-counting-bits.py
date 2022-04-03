class Solution(object):
    def convertBinary(self, n):
        bin_str = ""
        count = 0
        while n != 0:
            if n % 2 == 0:
                bin_str = '0' + bin_str
            else:
                bin_str = '1' + bin_str
                count = count + 1
            n = n // 2
        return count
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        lst = []
        for i in range(n+1):
            lst.append(self.convertBinary(i))
        return lst