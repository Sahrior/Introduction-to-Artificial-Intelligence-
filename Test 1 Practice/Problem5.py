#Given a list of integers, 
#create a new list containing only the distinct 
#elements while maintaining their original order.

n = int(input())

arr = []

arr = list(map(int, input().split()))

new_arr = []

for i in range(len(arr)):
    if arr[i] not in new_arr:
        new_arr.append(arr[i])

print(new_arr)
