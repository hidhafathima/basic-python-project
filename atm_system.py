print("Welcome to simple ATM System")
balance=1000
while True:
        print("\nPlease choose an option:")
        print("1.Check Balance")
        print("2.Deposit Money")
        print("3.Withdraw Money")
        print("4.Exit")
        choice=input("Enter your choice (1-4): ")
        if choice=="1":
            print("Your Current balance is :",balance)
        elif choice=="2":
            deposit=float(input("Enter the amount to deposit"))
            balance+=deposit
            print("Deposit Successful")
            print("Updated balance:",balance)
        elif choice=="3":
            withdraw=float(input("Enter the amount to withdraw"))
            if withdraw<=balance:
                balance-=withdraw
                print("Please collect your cash")
                print("remaining balance:",balance)
            else:
                print("Insufficient Balance")
        elif choice=="4":
            print("Thank You for using the ATM:Goodbye!")
            break
        else:
            print("Inavalid choice.Please try again.")