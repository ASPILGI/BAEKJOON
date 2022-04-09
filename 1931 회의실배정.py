n = int(input())
time = [] 
for i in range(n): 
    start, end = map(int, input().split()) 
    time.append([start, end])

time = sorted(time, key = lambda a : (a[0], a[1])) # point 

last_end = 0 
x = 0 

for start, end in time: 
    if start >= last_end:
        x += 1 
        last_end = end 

print(x)

