#ASSIGNMENT 11 ( NUMPY )
# Name: Merwin Pinto
# SRN: 202100102
# Sr.No : 1
# Roll No: 0102
# DIV: E  
# Batch: B1
#date : 11 -11-22

import numpy as np
Datalist = []

def function1_data():
    while True:
        try:
            val = int(input())
            print("\n")
            break

        except ValueError:
         print("Enter integers only !")

         if type(val) == int and val < 0:
                print("Enter Positive Interger")
    return val

def function1_data():
    while True:
        try:        
            data  = int(input())
            print("\n")
        
            if data <= 0 or data >101  :
                print("Enter Positive Number less than 100 or equal to 100 :")
                data = function1_data()
                break

            break
        except ValueError:
             print("\nERROR : Please Enter Only integers +ve numbers less than 100 !! \n")
    return data

def function_data():
        print("option 1 : to Display array ")
        print("option 2 : to find Max element from array ")
        print("option 3 : to find Min element from array ")
        print("option 4 : to find Mean of array ")
        print("option 5 : to find Variance of array ")
        print("option 6 : to find product of array ")
        print("option 7 : to find Sum of array ")
        print("option 8 : to find Square root of array ")
        print("option 9 : to Unique elements of array ")
        print("option 10: Exit code ")

print("PLEASE ENTER POSITIVE NUMBERS  ( <= 100 ) \n")
print("Enter count : ")
count = function1_data()

for i in range(count):
    print("\nElement : ",i+1)
    array = function1_data()
    Datalist.append(array)

# Datalist =[1,2,3,4,5]

#Using numpy here
x1 = np.array(Datalist)
x2 = np.prod(Datalist)
x3 = np.sqrt(Datalist)
x4 = np.unique(Datalist)

print("\n\nEnter the following option for particular tasks to get started \n\n")
print("\n\n----------------------------------------------\n\t\tM E N U\n----------------------------------------------")
function_data()

while True:
            print("Enter option  : ") 
            option = function1_data()
            if option == 1:
                print("Array Displaying is : ",Datalist) 
                print("----------------------------------------------\n")

            if option == 2:
                print("Max element from array is : ",x1.max()) 
                print("----------------------------------------------\n")
               
            elif option == 3:
                print("Min element from array is : ",x1.min())           
                print("----------------------------------------------\n")
            
            elif option == 4:
                print("Mean of array is : ",x1.mean())           
                print("----------------------------------------------\n")

            elif option == 5:
                print("variance of array is : ",x1.var())           
                print("----------------------------------------------\n")

            elif option == 6:
                print("Product of array is : ",x2)
                print("----------------------------------------------\n")

            elif option == 7:
                print("Sum of Whole array is : ",x1.sum())
                print("----------------------------------------------\n")

            elif option == 8:
                print("Square root of array is : ",x3)
                print("----------------------------------------------\n")

            elif option == 9:
                print("Unique elements of array : ",x4)
                print("----------------------------------------------\n")

            elif option == 10:
                print("Code exited !")
                break 

            else:
                print("Please enter a Valid option.")