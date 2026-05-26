

import time 

def timer(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        result=func(*args, **kwargs)
        print("-"*100)
        print("Process_time",time.time()-start_time)
        print("-"*100)
        return result
    return wrapper

def store_log(func):
    def wrapper(*args, **kwargs):
        print("inside decorator")
        print("data",*args,**kwargs)
        result=func(*args, **kwargs)
        print("result is",result)
        print("outside decorator")
        return result
    return wrapper
    

class Employee:
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):

    def __init__(self,fixed_salary:int):
        self.fixed_salary=fixed_salary

    def calculate_salary(self,months:int=1):
        return self.fixed_salary*months


class PartTimeEmployee(Employee):

    def __init__(self,hourly_salary:int):
        self.hourly_salary=hourly_salary

    @store_log
    @timer
    def calculate_salary(self,worked_hours:int):
        return self.hourly_salary*worked_hours



if __name__=="__main__":
    # part-time employee
    part_time_employee_obj=PartTimeEmployee(20)
    print("part time employee salary",part_time_employee_obj.calculate_salary(20))

    # #full-time employee
    # full_time_employee_obj=FullTimeEmployee(3000)
    # print("Full time employee salary",full_time_employee_obj.calculate_salary(2))


    

