n = int(input())
a = list(map(int, input().split())) 

count = 0 

for i in range(n): 
     if a[i] == count % 3:
         count = count + 1 

print(count)
