from register import register
from login import login
from bank_functions import *

user_data=[['Vysakh', '76', 7994634647, 2000, 'Vys7994', 'Vyga@123']]
while True:
    print("""1.Register
2.Login
3.Exit""")
    choice=int(input("Enter your choice :"))
    if choice==1:
        register(user_data)
        print(user_data)
    elif choice==2:
        c,user=login(user_data)
        if c==1: 
            while True:
                    print('''
1.Deposit
2.Withdraw
3.Balance Enquiry
4.logout''')
                    choice=int(input("Enter your choice :"))
                    if choice==1:
                        deposit(user)
                    elif choice==2:
                        withdraw(user)
                    elif choice==3:
                        balance(user)
                    elif choice==4:
                        break
                    else:
                        print("Invalid choice")
    elif choice==3:
        break
    else:
        print("Invlaid choice")





