#ASSIGNMENT 4 ( Matrix calculator for addition and multiplication  )
# Name: Merwin Pinto
# SRN: 202100102
# Sr.No : 1
# Roll No: 0102
# DIV: E  
# Batch: B1
#date : 25-10-22
def function_frequency():
    while True:
        try:        
            val  = int(input())
        except ValueError:
             print("Please enter a valid integer")
             continue
        if type(val) == int and val > 0:
            break
        else:
            print("WARNING : Please Enter Only integers !! \n")
    return val

def function_Matrix():
    while True:
         try:        
            Element  = int(input("Enter Element :"))
            print("\n")
            break

         except ValueError:
             print("WARNING : Please Enter Only integers !! \n")
    return Element

print("Matrix calculator for addition and multiplication \n")
print("Enter Matrix of order n  ")
n = function_frequency()

print("--------  MATRIX 1 DATA -------- \n")
print("Please Enter Row wise Elements \n")
matrix1 =[]
for i in range(n):       
    a1 =[]
    for j in range(n):      
            a1.append(function_Matrix())
    matrix1.append(a1)
        
print("\n\n--------  MATRIX 2 DATA -------- \n")
print("Please Enter Row wise Elements for Matrix 2 \n")
matrix2 =[]
for i in range(n):
    a2 =[]
    for j in range(n):    
             a2.append(function_Matrix())
    matrix2.append(a2)


print("\n ------------------------------------- \n")
print("\n\nDisplaying Matrix Data 1 \n")
for i in range(n):
    for j in range(n):
        print(matrix1[i][j],end = " ")
    print()

print("\n\nDisplaying Matrix Data 2 \n")
for i in range(n):
    for j in range(n):
        print(matrix2[i][j], end = " ")
    print()


# print('Matrix 1 :')
# for i in matrix1:
#     print(i)

# print('Matrix 2 :')
# for i in matrix2:
#     print(i)


while True:
    result = 0
    print("\nMATRICS OPERATION !\n")
    print("\n\nEnter The following option to perform the Matrices Operations !\n")
    print("Option 1 = Add Matrices \nOption 2 = Multiply Matrices \nOption 3 = Exit Code \n")
    print("Enter Option : ")
    option = function_frequency()
    if(option == 1):
        print("Performing Matrix addition \n")
        result = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):  
            for j in range(n):
                result[i][j] = matrix1[i][j] + matrix2[i][j]
        print("\n")
        for i in result:
            print(i)

    elif(option == 2):
        print("Performing Matrix Multiplication \n")
        print("Performing Matrix addition \n")
        result = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):  
            for j in range(n):
                for k in range(n):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
        print("\n")
        for i in result:
            print(i)

    elif(option == 3):
        print("Code exited !")
        break

    else:
        print("WARNING ! : Please Enter a Valid Option ! ")