"""
5栈与队列：
    栈是先进后出
    队列是先进先出
"""

class Stack:
    def __init__(self):
        self.stack = []


    # 入栈
    def push(self, data):
        self.stack.append(data)


    # 出栈
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return -1

    # 判空
    def is_empty(self) -> bool:
        if not self.stack:
            return True
        else:
            return False


class Queue:
    def __init__(self):
        pass

    # 入队

    # 出队

    # 判空

