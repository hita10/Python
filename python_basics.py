# PYTHON BASICS 
#  Variables and Data Types
user_name = "Alex"     
user_age = 21         
gpa = 3.85             
is_enrolled = True      

print(f"Student: {user_name}, Age: {user_age}, GPA: {gpa}, Active: {is_enrolled}")

#  Basic Operators & Math Operations
num_a = 15
num_b = 4

addition = num_a + num_b
floor_div = num_a // num_b  
modulus = num_a % num_b    
power = num_a ** num_b     

print(f"Floor Div: {floor_div}, Modulus: {modulus}, Power: {power}")

#  Conditional Statements 
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

print(f"Calculated Grade: {grade}")

#  Loops 

print("--- For Loop Execution ---")
for i in range(1, 4):
    print(f"Iteration step: {i}")

# While Loop
print("--- While Loop Execution ---")
counter = 3
while counter > 0:
    print(f"Countdown: {counter}")
    counter -= 1