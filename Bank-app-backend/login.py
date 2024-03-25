def login(user_data):
    user_name=input("Enter Username :")
    password=input("Enter password :")
    c=0
    u=[]
    for user in user_data:
        if user_name in user and password==user[5]:
            print("Login Successfull")
            c=1
            u=user
            
    if c==0:
        print("Invalid password or Username")
    return c,u