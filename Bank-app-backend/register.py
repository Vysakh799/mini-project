def register(user_data):
        name=input("Enter Your name :")
        age=input("Enter your age :")
        phno=int(input("Enter your Phone number :"))
        minbal=int(input("Enter the minimum balance that you can keep in your account :"))
        n=name[:3]
        ph=str(phno)
        p=ph[:4]
        user_name=n+p
        password=input("Enter your password :")
        user_data.append([name,age,phno,minbal,user_name,password])
        print("User name :",user_name,"\nPassword :",password)