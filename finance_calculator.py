# finance_calculator.py

# Function to calculate monthly savings and projected annual savings
def finance_calculator():
    # User input for financial details
    monthly_income = float(input("Enter your monthly income: "))
    monthly_expenses = float(input("Enter your total monthly expenses: "))

    # Calculate monthly savings
    monthly_savings = monthly_income - monthly_expenses

    # Calculate projected savings after one year with 5% interest
    projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

    # Output the results
    print(f"Your monthly savings are ${monthly_savings:.2f}.")
    print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")

# Run the function
if __name__ == "__main__":
    finance_calculator()
