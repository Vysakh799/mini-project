lawyers=[]
customers=[]
while True:
    print("""1.Lawyer
2.Customer
3.View all Lawyers
4.Exit""")
    choice=int(input("Enter your choice :"))
    if choice==1:
        while True:
            print("""1.Register
2.Login
3.Exit""")
            choice=int(input("Enter your choice :"))
            if choice==1:
                l_name=input("Enter your name :")
                l_phno=input("Enter your phno :")
                l_id=l_phno[::5]
                l_address=input("Enter your address :")
                l_experience=input("Enter your experince :")
                l_fc_area=input("Enter your focus area :")
                l_location=input("Enter your location :")
                p=l_phno[:4]
                u=l_name[:3]
                l_username=p+u
                l_password=input("Enter your password :")
                lawyers.append([l_id,l_name,l_phno,l_address,l_experience,l_fc_area,l_location,l_username,l_password])
                print("Username :",l_username)
                print("Password :",l_password)
            elif choice==2:
                username=input("Enter your username :")
                password=input("Enter your password :")
                while True:
                    if username==l_username and password==l_password:
                        print("""1.Case details
2.Customer
3.Case updates
4.Exit""")
                        choice==int(input("Enter your choice :"))
                        # if choice==1:
                        if choice==3:
                            for customer in customers:
                                print

                    else:
                        print("Invalid username OR password")
            elif choice==4:
                break
    elif choice==2:
        while True:
            print("""1.Register
2.Login
3.Exit""")
            choice==int(input("Enter your choice :"))
            while True:
                if choice==1:
                    
    elif choice==4:
        break

