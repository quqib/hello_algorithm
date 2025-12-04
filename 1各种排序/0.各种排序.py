s = [9, 5, 10, 113, 1, 15]

"""
冒泡
"""
def bubble(s):
    for i in range(1, len(s)):
        for j in range(1, i + 1):
            if s[i] > s[j]:
                s[i], s[j] = s[j], s[i]

    return s

bubble_ = bubble(s)
print(bubble_)

