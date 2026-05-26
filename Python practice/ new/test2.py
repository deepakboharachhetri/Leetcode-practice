
def shuffle(nums: List[int], n: int) -> List[int]:
    temp=0
    new_list=[]
    for  i in range(2*n):
        if i%2==0:
            if i==0:
                new_list.append(nums[0])
                print("hello",i,new_list)
            else:
                new_list.append(nums[i-1])
                print("hello2",i,new_list)

        else:
            new_list.append(nums[n])
            print("hello",i,new_list,nums[n],n)
            n+=1

    return new_list


print(shuffle(nums=[2,5,1,3,4,7],n=3))
[2, 3, 5, 4, 3, 7]