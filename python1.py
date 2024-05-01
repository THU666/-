#第一道题
def get_number(source, target):
    # 创建一个字典来存储源字符串中每个字符的最后出现位置
    last_index = {}
    for i, char in enumerate(source):
        last_index[char] = i

    # 初始化变量
    number = 0
    idx = -1

    # 遍历目标字符串中的每个字符
    for char in target:
        # 如果字符不在源字符串中，则返回 -1
        if char not in last_index:
            return -1
        # 如果当前字符的索引小于或等于上一个索引，则意味着我们需要开始一个新的子序列
        if last_index[char] <= idx:
            number += 1
            idx = -1
        # 更新索引为当前字符的最后出现位置
        idx = last_index[char]

    # 如果最后一个索引不是 -1，则增加一个子序列
    if idx != -1:
        number += 1

    return number