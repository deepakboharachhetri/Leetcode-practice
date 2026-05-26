# DataType in python
- Numeric Types :int, float, complex
- Text Type :str 
- Sequence Types :list, tuple, range
- Mapping Type :dict
- Set Types : set,frozenset
- Boolean Type :bool
- Binary Types :bytes, bytearray, memoryview
- None Type :None

### Numeric Types

#### 1.int()
   - syntax   
     x:int
    
   - some methods for integer
     1. `int_obj.id()` --> return object's unique identity -> in cpython its a memory address

     2. Decimal to other base 
        - using direct methods
            - `bin(n)` -to  binary with prefixed 0b
            - `oct(n)` -to octal with prefixed 0o
            - `hex(n) `-to hexadecimal with prefixed 0x  
            Note to remove  prefix we can use slice method 
            `bint(n)[2:]`
        
        - using format method
           - `format(n,'b')` - to binary 
           - `format(n,''o)` - to octal
           - `format(n,'x')` - to hex 

        
     3. other base to decimal
      - using `int()` method
        - `syntax: int(string, base)` 
        - example:
            - int('101',2) - form bin 
            - int('12657',8)- form octal
            - int('12ABD',16)- from hexadecimal  
            Note : scalable
            
      - conversion using f-string
        - hex_value=15 
        - print(f"{hex_value:10b}) # here b is binary and 10 is right aligned  means it allocate 10 spaces even not used if it shift toward left
        - for left we use (>,example {hex_value:>5}) right, (<,example {hex_value:<5})left , (^,example {hex_value:^5}) center


     4. Convert between Non decimal bases
      - first any convert into decimal then convert into other form  
        - example: from octal to hex

        <pre>  
          out_dec=int('1276',8) # convert octal to decimal 
          hex_out = hex(out_dec) # convert decimal to hex
          int("0xa", 0)    # Returns 10 (prefix is required here)   
        </pre>


#### 3. float 


         