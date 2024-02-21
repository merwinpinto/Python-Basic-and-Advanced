#ASSIGNMENT 3 ( Swapping List elements ) ( sub done )
# Name: Merwin Pinto
# SRN: 202100102
# Sr.No : 1
# Roll No: 0102
# DIV: E  
# Batch: B1
#date : 20-9-22

list = []
print("Please Enter ( more than one ) Element \n")

while True:
    try:        
        array_element = input("Enter a list of elements (Enter spaces between them ) \n Element = ")
        list = array_element.split()
        print("\n")
        break

    except ValueError:
        print("ERROR : Non Integers not Allowed ! Please re-enter correct index Number\n")

print("element Elements displaying are \n")
print(list)
size = len(list)
print("The length of the Array is : ",size)

print("\nEnter which Element you would like to swap with \n")

while True:
    try:        
        i = int(input("\nEnter index of element for swapping other element \nElement 1 : "))
        print("\n")
        assert size * -1 <= i < size

    except ValueError:
        print("ERROR : Non Integers not Allowed ! Please re-enter correct index Number\n")

    except AssertionError:
        print("ERROR : Please enter only indexe's Suitable in List")
    else:
        break

while True: #loop until the user enters a valid int
    try:        
        j = int(input("Enter index of element for swapping Element 1 \nElement 2 : "))
        print("\n")
        assert size * -1 <= j < size 
        
    except ValueError:
        print("ERROR : Non Integers not Allowed ! Please re-enter correct index Number\n")

    except AssertionError:
        print("ERROR : Please enter only indexe's Suitable in List")

    else:
        break

print("The List before swapping is : ",list)
print("\nSwapped Elements List updated !:\n\nThe List After swapping is :")
list[i], list[j] = list[j], list[i]
print("The Swapped list is : ",list)