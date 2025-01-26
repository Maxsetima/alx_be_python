from datetime import datetime, timedelta

def display_current_datetime():
    """Formats current date and time to YYYY-MM-DD HH:MM:SS"""
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")
    
display_current_datetime()
# prompts the user for number of days
number_of_days = float(input("Enter the number of days to add to the current date: ")) 

def calculate_future_date():
    """Calculate future day by adding number of days(month) to future date entered by user"""
    future_date = datetime.now() + timedelta(days=number_of_days)
    calculated_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {calculated_future_date}")

calculate_future_date()