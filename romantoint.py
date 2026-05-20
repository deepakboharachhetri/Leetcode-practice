
import time
def timer(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        print("process_time",time.time()-start_time)
        return result
    return wrapper


class Solution:
    @timer
    def romanToInt(self, s: str) -> int:
        roman = {
                    "I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000
                }
        total=0
        length_s=len(s)
        for i in range(length_s):
            value_str_value=roman.get(s[i])
            # print(s[i],s[i+1])
            if i<length_s-1 and roman.get(s[i+1])>value_str_value :
                total-=value_str_value
            else:
                total+=value_str_value
        return total
s=Solution()           
print(s.romanToInt(s="MCMXCIV"))
print(s.romanToInt(s="LVIII"))
print(s.romanToInt(s="III"))



class SolutionOptimize:
    @timer
    def romanToInt(self, s: str) -> int:
        roman = {
                    "I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000
                }
        total=0
        prev=0
        for ch in reversed(s):
            value=roman[ch]
            if value<prev:
                total-=value
            else:
                total+=value
            prev=value
        return total
s=SolutionOptimize()           
print(s.romanToInt(s="MCMXCIV"))
print(s.romanToInt(s="LVIII"))
print(s.romanToInt(s="III"))


class SolutionOptimize2:
    @timer
    def romanToInt(self, s: str) -> int:
        roman = {
                    "I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000
                }
        total=0
        length_s=len(s)
        for i in range(length_s):
            value_str_value=roman[s[i]]
            if i<length_s-1 and roman[s[i+1]]>value_str_value :
                total-=value_str_value
            else:
                total+=value_str_value
        return total
s=SolutionOptimize2()           
print(s.romanToInt(s="MCMXCIV"))
print(s.romanToInt(s="LVIII"))
print(s.romanToInt(s="III"))