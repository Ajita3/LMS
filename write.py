from tabulate import tabulate #importing table


#defining a function to read the data
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


# defining the function named "change_availability_status"
def change_availability_status(kitta_number, new_status):
    with open("land.txt", "r") as file:
        lines = file.readlines()

    updated_lines = [] #Creating a list

    for line in lines:
        data = line.strip().split(',')
        if data[0] == str(kitta_number):
            data[5] = new_status
        updated_lines.append(','.join(data) + '\n')

    with open("land.txt", "w") as file:
        file.writelines(updated_lines)

# Updating availability status of kitta_number 102
change_availability_status(102, "Available")

# adding the some other data in the preexisting data in the text file 
add_data1 = "104,Biratnagar,East,8,900000,Available\n"
add_data2 = "105,Bhaktapur,North,9,900000,Available\n"
add_data3 = "106,Dharan,West,10,900000,Available\n"

# Updating (writing in) the text file
with open("land.txt", "a") as file:
    file.write(add_data1)
    file.write(add_data2)
    file.write(add_data3)

# displaying the updating details
land_dictionary = land_details()
table_data = [["Kitta Number", "City/District", "Direction", "Anna", "Price", "Availability Status"]]
for kitta_number, details in land_dictionary.items():
    table_data.append([kitta_number] + details)

print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))





