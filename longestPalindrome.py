import timeit

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        for w in s:
            print(s.index(w))
        return s

if __name__ == '__main__':
    str = "PAYPALISHIRING"
    start_time = timeit.default_timer()
    print(Solution().convert(str, 3))
    print(timeit.default_timer() - start_time)