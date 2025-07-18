
def menu(Accounts, ch):
    while True:
        print(f"\nWelcome to account number {ch}:")
        print("1. CHECK BALANCE")
        print("2. DEPOSIT")
        print("3. WITHDRAW")
        print("4. TRANSFER")
        print("5. LOGOUT")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(f"Current Balance: {Accounts[ch]}")
        elif choice == 2:
            amount = int(input("Enter amount to deposit: "))
            if amount > 0:
                Accounts[ch] += amount
                print(f"Deposited {amount}. New Balance: {Accounts[ch]}")
            else:
                print("Invalid amount.")
        elif choice == 3:
            amount = int(input("Enter amount to withdraw: "))
            if 0 < amount <= Accounts[ch]:
                Accounts[ch] -= amount
                print(f"Withdrew {amount}. New Balance: {Accounts[ch]}")
            else:
                print("Insufficient funds or invalid amount.")
        elif choice == 4:
            target = int(input("Enter recipient account number: "))
            if target in Accounts and target != ch:
                amount = int(input("Enter amount to transfer: "))
                if 0 < amount <= Accounts[ch]:
                    Accounts[ch] -= amount
                    Accounts[target] += amount
                    print(f"Transferred {amount} to account {target}. New Balance: {Accounts[ch]}")
                else:
                    print("Insufficient funds or invalid amount.")
            else:
                print("Recipient account not found or invalid.")
        elif choice == 5:
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice. Please try again.")





Accounts = {101: 10000, 102: 20000, 103: 30000}
while True:
    print("\nBANK MANAGEMENT SYSTEM")
    ch = int(input("Enter account number (0 to exit): "))
    if ch == 0:
        print("Exiting the system")
        break
    elif ch in Accounts:
        menu(Accounts, ch)
    else:
        print("Invalid account number.")



        accounts = {101: 1000,102: 2000,103: 3000}

def main(accounts, ch):
    while True:
        print("\n------ BANK MENU ------")
        print("1. CHECK BALANCE")
        print("2. DEPOSIT")
        print("3. WITHDRAW")
        print("4. TRANSFER ACCOUNT")
        print("5. LOG OUT")
        d = int(input("Enter your choice: "))
        
        if d == 1:
            print(f"Your current balance is ₹{accounts[ch]}")
            
        elif d == 2:
            amt = int(input("Enter amount to deposit: ₹"))
            if amt > 0:
                accounts[ch] += amt
                print(f"Deposited ₹{amt}. New balance: ₹{accounts[ch]}")
            else:
                print("Invalid amount.")
                
        elif d == 3:
            amt = int(input("Enter amount to withdraw: ₹"))
            if 0 < amt <= accounts[ch]:
                accounts[ch] -= amt
                print(f"Withdrew ₹{amt}. New balance: ₹{accounts[ch]}")
            else:
                print("Insufficient balance or invalid amount.")
        elif d == 4:
            target = int(input("Enter recipient account number: "))
            if target in accounts:
                amt = int(input("Enter amount to transfer: ₹"))
                if 0 < amt <= accounts[ch]:
                    accounts[ch] -= amt
                    accounts[target] += amt
                    print(f"Transferred ₹{amt} to account {target}. New balance: ₹{accounts[ch]}")
                else:
                    print("Insufficient balance or invalid amount.")
            else:
                print("Recipient account not found.")
        elif d == 5:
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

acc_no = int(input("Enter your account number: "))
if acc_no in accounts:
    main(accounts, acc_no)
else:
    print("Account not found.")