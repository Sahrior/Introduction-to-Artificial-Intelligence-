#Write a Python program that takes N integers 
#into a list and prints the second-largest distinct number.

n = int(input())

arr = []

arr = list(map(int, input().split()))

mx1 = 0

for i in range (0, n, 1):
    if(arr[i]>mx1):
        mx1 = arr[i]

mx2 = arr[0]
for i in range (1, n, 1):
    if(arr[i] > mx2 and arr[i]<mx1 ):
        mx2 = arr[i]

        
print(mx2)