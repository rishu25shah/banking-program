def show_balance(balance):
    print("*******************************")
    print(f"YOUR BALANCE IS:${balance:.2f}")
    print("*******************************")

def deposit():
    print("*******************************")
    amount=float(input("ENTER THE AMOUNT TO DEPOSIT:"))
    print("*******************************")
    if amount <=0:
        print("*******************************")
        print("   THAT NOT A VALID AMOUNT!")
        print("*******************************")
        return 0
    else:
        return amount

def withdraw(balance):
    print("*******************************")
    amount=float(input("ENTER THE AMOUNT TO WITHDRAW:"))
    print("*******************************")
    if balance < amount:
        print("*******************************")
        print("      INSUFFICIENT FUNDS!")
        print("*******************************")
        return 0
    elif amount <= 0:
        print("*******************************")
        print("AMOUNT MUST BE GREATER THAN 0!")
        print("*******************************")
        return 0
    else:
        return amount
def main():
    balance=0
    is_running=True

    while is_running:
        print("***************************")
        print("     BANKING PROGRAM       ")
        print("***************************")
        print("1.SHOW BALANCE")
        print("2.DEPOSIT")
        print("3.WITHDRAW")
        print("4.EXIT")

        choice=int(input("Enter your choice (1-4):"))

        match choice:
            case 1:
                show_balance(balance)
            case 2:
                balance+=deposit()
            case 3:
                balance-=withdraw(balance)
            case 4:
                is_running=False
            case _:
                print("***************************")
                print("     INVALID CHOICE!       ")
                print("***************************")
    print("**************************")
    print("THANK YOU! HAVE A NICE DAY")
    print("**************************")

if __name__=="__main__":
    main()
