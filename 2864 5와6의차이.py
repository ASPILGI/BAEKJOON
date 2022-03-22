// 문자열 변환을 하기위해서는 정수로 입력값을 받으면 안된다 //
A,B = input().split()

min =  int(A.replace('6', '5')) + int(B.replace('6', '5'))
max =  int(A.replace('5', '6')) + int(B.replace('5', '6'))
print(min, max)

