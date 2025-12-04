"""
hash表:
    散列表 通过key value映射 哈希表输入一个key 可以在O(1)内得到一个value
哈希冲突：
    多个输入对用同一个输出的情况（容量越大，hash冲突的可能性就越低）
负载因子是hash表的一个重要概念：
    定义：哈希表元素数量除以桶数量，用于衡量哈希冲突的严重程度，也常作为哈希表扩容的触发条件
    在java中 负载因子超过0.75 系统会将哈希表扩容至原先的2倍
哈希表结构改良：
    “链式地址”和“开放寻址”
"""

# 初始化哈希表
hmap: dict = {}

# 添加操作
# 在哈希表中添加键值对 (key, value)
hmap[12836] = "小哈"
hmap[15937] = "小啰"
hmap[16750] = "小算"
hmap[13276] = "小法"
hmap[10583] = "小鸭"

# 查询操作
# 向哈希表中输入键 key ，得到值 value
name: str = hmap[15937]

# 删除操作
# 在哈希表中删除键值对 (key, value)
hmap.pop(10583)
# print(hmap)


# 遍历哈希表
# 遍历键值对 key->value
for key, value in hmap.items():
    # print(key, "->", value)
    pass
# 单独遍历键 key
for key in hmap.keys():
    # print(key)
    pass
# 单独遍历值 value
for value in hmap.values():
    # print(value)
    pass



"""
哈希表的简单实现 数组实现哈希表
"""
class Pair:
    """键值对"""

    def __init__(self, key: int, val: str):
        self.key = key
        self.val = val

class ArrayHashMap:
    """基于数组实现的哈希表"""

    def __init__(self):
        """构造方法"""
        # 初始化数组，包含 100 个桶
        self.buckets: list[Pair | None] = [None] * 100

    def hash_func(self, key: int) -> int:
        """哈希函数"""
        index = key % 100
        return index

    def get(self, key: int) -> str | None:
        """查询操作"""
        index: int = self.hash_func(key)
        pair: Pair = self.buckets[index]
        if pair is None:
            return None
        return pair.val

    def put(self, key: int, val: str):
        """添加和更新操作"""
        pair = Pair(key, val)
        index: int = self.hash_func(key)
        self.buckets[index] = pair

    def remove(self, key: int):
        """删除操作"""
        index: int = self.hash_func(key)
        # 置为 None ，代表删除
        self.buckets[index] = None

    def entry_set(self) -> list[Pair]:
        """获取所有键值对"""
        result: list[Pair] = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair)
        return result

    def key_set(self) -> list[int]:
        """获取所有键"""
        result = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair.key)
        return result

    def value_set(self) -> list[str]:
        """获取所有值"""
        result = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair.val)
        return result

    def print(self):
        """打印哈希表"""
        for pair in self.buckets:
            if pair is not None:
                print(pair.key, "->", pair.val)


arrayhashmap = ArrayHashMap()
pair = Pair(2, "10")






