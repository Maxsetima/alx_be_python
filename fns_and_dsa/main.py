from arithmetic_operations import perform_operation

print("Arithmetic Operations")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
operations = perform_operation(num1, num2, operation)
print(operations)