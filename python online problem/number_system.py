def print_formatted(number):
    for i in range(1,number+1):
        print(f"{i:5}{i:6o}{i:6X}{i:6b}")
            

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)