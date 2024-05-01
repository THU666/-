# 第二道题
def check_brackets(string):
    stack = []
    result = ''
    for i, char in enumerate(string):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                result += '?'
    while stack:
        result += 'x'
        stack.pop()
    return result