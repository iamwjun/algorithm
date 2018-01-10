import timeit
from operator import is_not
from functools import partial
from itertools import combinations, permutations

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        retype = 0
        re = []
        for c in s:
            if c not in re:
                re.append(c)
        i = len(''.join(re))
        l = ''.join(re)
        if i == len(s):
            return i
        while i > 0:
            for w in list(permutations(l, i)):
                # print("string:{0} bool:{1}".format(''.join(w), ''.join(w) in s))
                if ''.join(w) in s:
                    retype = len(''.join(w))
            if retype > 0:
                break
            i = i - 1

        return retype


if __name__ == '__main__':
    str = "xrstenkqqpj"
    start_time = timeit.default_timer()
    print(Solution().lengthOfLongestSubstring(str))
    print(timeit.default_timer() - start_time)
