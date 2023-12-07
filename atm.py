import random

balance = 1000 

while True:
    
    print("""
    Select Option From Below
    
    1. Check balance
    2. Withdraw money
    3. Deposit money
    4. Exit
    
    """)
    
    option = int(input("Choose an option: "))
    
    if option == 1:
        print(f"Your balance is ${balance}")
        
    elif option == 2:
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds")
        else:
            balance -= amount
            print(f"${amount} withdrawn. Current balance is ${balance}")
            
    elif option == 3:
        amount = int(input("Enter amount to deposit: "))         
        balance += amount
        print(f"${amount} deposited. Current balance is ${balance}")
        
    elif option == 4:
        print("Bye!") 
        break
    
    else:
        print("Invalid option. Please enter number between 1 to 4")