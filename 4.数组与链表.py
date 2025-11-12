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



