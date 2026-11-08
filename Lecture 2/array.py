arr = [10, 20, 30, 40, 50]

# 1. append() - Adds an element at the end
print("Original List:", arr)

arr.append(60)
print("After append:", arr)


# 2. insert() - Adds an element at a specific index
arr.insert(2, 100)
print("After insert:", arr)


# 3. remove() - Removes a specific value
arr.remove(30)
print("After remove:", arr)


# 4. pop() - Removes an element by index
arr.pop(1)
print("After pop:", arr)


# find using if else 

arr = [10, 20, 30, 40, 50]

search = int(input("Enter a number to search: "))

if search in arr:
    print("Element found in the array!")
else:
    print("Element not found in the array!")