# class Singleton:
#     _instance=None
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance =super().__new__(cls)
#         return cls._instance
    
# class SingletonExample(Singleton):
#     def __init__(self):
#         print("SingletonExample instance created")

# s1=SingletonExample()
# s2=SingletonExample()  
# print(s1)
# print(s2)       
# print(s1 is s2)
# print(id(s1),id(s2))



def singleton(cls):
    _instance={}
    def get_instance(*args,**kwargs):
        if cls not in _instance:
            _instance[cls]=cls(*args,**kwargs)
        return _instance[cls]
    return get_instance

@singleton
class SingletonExample:
    def __init__(self):
        print("SingletonExample instance created")

s1=SingletonExample()
s2=SingletonExample()  
print(s1)
print(s2)       
print(s1 is s2)
print(id(s1),id(s2))