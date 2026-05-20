



# decorator
import time
def time_decoration(func):
    def wrapper(*args,**kwargs):
       start_time=time.time()
       result=func(*args,**kwargs)
       print("time",time.time()-start_time)
       return result
    return wrapper

class Palindrome:
    @time_decoration
    def using_loop(self, nums: int):

        if nums < 0:
            return False

        original = nums
        reverse_value = 0

        while nums:

            reverse_value = reverse_value * 10 + nums % 10

            nums //= 10

        return original == reverse_value

    @time_decoration
    def using_comprehension1(self,nums:int):
        if str(nums)==str(nums)[::-1]:
            return True
        return False
        
    @time_decoration
    def using_comprehension2(self,nums:int):
        nums_str=str(nums)
        return nums_str==nums_str[::-1]

    @time_decoration
    def using_join(self,nums:int):
        nums_str=str(nums)
        return nums_str == "".join(reversed(nums_str))
    @time_decoration
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        while x > reversed_half:

            reversed_half = reversed_half * 10 + x % 10

            x //= 10

        return x == reversed_half or x == reversed_half // 10

if __name__=="__main__":
    p=Palindrome()
    result=p.using_loop(nums=121)
    print("result",result)
    result=p.using_comprehension1(nums=121)
    print("result",result)
    result=p.using_comprehension2(nums=121)
    print("result",result)
    result=p.using_join(nums=121)
    print("result",result)
    result=p.isPalindrome(x=121)
    print("result",result)