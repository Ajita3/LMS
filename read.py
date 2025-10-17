#welcome message
def messages():
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("Hello and welcome to land management system")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("The Elucidation for using this system is, you have to follow the messages provided below such as (Enter '1' to Rent Land)")
    print("++++++++++++++++++++++++++++++++++++++++++++")

    
messages()






#Reading a file named "land.txt" where the information of land is stored

def read_file():
    file = open ("land.txt" , "r")
    print(file.read())
    print( "\n" )
    file.close()
read_file() #Triggering the function

from tabulate import tabulate #Importing table


def land_details():
    file = open("land.txt", "r")
    data = {}  # Creating a dictionary to store the data of the txt file
    i = 1
    
    for line in file:
        line = line.strip() 
        if line:  # Checking if the line is not empty
            line = line.split(",")
            data[i] = line
            i += 1
            print(line)
    
    file.close()
    return data


# Triggering the functions
land_dictionary = land_details()
print(land_dictionary)

# Displaying the land details in tabular format
table_data = [[ "Land ID" , "Kitta Number", "City/District", "Direction", "Anna", "Price", "Availability Status"]]
for kitta_number, details in land_dictionary.items(): # Using key, value pair
    table_data.append([kitta_number] + details)

print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))

def validate():
    # Executing a while loop 
  continuation=True

  while continuation==True:
#Messages to be displayed so that user can choose one 
    print("Enter '1' to Rent Land")
    print("Enter '2' to Return land")
    print("Enter '3' to exit")
#Asking user for a input 
    value=int(input("Please enter a value: "))

# Executing if/else statements
#If user enters '3' the print statements are displayed
    if value==3:
        print("++++++++++++++++++++++++++++++++++++++++++++")
        print("Thank you for using our land management system")
        print("++++++++++++++++++++++++++++++++++++++++++++")
#If user enters 1 , the renting procedure starts
    elif value==1:
        print("You will now rent the land")
        
        
#Asking user for a input        
        kitta_number = int(input("Enter kitta number of the land you want to borrow: "))

#If kitta number are 101 or 103 , print statements are displayed
        if kitta_number==101 or kitta_number==103:
            print("kitta number is " , kitta_number)
            print("++++++++++++++++++++++++++++++++++++++++++++")
            print("Land is available")
            print("++++++++++++++++++++++++++++++++++++++++++++")
            print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))
            print(land_dictionary)
            print("Enter '1' to Rent Land")
            print("Enter '2' to Return land")
            print("Enter '3' to exit")
            value=int(input("Please enter a value: "))


   



          
#If kitta number is 102, the print statement are displayed            
        elif kitta_number==102:
           
            print("kitta number is " , kitta_number)
            print("++++++++++++++++++++++++++++++++++++++++++++")
            print("Land is not available")
            print("++++++++++++++++++++++++++++++++++++++++++++")
            print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))
            print(land_dictionary)
            print("Enter '1' to Rent Land")
            print("Enter '2' to Return land")
            print("Enter '3' to exit")
            value=int(input("Please enter a value: "))


            
#If user enters a kitta number which is not included in the data the else statement is executed 
        else:
             print("++++++++++++++++++++++++++++++++++++++++++++")
             print("Please provide a valid kitta number")
             print("++++++++++++++++++++++++++++++++++++++++++++")
             print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))
             print(land_dictionary)
             print("Enter '1' to Rent Land")
             print("Enter '2' to Return land")
             print("Enter '3' to exit")
             value=int(input("Please enter a value: "))


            
            
        
            
#If user enters 2 , the returning procedure starts  
    elif value==2:
    
        print("You will now return the land")


     

    else:
        print("++++++++++++++++++++++++++++++++++++++++++++")
        print("Invalid input!!")
        print("Please provide value as 1, 2 or 3")
        print("++++++++++++++++++++++++++++++++++++++++++++")
        print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))
        print(land_dictionary)
        print("Enter '1' to Rent Land")
        print("Enter '2' to Return land")
        print("Enter '3' to exit")
        value=int(input("Please enter a value: "))
      



      

