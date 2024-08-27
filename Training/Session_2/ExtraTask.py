def is_balanced(s):
    stack = []
    
    matching_pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != matching_pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

# Test cases
print(is_balanced("([]{})"))  # Output should be True
print(is_balanced("([)]"))    # Output should be False
print(is_balanced("{[}]"))    # Output should be False
