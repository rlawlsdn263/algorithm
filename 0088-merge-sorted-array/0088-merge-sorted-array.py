class Solution:
    def merge(self, nums1, m, nums2, n):
        p1 = m - 1
        p2 = n - 1
        i = m + n - 1
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
            i -= 1
        
        # If there are remaining elements in nums2, copy them
        nums1[:p2 + 1] = nums2[:p2 + 1]