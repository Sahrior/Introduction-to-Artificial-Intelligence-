# Creating a tuple
student = ("Rahim", 20, "CSE", 3.75)

# Printing the complete tuple
print("Student Information:", student)

# Accessing tuple elements
print("Name:", student[0])
print("Age:", student[1])
print("Department:", student[2])
print("CGPA:", student[3])

# Finding the length of the tuple
print("Total Elements:", len(student))

# Checking if an element exists
if "CSE" in student:
    print("CSE Department Found!")

# Looping through the tuple
print("\nStudent Details:")
for item in student:
    print(item)