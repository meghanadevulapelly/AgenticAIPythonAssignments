# Input student details
name = input("Enter student name: ")
maths = int(input("Enter Maths marks: "))
physics = int(input("Enter Physics marks: "))
chemistry = int(input("Enter Chemistry marks: "))

# Calculate total
total = maths + physics + chemistry

# Assign grade
if total >= 270:
    grade = "A"
elif total >= 240:
    grade = "B"
elif total >= 180:
    grade = "C"
else:
    grade = "D"

# Display result
print("\nStudent Name:", name)
print("Total Marks:", total)
print("Grade:", grade)