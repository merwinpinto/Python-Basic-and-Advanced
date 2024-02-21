import re
def function1_data():
    while True:
        try:
            n = int(input("Enter a number  : "))
        except ValueError:
         print("Please enter a integers only !")

        continue
        if type(n) == int and n > 0:
            break
        else:
            print("enter a proper number : ")


def function2_data():
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

#for input of words only !

def function3_data():
    while True:
        data = input( "Enter Name : ")
        
        if not re.match(r"^[a-zA-Z\s]+$",data):
            print("\nEnter only letters\n")
            continue
        else:
            print(data)
        break

    return data


      
