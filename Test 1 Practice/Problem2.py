
n = int(input())

arr = []

arr = list(map(int,input().split()))

evenSum = 0
oddSum =0;

for i in range (0,n,1):
    if(arr[i]%2==0):
        evenSum = evenSum + arr[i]
    else:
        oddSum = oddSum + arr[i]

print(evenSum, " ", oddSum)
