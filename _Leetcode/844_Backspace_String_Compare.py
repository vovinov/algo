def backspaceCompare(s: str, t: str) -> bool:

    def _helper(string):

        stack = []

        for c in string:

            if c == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(c)

        return "".join(stack)

    return _helper(s) == _helper(t)


print(backspaceCompare(s="ab#c", t="ad#c"))
print(backspaceCompare(s="ab##", t="c#d#"))
print(backspaceCompare(s="a#c", t="b"))
