import timeit
# 方法一 对连续出现字条串

# class Solution:
#     def longestPalindrome(self, s):
#         """
#         :type s: str eqgjjgqf
#         :rtype: str
#         """
#         repeat = []
#         substring_map = {}
#         start = 0
#         length = len(s)
#         norepeat = []
#         maxLength = 1
#         for w in s:
#             if w not in norepeat:
#                 norepeat.append(w)

#         if length == 0 or length == 1 or len(''.join(norepeat)) == 1:
#             return s

#         for i in range(length):
#             posithon = substring_map.get(s[i])
#             print("i->{0} posithon->{1} start->{2}".format(i, posithon, start))
#             if posithon is not None:
#                 if s[posithon:i+1] == s[posithon:i+1][::-1]:
#                     repeat.append(s[posithon:i+1])
#                 else:
#                     repeat.append(s[i])
#             substring_map[s[i]] = i
#         print(substring_map)
#         print(repeat)
        
#         return max(repeat, key=len)

# 方法二 超时 https://stackoverflow.com/questions/17217473/python-search-longest-palindromes-within-a-word-and-palindromes-within-a-word-s

# class Solution:
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         if len(s) == 0 or len(s) == 1:
#             return s
#         text = s.lower()
#         repeat = []
#         length = len(s)        
#         if length == 0 or length == 1:
#             return s

#         for i in range(length):
#             for j in range(0, i + 1):
#                 chunk = text[j:i + 1]
#                 if chunk == chunk[::-1]:
#                     repeat.append(chunk)
#         print(repeat)
        
#         if len(repeat) == 0:
#             return ''
#         else:
#             return max(repeat, key=len)

# 方法三  OK

class Solution:
    def longestPalindrome(self, s):
        if len(s) == 0 or len(s) == 1:
        	return s
        maxLen = 1
        start = 0
        for i in range(len(s)):
            print("i->{0} maxLen->{1} start->{2}".format(i, maxLen, start))
            if i - maxLen >= 1 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1:i + 1][::-1]:
                start = i - maxLen - 1
                maxLen += 2
                print('maxLen->{0} start->{1} return->{2}'.format(maxLen, start, s[start:start+maxLen]))
                continue

            if i - maxLen >= 0 and s[i - maxLen:i + 1] == s[i - maxLen:i + 1][::-1]:
                start = i - maxLen
                maxLen += 1
                print('maxLen->{0} start->{1} return->{2}'.format(maxLen, start, s[start:start+maxLen]))
                # print('maxLen->{0}'.format(maxLen))

        return s[start:start+maxLen]
                

if __name__ == '__main__':
    # str = "aa"
    # str = "anana"
    str = "rgczcpratwyqxaszbuwwcadruayhasynuxnakpmsyhxzlnxmdtsqqlmwnbxvmgvllafrpmlfuqpbhjddmhmbcgmlyeypkfpreddyencsdmgxysctpubvgeedhurvizgqxclhpfrvxggrowaynrtuwvvvwnqlowdihtrdzjffrgoeqivnprdnpvfjuhycpfydjcpfcnkpyujljiesmuxhtizzvwhvpqylvcirwqsmpptyhcqybstsfgjadicwzycswwmpluvzqdvnhkcofptqrzgjqtbvbdxylrylinspncrkxclykccbwridpqckstxdjawvziucrswpsfmisqiozworibeycuarcidbljslwbalcemgymnsxfziattdylrulwrybzztoxhevsdnvvljfzzrgcmagshucoalfiuapgzpqgjjgqsmcvtdsvehewrvtkeqwgmatqdpwlayjcxcavjmgpdyklrjcqvxjqbjucfubgmgpkfdxznkhcejscymuildfnuxwmuklntnyycdcscioimenaeohgpbcpogyifcsatfxeslstkjclauqmywacizyapxlgtcchlxkvygzeucwalhvhbwkvbceqajstxzzppcxoanhyfkgwaelsfdeeviqogjpresnoacegfeejyychabkhszcokdxpaqrprwfdahjqkfptwpeykgumyemgkccynxuvbdpjlrbgqtcqulxodurugofuwzudnhgxdrbbxtrvdnlodyhsifvyspejenpdckevzqrexplpcqtwtxlimfrsjumiygqeemhihcxyngsemcolrnlyhqlbqbcestadoxtrdvcgucntjnfavylip"
    start_time = timeit.default_timer()
    print(Solution().longestPalindrome(str))
    print(timeit.default_timer() - start_time)