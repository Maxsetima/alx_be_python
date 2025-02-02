from bank_account import BankAccount

account = BankAccount(100)
def main():
    command = input("Commands: deposit, withdraw, display: ").lower().strip()
    if command == "deposit":
        amount = float(input("How much do you want to deposit: "))
        print(account.deposit(amount))
    elif command == "withdraw":
        amount = float(input("How much do you want to withdraw: "))
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
            account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()