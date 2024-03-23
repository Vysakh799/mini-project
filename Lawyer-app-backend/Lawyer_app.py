lawyers=[['79644', 'Vysakh', '7994634647', 'Vysakham,Poovannur palli', '3 years', 'Criminal case', 'Calicut', 'Vys7994', 'Vyga@123'],
         ['79655', 'Nihal', '7994634648', 'Nakkotil house ,Aikkarappadi', '4 years', 'Petti case', 'Malappuram', 'Nih7994', 'Nilu@123'],
         ['79666', 'Amal', '7945673475', 'Amaloski villa ,Farook college', '2 years', 'Any case', 'Calicut', 'Ama7945', 'Amal@123']]
customers=[['87564', 'Salman', '8756457384', 'PPMS Villa', 'Adhaar', 'Sal8756', 'Salu@123',[],{}],
           ['74567', 'Muneeb', '7456743798', 'Sabisthan house', 'Adhaar', 'Mun7456', 'Munu@123',[],{}]]
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
                l_id=l_phno[::2]
                l_address=input("Enter your address :")
                l_experience=input("Enter your experince :")
                l_fc_area=input("Enter your focus area :")
                l_location=input("Enter your location :")
                p=l_phno[:4]
                u=l_name[:3]
                l_username=u+p
                l_password=input("Enter your password :")
                lawyers.append([l_id,l_name,l_phno,l_address,l_experience,l_fc_area,l_location,l_username,l_password])
                print("Username :",l_username)
                print("Password :",l_password)
            elif choice==2:
                username=input("Enter your username :")
                password=input("Enter your password :")
                while True:
                    for lawyer in lawyers:
                        if username==lawyer[-2] and password==lawyer[-1]:
                            print("""1.Customer
2.Case Details
3.Case updates
4.Exit""")
                            choice=int(input("Enter your choice :"))
                            # if choice==1:
                                # for customer in customers:
                                #     for i in customer:


            elif choice==3:
                break
    elif choice==2:
        while True:
            print("""1.Register
2.Login
3.Exit""")
            choice=int(input("Enter your choice :"))
            if choice==1:
                    c_name=input("Enter your name :")
                    c_phno=input("Enter your phone number :")
                    c_id=c_phno[:5]
                    c_address=input("Enter your address :")
                    c_idproof=input("Submit your any id proof :")
                    p=c_phno[:4]
                    u=c_name[:3]
                    c_username=u+p
                    c_password=input("Enter your password :")
                    customers.append([c_id,c_name,c_phno,c_address,c_idproof,c_username,c_password,[],{}])
                    print("Username :",c_username)
                    print("Password :",c_password)
                    for customer in customers:
                        print(customer)
            elif choice==2:
                    username=input("Enter your username :")
                    password=input("Enter your password :")
                    for customer in customers:
                        if username==customer[5] and password==customer[6]:
                            print("Hi",customer[1])
                            while True:
                                print("""1.Find lawyers
2.Case details
3.Case updates
4.Exit""")
                                choice=int(input("Enter your choice :"))
                                if choice==1:
                                    location=input("Enter the location which u need to find lawyer :")
                                    c=0
                                    for lawyer in lawyers:
                                        if location==lawyer[6]:
                                            print("ID :",lawyer[0],"|",lawyer[1],"|",lawyer[2],"|",lawyer[3],"|",lawyer[4],"of experience","|",lawyer[5])
                                            c=1
                                    id=int(input("Enter the id of Lawyer you need to choose :"))
                                    for customer in customers:
                                        if username==customer[5] and password==customer[6]:
                                            customer[7].append(id)
                                            print("Lawyer added successfully")
                                    if c==0:
                                         print("Invalid Location")
                                elif choice==2:
                                    case_details=input("Enter case details :")
                                    for customer in customers:
                                        if username==customer[5] and password==customer[6]:
                                            customer[8].update({'Case_details':case_details})
                                            print("Case details added Successfully")
                                elif choice==3:
                                    for customer in customers:
                                        if username==customer[5] and password==customer[6]:
                                            print(customer)
                                elif choice==4:
                                     break
            elif choice==3:
                    break
    elif choice==4:
        break

