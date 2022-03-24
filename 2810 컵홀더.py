n = input()
Seats = input()
result = 0

countL = Seats.count('LL')
countS = Seats.count('S')

if countL > 0:
    result += countL+1
result += countS

print(result)