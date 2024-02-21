#ASSIGNMENT 5 ( String manupulation ) ( sub done )
# Name: Merwin Pinto
# SRN: 202100102
# Sr.No : 1
# Roll No: 0102
# DIV: E  
# Batch: B1
#Date : 6 - 10 - 22

def function_text():
    while True:
         try:        
            text  = input("Please Enter your Text 1 Line : ")
            print("\n")
            break

         except ValueError:
             print("ERROR : Please Enter Only Text !! \n")
            

    return text                        #for passing this value to another function we have to return this

def function_text2():
    while True:
         try:        
            text2  = input("Please Enter your Text 2 Line : ")
            print("\n")
            break

         except ValueError:
             print("ERROR : Please Enter Only Text !! \n")
            

    return text2

def string_copy():
    
    text = function_text()
    print("The Text is : ",text)
    length = len(text)
    print("The String length is : ",length)
    storage1 = text
    storage2 = storage1
    print("String copied to list 2 is : ",storage2)

    
def string_concat():
    text = function_text()
    text2 = function_text2()
    print("The Text 1 is : ",text)
    print("The Text 2 is : ",text2)
    # text3 = text.capitalize() +" "+ text2.capitalize()
    
    #algo for concating string
    text3 = text+""+text2
    print("String concated is : ",text3)
        

def string_reverse():
    text = function_text()
    print("The Text is : ",text)
    length = len(text)
    print("The String length is : ",length)
    print("\nPerforming String reverse \n")
    
    #algo for reversing string
    str=""
    for i in text:
        str = i + str
    print("\nReversed string : ",str)

def string_compare():
    text = function_text()
    text2 = function_text2()
    print("The Text 1 is : ",text)
    print("The Text 2 is : ",text2)

    #algo for comparing string
    if text == text2:
     print("\nBoth texts are same !\n")

    else:
     print("\nBoth strings different\n")    
    
print("\nPYTHON PROGRAMMED STRING MANUPULATOR ! \n")
print("\n--------------------------------\n\t * MENU * \n--------------------------------\n")
print("\nchoice 1 : Perform string copy.     \n\nchoice 2 : Perform String concat.  ")
print("\nchoice 3 : Perform string reverse . \n\nchoice 4 : Perform string compare \n\nchoice 5 : Code Exit \n")

while True:
    try: 
         print("\n---------------------------------------------\n")       
         option  = int(input("Enter Which choice you would like to perform :  "))
         print("\n---------------------------------------------\n")
        
    except ValueError:
                print("ERROR : choice not recognized  ! Please re-enter correct choice\n")
                continue         

    choice = option             

    if choice == 1:
                print("Performing String Copy\n")
                string_copy()
                             

    elif choice == 2:
                print("Performing String Concatenation !\n  ") 
                string_concat()     

    elif choice == 3:
                print("Performing String Reverse !\n  ")
                string_reverse()    

    elif choice == 4:
                print("Performing String Compare !\n  ")
                string_compare()  

    elif choice == 5:
                print("Code exited \n") 
                break

    else :
        print("choice not recognized ! \nPlease re-enter correct choice\n")
