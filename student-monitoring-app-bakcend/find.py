def find_st(students,std=False,stds=False):
    if std:
        st_class=std['class']
    else:
        st_class=input("Enter the class of student")
    for student in students:
        if st_class==student['class']:
            if stds:
                if 'phone' in student:
                    print(student['name'],student['phone'])
                else:
                    print(student['name'])
            else:
                print(student)
def update_att(students):
    adm_no=input("Enter the adm.no of the student :")
    c=0
    for student in students:
        if adm_no==student['adm_no']:
            n_att=input("Enter the new attendance :")
            student.update({'attendace':n_att})
            c=1
    if c==0:
        print("Invalid admission number :")
