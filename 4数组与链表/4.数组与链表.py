"""
在python中暂时不考虑链表

"""
import random

import numpy as np

# 类型注解
arr: list[int] = [0]
nums: list[int] = [1, 3, 2, 5, 4]

def random_access(nums: list[int]) -> int:
    random_index = random.randint(0, len(nums) - 1)
    random_num = nums[random_index]
    return random_num


# 无重复最长回文子串 正着读 反着读内容一样
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result_str = ''
        # 第一遍判断所有
        if s == s[::-1]:
            return s

        # 第二种情况是其中一部分是最长回文子串
        for char in s:
            result_str += char



s = Solution()

b = s.longestPalindrome("bab")

print(b)




