import timeit
from operator import is_not
from functools import partial
from itertools import combinations, permutations

# 方法1，数据大时运行速度慢

# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         retype = 0
#         re = []
#         for c in s:
#             if c not in re:
#                 re.append(c)
#         i = len(''.join(re))
#         l = ''.join(re)
#         if i == len(s):
#             return i
#         while i > 0:
#         # f = open('log.txt','w')
#             for w in list(permutations(l, 8)):
#                 # f.write("string:{0} bool:{1}\n".format(''.join(w), ''.join(w) in s))
#                 # print("string:{0} bool:{1}".format(''.join(w), ''.join(w) in s))
#                 if ''.join(w) in s:
#                     print(''.join(w))
#                     retype = len(''.join(w))
#             if retype > 0:
#                 break
#             i = i - 1
#         # f.close()

#         return retype

# 方法2

# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         longest = 0
#         substring_map = {}
#         start = 0
#         for i in range(len(s)):
#             print(i)
#             position = substring_map.get(s[i])
#             if position is not None and position >= start:                 
#                 length = i - start
#                 start = position + 1                
#                 longest = max(length, longest)
#             substring_map[s[i]] = i
#             print(substring_map)

#         longest = max(len(s) - start, longest)
#         return longest

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :a
        :c: int 最长长度
        """
        longest = 0
        substring_map = {}
        start = 0
        for i in range(len(s)):
            position = substring_map.get(s[i])
            if position is not None and position >= start:
                length = i - start
                start = position + 1
                longest = max(length, longest)
            substring_map[s[i]] = i
            print(i)
            print(substring_map)

        longest = max(len(s) - start, longest)
        return longest

if __name__ == '__main__':
    str = "awyuwqeaq"
    start_time = timeit.default_timer()
    print(Solution().lengthOfLongestSubstring(str))
    print(timeit.default_timer() - start_time)
