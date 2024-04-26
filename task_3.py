def is_balanced(expression):
    stack = []
    brackets_map = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != brackets_map[char]:
                return "Несиметрично"
            stack.pop()

    if stack:
        return "Несиметрично"
    else:
        return "Симетрично"