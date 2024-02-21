#ASSIGNMENT 8 ( Find words , lines , char , spaces )
# Name: Merwin Pinto
# SRN: 202100102
# Sr.No : 1
# Roll No: 0102
# DIV: E  
# Batch: B1
#date : 18-10-22

def function_option():
    while True:
         try:        
            option  = int(input("Please Enter option : "))
            print("\n")
            break

         except ValueError:
             print("ERROR : Please Enter Only integers !! \n")
    return option

def word_find():
    file = open('merwin.txt','r')
    read_data = file.read()
    word_data = read_data.split()
    words_total = len(word_data)
    print("\nThe total words in File = ",words_total)
    return words_total

def char_find():
        file = open('merwin.txt', 'r')
        char_total = 0
        read_data = file.read()
        for character in read_data:
            if character != ' ' and character != '\n':
                char_total += 1
        file.close()
        
        if char_total >= 1:
            print("\nTotal Characters in the File are :",char_total)

        else:
            print("\nThe File is empty!")

            
        return char_total    

def space_find():
        file = open('merwin.txt', 'r')
        space_total = 0

        for space in file.read():
            if space == ' ':
             space_total += 1
             file.close()

        if space_total >= 1:
            print("\nTotal Spaces in file are : ",space_total)

        else:
            print("\nNo Spaces in File")  
        
        return space_total


def line_find():
        file = open('merwin.txt', 'r')
        line_total = 0   #1 bcoz represent 1 line already 
        for line in file:
             if line != '\n':
                line_total += 1
        file.close()

        if line_total >= 1:
            print("\nTotal lines containing Text in file are = ",line_total)

        else:
            print("\nThe File is empty!")  
        
        return line_total

def all_find():
    words_total = word_find()
    char_total = char_find()
    space_total = space_find()
    line_total = line_find()
             

print("\n\nEnter the following option for particular tasks to get started \n\n")
while True:      #while loop
            print("\n\n----------------------------------------------\n\t\tM E N U\n----------------------------------------------")
            print("option 1 : To find no of words")
            print("option 2 : To find no of characters")
            print("option 3 : To find no of spaces")
            print("option 4 : To find no of lines")
            print("option 5 : To find all of the above options ")
            print("option 6 : To Exit code")

            option = function_option()

            if  option == 1: 
                    print("Displaying number of words in the File ")
                    word_find()
                    print("----------------------------------------------")
                
            elif option == 2:
                    print("Displaying number of characters in the File ")
                    char_find() 
                    print("----------------------------------------------")
                               
            elif option == 3:
                    print("Displaying number of spaces in the File ")
                    space_find()                                         
                    print("----------------------------------------------")

            elif option == 4:
                    print("Displaying number of lines in the File ")
                    line_find()
                    print("----------------------------------------------")
               
            elif option == 5:
                    print("Displaying number of words , characters , space and lines in the File ")
                    all_find()
                    print("----------------------------------------------")
            
            elif option == 6:
                    print("Code exited !")
                    break
   
            else:
                    print("Please enter a Valid option.")