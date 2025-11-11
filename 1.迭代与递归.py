"""
迭代说的就是for循环
递归说的就是重复调用一个函数
"""
# for循环实现迭代
def for_loop(n: int) -> int:
    res = 0
    for i in range(1, n + 1):
        res += i

    return res

# while循环实现迭代
def while_loop(n: int) -> int:
    res = 0
    i = 1
    while i <= n:
        res += i
        i += 1
    return res


# 嵌套循环
def nested_for_loop(n: int) -> str:
    res = ""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            res += f"({i}, {j})"
    return res


# 递归 终止条件 递归调用 返回结果 注意：编程语言允许的递归深度通常是有限的
# 过深的递归可能导致栈溢出错误
def recure(n: int) -> int:
    if n == 1:
        return 1
    res = recure(n - 1)
    return n + res

# 尾递归 求和是在递的过程中完成的
def tail_recur(n, res):
    if n == 0:
        return res

    # 尾递归调用
    return tail_recur(n - 1, res + n)

# 递归树 斐波那契额数列
def fib(n: int) -> int:
    if n == 1 or n == 2:
        return n - 1

    res = fib(n - 1) + fib(n - 2)

    return res


# 我们可以使用一个显式的栈来模拟调用栈的行为，从而将递归转化为迭代形式
# 主要考虑到入栈和出栈
def for_loop_recur(n: int) -> int:
    # 创建一个栈
    stack = []
    res = 0

    # 递：递归调用
    for i in range(n, 0, -1):
        stack.append(i)

    # 归：返回结果
    while stack:
        # 通过“出栈操作”模拟“归”
        res += stack.pop()

    return res








