def deposit(user):
    amount=int(input("Enter the amount you need to Deposit :"))
    user[3]+=amount
    print("Amount deposited Successfully")
def withdraw(user):
    amount=int(input("Enter the amount you need to Withdraw :"))
    if amount<user[3]:
        user[3]-=amount
        print("Withdrawel Successfull")
    else:
        print("Insufficient balance")
def balance(user):
    print("Balance :",user[3])