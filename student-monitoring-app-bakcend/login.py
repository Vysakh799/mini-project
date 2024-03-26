def login(students):
    username=input("Enter Username :")
    password=input("Enter password :")
    log=0
    std={}
    if "adm123"==username and "adm@123"==password:
        print("Welcome SIR")
        log=1
    else:
        for student in students:
            if username==student['name'] and password==student['adm_no']:
                print("Welcome",student['name'])
                log=2
                std=student
    return log,std
