def perform_operation(num1, num2, operation):
    """Accepts numbers as input and perform arithmetric operation with (add, subtract, divide and multiply, then return a message to the user if divisor is 0)"""
    if operation == 'add':
        num1 + num2
        result = num1 + num2
        return f"Result: {result}"
    elif operation == 'subtract':
        num1 - num2
        result = num1 + num2
        return f"Result: {result}"
    elif operation == 'multiply':
        result = num1 * num2
        return f"Result: {result}"
    elif operation == 'divide':
        if num2 == 0:
            result = f"{num1} cannot be divided by 0"
            return result
        else:
            result = num1 / num2
            return f"Result: {result}"