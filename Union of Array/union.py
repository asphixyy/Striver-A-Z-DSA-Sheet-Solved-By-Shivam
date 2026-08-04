class Solution:
    def unionArray(self, nums1, nums2):
        for i in nums2:
            if i in nums1:
                continue
            else:
                nums1.append(i)
        return set(nums1)
x=Solution()
print(x.unionArray([3, 4, 6, 7, 9, 9], [1, 5, 7, 8, 8]))
