#ASSIGNMENT 1  ( Calculator ) ( sub done )
# Name: Merwin Pinto
# SRN: 202100102
# Sr.No : 1
# Roll No: 0102
# DIV: E  
# Batch: B1

def function_option():
    while True:
         try:        
            option  = int(input ("Enter Option : "))
            print("\n")
            break

         except ValueError:
             print("WARNING : Please Enter Only integers !! \n")
    return option

def multioperation():     #Function
                        input_string = input("Enter an expression : ")
                        result = 0
                        counter = -1
                        for num in range(len(input_string)):   #for loop
                            if counter == num:
                                continue

                            if input_string[num] in ['-', '+', '/', '*']:
                                
                                next_option = float(input_string[num+1])
                                
                                if input_string[num] == '-':
                                    result -= next_option
                                    counter = num+1
                                
                                elif input_string[num] == '+':
                                    result += next_option
                                    counter = num+1
                                
                                elif input_string[num] == '*':
                                    result *= next_option
                                    counter = num+1
                                
                                elif input_string[num] == '/':
                                    result /= next_option
                                    counter = num+1
                            else:
                                result = float(input_string[num])
                        
                        print(result)


print("Welcome to Python Programmed Basic Calculator ")

while True:      #while loop
            print(" \n Enter the following option for particular operation to get started ")
            print("option 1 : Multioperation")
            print("option 2 : Exit code ")
            option = function_option()
                                                 
             #if else statements
            if option == 1:
                           multioperation()   

            elif option == 2:
                             print("Code exited !")
                             break

            else:
                print("\n.\n.\n  Code exited ! || Please enter a Valid option ")
                break


