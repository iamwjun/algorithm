class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        numbs3 = nums1 + nums2
        numbs3.sort()
        length = len(numbs3)
        type = length % 2
        if type == 0:
            re = (numbs3[int(length/2)] + numbs3[int(length/2) - 1]) /2
        else:
            re = numbs3[length//2]

        return re

if __name__ == '__main__':
    nums1 = [1,2]
    nums2 = [3,4]
    print(Solution().findMedianSortedArrays(nums1, nums2))