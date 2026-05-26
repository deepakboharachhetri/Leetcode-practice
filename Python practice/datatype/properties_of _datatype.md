# Datatype core properties in python 
python basic format:  
 In python everything is an object.Each object has
 - Type(what kind of data it is)
 - Identity(memory address)
 - value  
 for example :`x=5`
    - Type -> int
    - Identity ->:memory address
    - value -> 5  
### Core Properties of Datatype
#### 1.Mutability
If any object that can be change or not change after creation is called mutability feature

- Types:
  - Immutable:
    - Object that cannot be change after creation( return error if trying to update or change)

    - while changing value it create new object (and assign new refrence to the variable)
    
    - stored in fixed memory and cannot change size/value

    - Internal Mecahnism step by step :
      - object created in memory
      - value stored
      - Any modification -> new object created
      - Old object remains unchanged (garbage collected old object)

    - for example :int, float, double,Nonetype, frozenset, range, bool, tuple, string(the method that update the string create a new object), etc 


  - Mutable : 
    - object that can change after creation

    - while changing value it update on the same object 

    - stored with dynamic memory and can grow/shrink(methods directly modify internal architecture)

    - Internal Mecahnism step by step :
      - object created
      - reference stored
      - Methods modify same memory
      - New object needed

    - for example Dict, List, set
    
    - Note: if list or dict consist immutable element then it will be immutable

### 2.Iterability
object that can be looped over using for.

- Iterable object must be instance of Iterable class <pre>from collections.abc import Iterable
print(isinstance([1,2,3], Iterable))  # True
print(isinstance(10, Iterable))       # False</pre>

- Types:
    - Iterable :list, str, set, dict, range, bytes 
    - Non-Interable : int, float, double, complex, boolean 

- Internal Mechanism
  - iterator tool (iterator datatype like str, tuple, set, dict, list, etc.)
  - it use iterator method `iter(obj) or obj.__iter___()`
  - get an iterator
  - calls `next(obj) or obj.__next__()`
  - stops iteration when `StopIteration` is raised

- methods :
  - `iter(obj)`- (recommended, safety, readibility, didnot raise exception) than `obj.__iter__()`  
  Note :if obj hasnot iter then it check `__getitem__(index)` except dict

  - `next(obj)` -(recommended, safety, readibility, didnot raise exception) than `obj.__next__()`
  
  - `enumerate()`
    - syntax:  
    `enumerate(iterable, start=0)`

    - it create tuple with index (index, value)

  - `zip()`
    - syntax: 
    - example :<pre>
    names = ["a", "b", "c"]
    nums = [1, 2, 3]
    z = zip(names, nums)
    print(list(z))
    [('a', 1), ('b', 2), ('c', 3)] #output
    </pre> 
    - it creates tuple not a list it create iterator 
        >(names[0], nums[0])  
        >(names[1], nums[1])  
        >(names[2], nums[2])

    - for unzipping
    <pre>
    pairs = [('a', 1), ('b', 2), ('c', 3)]
    a, b = zip(*pairs)
    </pre>

### 3.Indexibility
Access element using index or position 
- Internal Mechanism 
  - python calls `obj.__get__items(index)`
  - return value at that memory position

- Types
   - Indexable: list, tuple, str, range,etc.
   - Non Indexable: set, dict



### 4.Order
whether the elements maintain insertion order
- Types :
  - ordered:list, tuple, str, dict(3.7+)
  - unordered:set


### 5. Hashability:
whatether  an object can be converted into a fixed integer value(hash value) using built in function .

- Types :
  - hashable: int, float, tuple
  - unhashable: list, dict, set 

- Internal mechanism:
  - Python computes `hash(obj)`
  - stores in hash table 
  - must be immutable

### 6.Homogenity(Type consistency) 
whather a data structure requires all elements to be of the same type.

- Python is not strictly homogenous( unlike like c arrays)

- python internal reason because it store reference not raw value so type doesnot matter

- but in sorted or comparision the datatype must be same 
 <pre>sorted([1,'a']) #TypeError</pre>
 <pre>[1]+['a'] #works</pre>


- Type :

  - Heterogenous :
    - most of the datatype are heterogenous except string

  - Homogenous :
    - example :string


### 7.Dynamic Sizing
whether an object can grows or shrink at runtime

- dynamic sized : list, set, dict 
- fixed sized : int, float, str, tuple

- Internally:
- python allocates extra memory(capacity >size)
- when 2/3 of size full:
   - allocates bigger block 
   - copies elements 
   - updates references 