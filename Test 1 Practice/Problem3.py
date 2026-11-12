#Take an integer N and print its multiplication table from 1 to 20. 
#However, skip the multiples of 3 and stop printing when the result exceeds 100.

n = int(input())

for i in range(1,20,1):
    multi = i*n
    if(multi%3!=0 and multi<=100):
        print(multi)
