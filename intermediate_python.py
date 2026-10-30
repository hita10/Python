# Data Structures
fruits = ["apple", "banana", "cherry"]
fruits.append("date")

coordinates = (10.0, 20.5)

student_record = {
    "name": "Sarah",
    "courses": ["CS101", "MATH201"],
    "graduated": False
}

unique_tags = {"python", "coding", "python", "oops"}

print(f"Updated List: {fruits}")
print(f"Student Courses: {student_record['courses']}")
print(f"Unique Tags Set: {unique_tags}")

# Functions and Type Hinting
def calculate_final_price(price: float, discount: float = 0.10) -> float:
    discount_amount = price * discount
    return price - discount_amount

total_cost = calculate_final_price(100.0, 0.15)
print(f"Final Price after discount: ${total_cost:.2f}")

# List Comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_squares = [num ** 2 for num in numbers if num % 2 == 0]
print(f"Squares of even numbers: {even_squares}")