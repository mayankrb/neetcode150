from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        check_dict = { "}":"{", "]":"[", ")":"(" }
        for ch in s:
            if ch in check_dict.keys():
                if not stack or stack[-1]!=check_dict[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        if stack:
            return False
        return True