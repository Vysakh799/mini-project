import sqlite3
con=sqlite3.connect("/home/synnefo/vysakh/mini-project/employe-management-system-backend/employee.db")
try:
    con.execute("create table employee(id int primary key,name text,email text,phno int,salary int,position text)")
except:
    pass
while True:
    print("""1.Add employee
2.View employee
3.Update employee
4.Delete employee
5.Exit""")
    choice=int(input("Enter your choice :"))
    if choice==1:
        name=input("Enter the name of the employee :")
        email=input("Enter the email of the employee :")
        phno=input("Enter the phno of the employee :")
        salary=input("Enter the salary of the employee :")
        pos=input("Enter the position of the employee :")
        data=con.execute("select max(id) from employee")
        for i in data:
            if i[0]==None:
                id_no=1
            else:
                id_no=i[0]+1
        con.execute("insert into employee values(?,?,?,?,?,?)",(id_no,name.upper(),email,phno,salary,pos))
        con.commit()
    elif choice==2:
        while True:
            print("""1.View all
2.Search
3.Exit""")
            choice=int(input("Enter your choice :"))
            if choice==1:
                print("{:<20}{:<20}{:<30}{:<20}{:<20}{:<20}".format("id_no","Name","email","phno","Salary","Position"))
                data=con.execute("select*from employee")
                for i in data:
                    print("{:<20}{:<20}{:<30}{:<20}{:<20}{:<20}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
            elif choice==2:
                name=input("Enter the name of the employee you need to search :")
                print("{:<20}{:<20}{:<30}{:<20}{:<20}{:<20}".format("id_no","Name","email","phno","Salary","Position"))
                data=con.execute("select*from employee where name=?",(name.upper(),))
                for i in data:
                    print("{:<20}{:<20}{:<30}{:<20}{:<20}{:<20}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
            elif choice==3:
                break
            else:
                print("Invalid choice")
    elif choice==3:
        id_no=input("Enter the id_no of the employee you need to find :")
        data=con.execute("select* from employee where id=?",(id_no,))
        c=0
        for i in data:
            print("{:<20}{:<20}{:<30}{:<20}{:<20}{:<20}".format("id_no","Name","email","phno","Salary","Position"))
            print("{:<20}{:<20}{:<30}{:<20}{:<20}{:<20}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
            c=1
        if c==0:
            print("Employee not found")
        else:
            while True:
                print("""1.Update Position
2.Update Salary
3.Update email
4.Update phno
5.Exit""")
                choice=int(input("Enter your choice :"))
                if choice==1:
                    f='position'
                    a=input("Enter the new position of the employee :")
                    # con.execute("update employee set position=? where id=?",(pos,id_no))
                    # con.commit()
                    print("Position updated successfully")
                elif choice==2:
                    f='salary'
                    a=input("Enter the new salary of the employee :")
                    # con.execute("update employee set salary=? where id=?",(sal,id_no))
                    # con.commit()
                    print("Salary updated successfully")
                elif choice==3:
                    f='email'
                    a=input("Enter the new email of the employee :")
                    # con.execute("update employee set email=? where id=?",(email,id_no))
                    # con.commit()
                    print("Email updated successfully")
                elif choice==4:
                    f='phno'
                    a=input("Enter the new phno of the employee :")
                    # con.execute("update employee set phno=? where id=?",(phno,id_no))
                    # con.commit()
                    print("Phno updated successfully")
                elif choice==5:
                    break
                else:
                    print("Invalid choice")
                try:
                    qry="update employee set {}=? where id=?".format(f)
                    con.execute(qry,(a,id_no))
                    con.commit()
                except:
                    pass
    elif choice==4:
        id_no=input("Enter the id of the employee you need to delete :")
        data=con.execute("select* from employee where id=?",(id_no,))
        c=0
        for i in data:
            print("{:<20}{:<20}{:<30}{:<20}{:<20}{:<20}".format("id_no","Name","email","phno","Salary","Position"))
            print("{:<20}{:<20}{:<30}{:<20}{:<20}{:<20}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
            c=1
        if c==0:
            print("Employee not found")
        else:
            con.execute("delete from employee where id=?",(id_no,))
            con.commit()
            print("Employee deleted succsessfully")
    elif choice==5:
        break
    else:
        print("Invalid choice")
        

                    

