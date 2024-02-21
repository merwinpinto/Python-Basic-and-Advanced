#ASSIGNMENT 6 ( Dictionary Merging ) ( sub done )
# Name: Merwin Pinto
# SRN: 202100102
# Sr.No : 1
# Roll No: 0102
# DIV: E  
# Batch: B1
#date : 11-10-22

def function_name():
    while True:
         try:        
            name  = input("Please Enter Employee name : ")
            print("\n")
            break

         except ValueError:
             print("ERROR : Please Enter Only name !! \n")       
    return name                        #for passing this value to another function we have to return this

def function_salary():
    while True:
         try:        
            salary  = int(input("Please Enter salary : "))
            print("\n")
            break

         except ValueError:
             print("ERROR : Please Enter Only integers !! \n")
    return salary

def function_count():
    while True:
         try:        
            count  = int(input())
            print("\n")
            break

         except ValueError:
             print("ERROR : Please Enter Only integers !! \n")
    return count


def func1():
    print("\nEnter data for dictionary 1 \n")
    print("Enter for how many Employees you need data : ")
    print("Please Enter Count : ")
    count = function_count()
    employee = {}    
    for i in range(count):
        name = function_name()
        salary = function_salary()
        employee[name] = salary      
    print(employee)
    print("------------------------------------------")
    return employee

def func2():
    print("\nEnter data for dictionary 2 \n")
    print("Enter for how many Employees you need data : ")
    print("Please Enter Count : ")
    count = function_count()
    employee2 = {}    
    for i in range(count):
     name = function_name()
     salary = function_salary()
     employee2[name] = salary      
    print(employee2) 
    print("------------------------------------------")
    print("------------------------------------------")
    return employee2  

def mergedict():
            dict1 = func1()
            dict2 = func2()
            for key, value in dict2.items():            #loop checks if keys and values if are overwriting in dict1
                if key in dict1:
                    dict1[key] = [value , dict1[key]]
                else:
                    dict1[key] = value
            return dict1

while True:
    print("-------------------------------------")
    print("Please Enter Respective options\n\nOption 1 : Dictionary Creating \nOption 2 : Exit Code")
    print("Please Enter Option : ")
    option = function_count()
    
    if option == 1:
        print("Entering Dictionary data \n")
        dict1 = mergedict()  
        print("\nThe dictionaries are merged \n",dict1)

    elif option == 2:
        print("Code exited !")  
        break
 







