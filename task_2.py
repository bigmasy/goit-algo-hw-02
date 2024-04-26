from collections import deque

def is_palindrome(input_str):
    input_str = input_str.lower().replace(" ", "")
    
    char_queue = deque(input_str)
    
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    return True

input_string = input('Введіть рядок для перевірки:')
print(is_palindrome(input_string))
