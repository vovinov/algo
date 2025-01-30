def isValid(s: str) -> bool:

    brackets = {")": "(", "}": "{", "]": "["}

    stack = []

    for br in s:
        if br not in brackets:
            stack.append(br)
        else:
            top_element = stack.pop() if stack else "_"
            if brackets[br] != top_element:
                return False

    return not stack


print(isValid("(})"))  #  true
