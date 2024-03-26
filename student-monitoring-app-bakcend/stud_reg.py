def student_registration(students):
    st_adm=input("Enter the admission number of student :")
    st_name=input("Enter name of student :")
    st_reg_no=input("Enter Register number of student :")
    st_class=input("Enter Class of student :")
    students.append({'adm_no':st_adm,'name':st_name,'reg_no':st_reg_no,'class':st_class})
def st_regs(std):
    std['phone']=input("Enter your phone number :")
    std['address']=input("Enter your Address :")
    std['B_group']=input("Enter your blood group :")



