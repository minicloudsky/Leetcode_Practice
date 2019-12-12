"""
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，
使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 1笨方法，类似于冒泡排序
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if abs(i-j) == k and nums[i]==nums[j]:
                    return True
        return False


if __name__ == '__main__':
    nums = [1, 1, 2, ]
    k = 2
    solution = Solution()
    print(solution.containsNearbyDuplicate(nums, k))
