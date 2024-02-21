import re
#ASSIGNMENT 9 ( Create Employee Class and objects and display data )
# Name: Merwin Pinto
# SRN: 202100102
# Sr.No : 1
# Roll No: 0102
# DIV: E  
# Batch: B1
#date : 2-11-22

def function_data():
    while True:
        try:        
            data  = int(input())
            print("\n")
        
            if data <= 0 or data > 80 :
                print("Enter Positive Number less than 80 :")
                data = function_data()
                break

            break
        except ValueError:
             print("\nERROR : Please Enter Only integers +ve numbers less than 80 !! \n")
    return data

def function2_data():
    while True:
        data = input( "Enter Name : ")
        
        if not re.match(r"^[a-zA-Z\s]+$",data):
            print("\nEnter only letters\n")
            continue
        else:
            print(data)
        break

    return data

    

class Employee:
        Count = 0

        def __init__(self):
            self.Name = function2_data()

            print("\nEnter Age :")
            self.Age = function_data()
            print(f"Age : {self.Age} Years ")

            print("\nEnter Experience ( in years ) :")
            self.Experience = function_data()
            print(f"Experience : {self.Experience} Years ")

            print("\nEnter Salary in K ( thousands ) ):")
            self.Salary = function_data()
            print(f"Salary : {self.Salary} K ")
            
            Employee.Count += 1
           

        def display(self):
                print(self.Name,end = '\t\t')
                print(f"{self.Age} Yr",end  = '\t\t\t')
                print(f"{self.Experience} Yr",end = '\t\t\t')
                print(f"{self.Salary} K",end = '\t\t')
while True:
    print("Enter 1 =  to Start.\nEnter 2 = to Exit.\n")
    print("option : ")
    option = function_data()
    
    if option == 1:
        st = []
        print("PLEASE ENTER POSITIVE NUMBERS LESS THAN 80 \n")
        print("For how many Employee data would you like to Enter  \n")
        print("Count : ")
        n = function_data()

        print("EMPLOYEE DATA  \n")
        print("NOTE : (Srno,Age,Salary,Experience) in  integer type values only ! \n")

        for i in range(n):
            print("Employee : ",i+1)
            st.append(Employee())

        print("\n\nDisplaying Employee Information\n")
        print("-------------------------------------------------------------------------------------\n")
        print("NAME\t\tAGE(Years)\t\tEXPERIENCE(Years)\t\tSALARY(in K)")
        print("--------------------------------------------------------------------------------------\n")
        for i in range(n):
            st[i].display() 
            print("\n\n\n")

    elif(option == 2):
        print("Code exited !")
        break

    else:
        print("Please enter Valid option !")