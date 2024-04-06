schools=[]
students=[]
teachers=[]
while True:
    print("""1.Add
2.Show""")
    choice1=int(input("Enter your choice :"))
    if choice1==1:
        print("""1.Schools
2.Teachers
3.Students""")
        choice=int(input("Enter your choice :"))
        class Schools:
                def __init__(self):
                    if choice==1:
                        school_name=input("Enter the name of school :")
                        school_location=input("Enter location of school :")
                        schools.append([school_name,school_location])
                    else:
                         print("Invalid choice :")
        class Teachers(Schools):
                def __init__(self):
                    if choice==2:
                        t_name=input("Enter name of the teacher :")
                        t_address=input("Enter the address of the teacher :")
                        t_email=input("Enter the email of teacher :")
                        t_phno=input("Enter the phone number of teacher :")
                        t_qual=input("Enter the qualification of teacher :")
                        teachers.append([t_name,t_address,t_email,t_phno,t_qual])
                    else:
                        super().__init__()
        class Students(Teachers):
                def __init__(self):
                    if choice==3:
                        st_name=input("Enter name of the student :")
                        st_address=input("Enter address of the student :")
                        st_email=input("Enter the email of the student :")
                        st_phno=input("Enter the phone number of the student :")
                        st_class=input("Enter the class of the student :")
                        students.append([st_name,st_address,st_email,st_phno,st_class])
                    else:
                        super().__init__()
obj=Students()        

                

