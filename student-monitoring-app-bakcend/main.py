from login import login
from stud_reg import *
from find import *
from stud import stud


students=[{'adm_no': '100', 'name': 'Vysakh', 'reg_no': '20132000', 'class': 'Cs2'},
          {'adm_no': '101', 'name': 'Athul', 'reg_no': '20132001', 'class': 'Cs2'},
          {'adm_no': '102', 'name': 'Nihal', 'reg_no': '20132002', 'class': 'Cs3'}]
while True:
    print("""1.Login
2.Exit""")
    choice=int(input("Enter your choice :"))
    if choice==1:
        log,std=login(students)
        if log==1:
            while True:
                print("""1.Add students
2.View students based on class
3.Update attendace
4.logout""")
                choice=int(input("Enter your choice :"))
                if choice==1:
                    student_registration(students)
                elif choice==2:
                    find_st(students)
                elif choice==3:
                    find_st(students)
                    update_att(students)
                elif choice==4:
                    break
                else:
                    print("Invalid choice")
        elif log==2:
            while True:
                length=len(std)
                if length<=5:
                    st_regs(std)
                else:
                    stud(std)
                    find_st(students,std,True)
                    break
    elif choice==2:
        break
    else:
        print("Invalid choice ")
