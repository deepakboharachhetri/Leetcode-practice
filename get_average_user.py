
if __name__=="__main__":
    n=int(input())
    student={}
    for _ in range(n):
        name,*line=input().split()
        score=list(map(float,line))
        student[name]=score
    
    query=input()
    scores=student.get(query)
    score_avg=sum(score)/len(score)
    print(f"{score_avg:.2f}")
    print("{:.2f}".format(score_avg))

