adm_username="adm123"
adm_password="adm@123"
customer_data=[['79644', 'Vysakh', '7994634647', 'Vys7994', 'Vyga@123', []],['79647', 'Nihal', '7994654674', 'Nih7994', 'Nilu@123', []]]
books=[['100', 'Aadujeevitham', 'Bennyamin', '400'], ['101', 'Neelachadayan', 'Akhil', '250'],['102', 'Pathummante aadu', 'Vaikham Muhammed bhasheer', '300']]
while True:
    print("""1.Admin
2.User
3.Exit""")
    choice=int(input("Enter your choice :"))
    if choice==1:
        usrname=input("Enter Username :")
        pswd=input("Enter Password :")
        if usrname==adm_username and pswd==adm_password:
            print("!!! Welcome Sir !!!")
            while True:
                print("""1.Add book
2.Update book
3.Show all books
4.Delete book
5.Veiw Customers
6.Logout""")
                choice=int(input("Enter your choice pls :"))
                if choice==1:
                    b_no=input("Enter the number of the book :")
                    b_name=input("Enter the name of the book :")
                    b_author=input("Enter the name of the author of the book :")
                    b_price=input("Enter the price of the book :")
                    books.append([b_no,b_name,b_author,b_price])
                    print("Book added Successfully")
                elif choice==2:
                    while True:
                        print("You can ony update the number and Price of a book!!")
                        print('''1.Book Number
2.Book Price
3.Go back''')
                        choice=int(input("Enter the choice :"))
                        if choice==1:
                            book_no=input("Enter the number of the book u need to change :")
                            c=0
                            for book in books:
                                if book_no in book:
                                    print(book)
                                    print("Book found")
                                    nbook_no=input("Enter the new book number :")
                                    for book in books:
                                        if book_no in book[0]:
                                            book[0]=nbook_no
                                            print("Book number updated successfully")
                                            c=1
                            if c==0:
                                print("Invalid book number OR Book number already exist")
                        elif choice==2:
                            book_no=input("Enter the number of book which you need to change its price :")
                            c=0
                            for book in books:
                                if book_no in book:
                                    print(book)
                                    print("Book found")
                                    nbook_price=input("Enter the new book price :")
                                    book[3]=nbook_price
                                    print("Book price updated!!")
                                    c=1
                            if c==0:
                                print("Invalid book number!!")
                        elif choice==3:
                            break
                        else:
                            print("Invalid choice!!")
                elif choice==3:
                    for book in books:
                        print(book)
                elif choice==4:
                    book_no=input("Enter the number of book that u need to delete :")
                    c=0
                    for book in books:
                        if book_no in book[0]:
                            books.remove(book)
                            print("Book deleted Successfully")
                            c=1
                    if c==0:
                        print("Invalid book number!!")
                elif choice==5:
                    for customer in customer_data:
                       print( "{:<10}{:<10}{:<10}".format(customer[0],customer[1],customer[2]),customer[5])
                        # print(customer[0],customer[1],customer[2],customer[5])
                    if customer_data==[]:
                            print("No customers found!!")
                elif choice==6:
                    break
                else:
                    print("Invalid choice!!")
                        
        else:
            print("Invalid Username OR Password")


    elif choice==2:
        while True:
            print("""1.Register
2.Login
3.Exit""")
            choice=int(input("Enter your choice :"))
            if choice==1:
                cust_name=input("Enter Your name :")
                cust_ph=input("Enter your phone number :")
                cust_id=cust_ph[::2]
                n=cust_name[:3]
                ph=str(cust_ph)
                p=cust_ph[:4]
                cust_username=n+p
                cust_pswd=input("Enter password :")
                customer_data.append([cust_id,cust_name,cust_ph,cust_username,cust_pswd,[]])
                for cust in customer_data:
                    if cust_id in cust:
                        print(cust)
            elif choice==2:
                uname=input("Enter your Username :")
                upswd=input("Enter your password :")
                for cust in customer_data:
                    if uname==cust[3] and upswd==cust[4]:
                        print("Hi",cust[1])
                        while True:
                            print("""1.View book
2.Lend book
3.Return book
4.Books in hand
5.logout""")
                            choice=int(input("Enter your choice :"))
                            if choice==1:
                                print("Books")
                                for book in books:
                                    print(book)
                            elif choice==2:
                                book_no=input("Enter the number of book you need to find :")
                                c=0
                                for book in books:
                                    if book_no in book[0]:
                                        print("Book Found")
                                        print(book)
                                        for cust in customer_data:
                                            if uname==cust[3] and upswd==cust[4]:
                                                cust[5].append(book)
                                                print("Book added to your account Successfully!!")
                                        c=1
                                if c==0:
                                    print("Invalid book number !!")
                            elif choice==3:
                                for cust in customer_data:
                                    if uname==cust[3] and upswd==cust[4]:
                                        print(cust[5])
                                        book_no=input("Enter the number of book you need to return :")
                                        c=0
                                        for book in cust[5]:
                                            if book_no in book:
                                                cust[5].remove(book)
                                                print("Book returned Successfully")
                                                c=1
                                        if c==0:
                                            print("Invalid book number!!")
                            elif choice==4:
                                for cust in customer_data:
                                    if uname==cust[3] and upswd==cust[4]:
                                        print(cust[5])
                            elif choice==5:
                                break
                            else:
                                print("Invalid choice!!")


            elif choice==3:
                break
            else:
                print("Invalid choice!!")
            
        
    elif choice==3:
        break
    else:
        print("Invalid choice!!")