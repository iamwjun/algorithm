import timeit

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # for i in range(0, len(str), 3):
        #     print(i, s[i])
        if numRows == 1:
            return s
            
        step, zigzag = 2 * numRows - 2, ''
        for i in range(numRows):
            for j in range(i, len(s), step):
                zigzag += s[j]
                if 0 < i < numRows - 1 and j + step - 2 * i < len(s):
                    zigzag += s[j + step - 2 * i]
        return zigzag

if __name__ == '__main__':
    str = "PAYPALISHIRING"
    start_time = timeit.default_timer()
    print(Solution().convert(str, 3))
    print(timeit.default_timer() - start_time)