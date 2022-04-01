n=int(input())

max=list(map(int,input().split()))
min=list(map(int,input().split()))
sm,sn=0,0
for i in max:
    sm+=abs(i)
for i in min:
    sn+=abs(i)
print(sm+sn)