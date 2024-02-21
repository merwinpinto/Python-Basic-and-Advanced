#ASSIGNMENT 7 ( The Minimum and maximum K elemets in the tuple )
# Name: Merwin Pinto
# SRN: 202100102
# Sr.No : 1
# Roll No: 0102
# DIV: E  
# Batch: B1
#date : 26-10-22

def function_value():
    while True:
         try:        
            value  = int(input(""))
            print("\n")
            break

         except ValueError:
             print("WARNING : Please Enter Only integers !! \n")
    return value

def function_tuple():
    while True:
         try:        
            tuple_var  = tuple(int(tuple_var) for tuple_var in input("Enter space between each element : ").split())
            print("\n")
            break

         except ValueError:
             print("WARNING : Please Enter Only integers type elements  !! \n")
    return tuple_var

def function_find(tuple_var,k):
    tuple_var = tuple(tuple_var)
    x = len(tuple_var)
    for i in range(x):
        for j in range(i+1,x):
            if tuple_var[i] > tuple_var[j]:
                tuple_var[i],tuple_var[j] = tuple_var[j],tuple_var[i]
    print(tuple_var)
    test = tuple_var
    result = tuple(test[:k] + test[-k:])
    return result

while True:
    print("Enter 1 =  to Start.\nEnter 2 = to Exit.\n")
    print("option : ")
    option = function_value()

    if(option == 1):
        print("Tuple Value entry ! \n")
        tuple_var = function_tuple()

        print("Tuple displaying is :\n", tuple_var)

        print("\nPlease Enter K element : \n")
        k = function_value()

        result = function_find(tuple_var,k)
        print("The Minimum and maximum K elemets in the tuple are : ",result)
        print("\n---------------------------------------------\n\n")

    elif(option == 2):
        print("Code exited !")
        break

    else:
        print("Please enter Valid option !")
