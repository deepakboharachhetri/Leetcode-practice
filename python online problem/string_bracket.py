class Solution:
    def isValid(self, s: str) -> bool:
        stack=list()
        bracket={'(':')','{':'}','[':']'}
        for i in s:
            if i in bracket.keys():
                stack.append(i)
                print(stack)
            else:
                print(stack)
                if i != bracket.get(stack[-1]) or len(stack)==0:
                   return False
                stack.pop()          
        return len(stack)==0

s=Solution()

print(s.isValid("()"))      # True
print(s.isValid("([)]"))    # False
print(s.isValid("[()]"))    # True
print(s.isValid("{[]}"))    # True
print(s.isValid("()[]{}"))    # True