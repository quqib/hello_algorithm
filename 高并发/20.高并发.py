"""
并发 并行 同步 异步 阻塞 非阻塞


"""

# 第一种实现多线程的方式
import time
import threading

def task1():
    for i in range(10):
        time.sleep(1)
        print("一边看电视")

def task2():
    for i in range(10):
        time.sleep(1)
        print("一遍嗑瓜子")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

# t1.start()
# t2.start()


# 第二种方式
import time
import threading

class WatchThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        for i in range(10):
            time.sleep(1)
            print("一边看电视")

class EatThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        for i in range(10):
            time.sleep(1)
            print("一边嗑瓜子")


def main():
    wt = WatchThread(name="看电视线程")
    et = EatThread(name="嗑瓜子线程")

    wt.start()
    et.start()


# 通过线程池创建多线程
import time
from concurrent.futures import ThreadPoolExecutor, Executor, Future

def task1(sleep_time):
    # print("hello......")
    time.sleep(sleep_time)
    return "world"

executor = ThreadPoolExecutor(max_workers=3)

fu = executor.map(task1, [1, 2, 3, 2, 1])

# print(fu)
#
# for i in fu:
#     print(i)

# GIL 全局解释器锁 谁用了这个谁就能在CPU中进行执行和运算，谁没有这个锁谁就执行不了 保证在同一时刻只有一个线程执行字节码


# 生成器和迭代器
def my_generator():
   n = 1
   print('这是第一次调用生成器')
   yield n
   n += 1
   print('这是第二次调用生成器')
   yield n
   n += 1
   print('这是第三次调用生成器')
   yield n


# 创建生成器对象
gen = my_generator()
# 获取生成器的下一个值
print(next(gen)) # 输出: 这是第一次调用生成器 1
print(next(gen)) # 输出: 这是第二次调用生成器 2
print(next(gen)) # 输出: 这是第三次调用生成器 3







