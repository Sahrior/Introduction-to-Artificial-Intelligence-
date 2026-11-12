#Write a Python program that checks whether a
#given three-digit number is an Armstrong number.

#An Armstrong number is equal to the sum of the cubes of its digits.


n = int(input())

original = n

sum = 0

for i in range(1,4,1):
    m = n%10
    n = n//10
    p = m * m * m
    sum = sum + p

if(sum==original):
    print("Armstrong number")
else:
    print("Not Armstrong number")