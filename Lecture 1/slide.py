
# ============================================================
#                 PYTHON BASIC PROGRAMMING
#                  COMPLETE BEGINNER TUTORIAL
# ============================================================


# ============================================================
# 1. PRINTING OUTPUT
# ============================================================

print("Hello World")
print("Welcome to Python")
print(100)
print(10 + 20)

print("Name:", "Sahrior")
print("Age:", 22)


# ============================================================
# 2. VARIABLES AND DATA TYPES
# ============================================================

age = 22
cgpa = 3.75
name = "Sahrior"
is_student = True

print(age)
print(cgpa)
print(name)
print(is_student)

print(type(age))
print(type(cgpa))
print(type(name))
print(type(is_student))


# ============================================================
# 3. TAKING INPUT FROM USER
# ============================================================

name = input("Enter your name: ")
print("Hello", name)

age = int(input("Enter your age: "))
print("Age:", age)

cgpa = float(input("Enter your CGPA: "))
print("CGPA:", cgpa)


# ============================================================
# 4. ARITHMETIC OPERATIONS
# ============================================================

a = 20
b = 6

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)


# ============================================================
# 5. SHORTHAND OPERATORS
# ============================================================

a = 10

a += 5
print(a)

a -= 3
print(a)

a *= 2
print(a)

a //= 4
print(a)

a %= 4
print(a)


# ============================================================
# 6. COMPARISON OPERATORS
# ============================================================

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# ============================================================
# 7. CONDITIONAL STATEMENTS (IF, ELIF, ELSE)
# ============================================================

marks = 75

if marks >= 80:
    print("A+")

elif marks >= 70:
    print("A")

elif marks >= 60:
    print("A-")

else:
    print("Fail")


# ============================================================
# 8. NESTED IF
# ============================================================

age = 22
has_id = True

if age >= 18:

    if has_id:
        print("Entry allowed")

    else:
        print("ID required")

else:
    print("Too young")


# ============================================================
# 9. LOGICAL OPERATORS
# ============================================================

age = 22
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")

if age >= 18 or has_id:
    print("Condition satisfied")

is_raining = False

if not is_raining:
    print("We can go outside")


# ============================================================
# 10. FOR LOOP
# ============================================================

for i in range(1, 6):
    print(i)

# Increment by 2
for i in range(1, 11, 2):
    print(i)

# Decrement by 1
for i in range(5, 0, -1):
    print(i)


# ============================================================
# 11. SUM USING FOR LOOP
# ============================================================

n = 5
total = 0

for i in range(1, n + 1):
    total += i

print("Sum:", total)


# ============================================================
# 12. WHILE LOOP
# ============================================================

i = 1

while i <= 5:
    print(i)
    i += 1


# ============================================================
# 13. SUM USING WHILE LOOP
# ============================================================

n = 5
i = 1
total = 0

while i <= n:
    total += i
    i += 1

print("Total:", total)


# ============================================================
# 14. NESTED LOOPS
# ============================================================

for i in range(1, 4):

    for j in range(1, 4):
        print(i, j)


# ============================================================
# 15. STAR PATTERN
# ============================================================

for i in range(1, 6):

    for j in range(i):
        print("*", end="")

    print()


# ============================================================
# 16. BREAK AND CONTINUE
# ============================================================

# Break
for i in range(1, 10):

    if i == 5:
        break

    print(i)


# Continue
for i in range(1, 6):

    if i == 3:
        continue

    print(i)


# ============================================================
# 17. LIST (ARRAY)
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(numbers)

# Accessing elements
print(numbers[0])
print(numbers[1])

# Updating elements
numbers[0] = 100

print(numbers)

# Length
print(len(numbers))


# ============================================================
# 18. LIST OPERATIONS
# ============================================================

numbers = [10, 20, 30]

# Add element
numbers.append(40)
print(numbers)

# Insert at index
numbers.insert(1, 15)
print(numbers)

# Remove value
numbers.remove(20)
print(numbers)

# Remove using index
numbers.pop(0)
print(numbers)

# Sort
numbers.sort()
print(numbers)

# Reverse
numbers.reverse()
print(numbers)


# ============================================================
# 19. TRAVERSING A LIST
# ============================================================

numbers = [10, 20, 30, 40, 50]

# Using index
for i in range(len(numbers)):
    print(numbers[i])

# Direct traversal
for value in numbers:
    print(value)


# ============================================================
# 20. TAKING LIST INPUT
# ============================================================

n = int(input("Enter array size: "))

numbers = []

for i in range(n):
    value = int(input("Enter number: "))
    numbers.append(value)

print("Array:", numbers)


# ============================================================
# 21. MAXIMUM, MINIMUM AND SUM OF ARRAY
# ============================================================

numbers = [10, 50, 20, 80, 30]

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))


# ============================================================
# 22. TWO DIMENSIONAL ARRAY (2D LIST)
# ============================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][0])
print(matrix[1][2])

for i in range(3):

    for j in range(3):
        print(matrix[i][j], end=" ")

    print()


# ============================================================
# 23. STRING OPERATIONS
# ============================================================

name = "Python Programming"

print(name)
print(len(name))

print(name[0])
print(name[1])

print(name.upper())
print(name.lower())

print(name.replace("Python", "Java"))
print(name.find("Programming"))

print("Python" in name)


# ============================================================
# 24. STRING TRAVERSING
# ============================================================

name = "Python"

for i in range(len(name)):
    print(name[i])


# ============================================================
# 25. STRING SLICING
# ============================================================

name = "Programming"

print(name[0:4])
print(name[4:])
print(name[:6])
print(name[::-1])


# ============================================================
# 26. BASIC FUNCTION
# ============================================================

def greet():
    print("Hello World")
    print("Welcome to Python")

greet()


# ============================================================
# 27. FUNCTION WITH PARAMETERS
# ============================================================

def add(a, b):
    result = a + b
    print("Sum:", result)

add(10, 20)
add(50, 30)


# ============================================================
# 28. FUNCTION WITH RETURN
# ============================================================

def add(a, b):
    return a + b

result = add(10, 20)

print(result)


# ============================================================
# 29. FUNCTION TO FIND MAXIMUM
# ============================================================

def find_max(a, b, c):

    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    else:
        return c

result = find_max(10, 50, 30)

print("Maximum:", result)


# ============================================================
# 30. DEFAULT PARAMETERS
# ============================================================

def greet(name="Student"):
    print("Hello", name)

greet()
greet("Sahrior")


# ============================================================
# 31. RECURSION - FACTORIAL
# ============================================================

def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

result = factorial(5)

print("Factorial:", result)


# ============================================================
# 32. DICTIONARY
# ============================================================

student = {
    "name": "Sahrior",
    "age": 22,
    "cgpa": 3.75
}

print(student["name"])
print(student["age"])

# Update
student["cgpa"] = 3.80

# Add new key
student["department"] = "CSE"

print(student)


# ============================================================
# 33. DICTIONARY TRAVERSING
# ============================================================

student = {
    "name": "Sahrior",
    "age": 22,
    "cgpa": 3.75
}

for key, value in student.items():
    print(key, ":", value)


# ============================================================
# 34. TUPLE
# ============================================================

numbers = (10, 20, 30, 40)

print(numbers)
print(numbers[0])
print(numbers[2])
print(len(numbers))


# ============================================================
# 35. SET
# ============================================================

numbers = {10, 20, 30, 20, 10}

print(numbers)

numbers.add(40)
numbers.remove(20)

print(numbers)


# ============================================================
# 36. SORTING
# ============================================================

numbers = [5, 2, 8, 1, 9, 3]

# Ascending
numbers.sort()
print(numbers)

# Descending
numbers.sort(reverse=True)
print(numbers)


# ============================================================
# 37. SORTED FUNCTION
# ============================================================

numbers = [5, 2, 8, 1, 9]

new_list = sorted(numbers)

print("Original:", numbers)
print("Sorted:", new_list)


# ============================================================
# 38. LIST COMPREHENSION
# ============================================================

numbers = [i for i in range(1, 6)]
print(numbers)

squares = [i * i for i in range(1, 6)]
print(squares)

even = [i for i in range(1, 11) if i % 2 == 0]
print(even)


# ============================================================
# 39. EXCEPTION HANDLING
# ============================================================

try:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter valid numbers")

finally:
    print("Program finished")


# ============================================================
# 40. MULTIPLE INPUTS IN ONE LINE
# ============================================================

# Example input: 10 20 30

a, b, c = map(int, input().split())

print(a, b, c)


# Taking multiple numbers into a list

numbers = list(map(int, input().split()))

print(numbers)


# ============================================================
# 41. BUILT-IN FUNCTIONS
# ============================================================

numbers = [10, 20, 30, 40, 50]

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))

print(abs(-10))
print(pow(2, 3))
print(round(3.14159, 2))
print(type(numbers))


# ============================================================
# 42. FILE HANDLING
# ============================================================

# Writing
with open("data.txt", "w") as file:
    file.write("Learning Python")

# Reading
with open("data.txt", "r") as file:
    content = file.read()
    print(content)


# ============================================================
# 43. LAMBDA FUNCTION
# ============================================================

square = lambda x: x * x

print(square(5))

add = lambda a, b: a + b

print(add(10, 20))


# ============================================================
# 44. ENUMERATE
# ============================================================

numbers = [10, 20, 30, 40]

for index, value in enumerate(numbers):
    print(index, value)


# ============================================================
# 45. ZIP
# ============================================================

names = ["Rahim", "Karim", "Sahrior"]
ages = [20, 21, 22]

for name, age in zip(names, ages):
    print(name, age)


# ============================================================
# 46. COMPETITIVE PROGRAMMING TEMPLATE
# ============================================================

# n = int(input())
# arr = list(map(int, input().split()))

# total = 0

# for i in range(n):
#     total += arr[i]

# print(total)


# ============================================================
#                  END OF PYTHON TUTORIAL
# ============================================================
