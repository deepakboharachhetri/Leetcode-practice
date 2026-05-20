# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input("Enter odd number of n:").strip())
if(n%2==0):
    print("Invalid number.Only odd number are allowed.")
    exit()

m=3*n
initial_pattern=".|."
print(f"n:{n},m:{m}")
for i in range(0,n):

    middle_row=n//2
    
    if i < middle_row:
        pattern=initial_pattern*(2*i+1)
    elif i == middle_row:
        pattern="WELCOME"
    else:
        pattern=initial_pattern*(2*(2*middle_row-i)+1)

    half_len_dash = int((m-len(pattern))/2)
    # print(f"i:{i},dash_count:{half_len_dash}")
    column="-"*half_len_dash+pattern+"-"*half_len_dash
    print(column)
        