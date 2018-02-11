import timeit

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """ 
        if x < 0:
            result = -int(str(abs(x))[::-1])
        else:
            result = int(str(x)[::-1])
            
        if result > 2**31 - 1 or result < -2**31 + 1:
            return 0
        else:
            return result

if __name__ == '__main__':
    x = 1534236469
    start_time = timeit.default_timer()
    print(Solution().reverse(x))
    print(timeit.default_timer() - start_time)