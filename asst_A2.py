#ASSIGNMENT 2 ( Addition of array elements  ) ( sub done )
# Name: Merwin Pinto
# SRN: 202100102
# Sr.No : 1
# Roll No: 0102
# DIV: E  
# Batch: B1
#date : 13-9-22


print("Please Enter Only Numbers ( spaces between them !):")
array = [str(array) for array in input("Enter Numbers : ").split()]
print("Array Elements displaying are")
print(array)

summation=0
for i in range(len(array)):
    try:                                         #testing for error
        summation =  summation + int(array[i])
    except ValueError:
        if(array[i].isalpha()):
            i+=1
      
        print("\nAlphabet Found at Index : ",i-1)                            #solving error
        continue 
    print("\nNumber Found at Index : ",i)

print("\nAdding elements from array we get :",summation)
