class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        valid=True
        for i in range(len(s)):
            if s[i] in ['(','{','[']:
                stack.append(s[i])
            elif len(stack)>0:
                poped_bracket=stack.pop()
                if poped_bracket == '(' and s[i] != ')':
                    valid=False
                    break
                elif poped_bracket == '{' and s[i] != '}':
                    valid=False
                    break
                elif poped_bracket == '[' and s[i] != ']':
                    valid=False
                    break
            else:
                valid=False
        if(len(stack)!=0):
            valid=False
        return valid