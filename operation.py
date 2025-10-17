#importing datetime and table 
import datetime
from tabulate import tabulate
#defining a function named "read_land_details"
def read_land_details():
    land_details = {}
    with open("land.txt", "r") as file:
        for line in file:
            line = line.strip().split(",")
            land_details[line[0]] = line[1:]
    return land_details
# defining a function to store the data in tabular format
def update_table(land_details, land_availability):
    table_data = [["Kitta Number", "Location", "Direction", "Anna", "Price", "Availability Status" ]]
    for kitta_number, details in land_details.items():
        availability = land_availability[kitta_number]
        table_data.append([kitta_number]  + details )
    return table_data
# defining a function to start the procedure of renting land 
def rent_land(land_availability, land_details, table_data):
#executing while loop
    while True:
        print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid")) #displaying a table

        kitta_number = input("Enter kitta number of the land you want to borrow: ") #asking user for input

        if kitta_number not in land_availability:           #If user provides invalid kitta number, the following code executes
            print("Please provide a valid kitta number")
            continue

        if land_availability[kitta_number] != "Available":  #If user enters kitta number whose availability status is not available, the following code executes
            print("Kitta Number: ", kitta_number)
            print("Land is not available to rent")
            continue

        land_availability[kitta_number] = "Not Available"    #Changing the availability status to 'not available'
        
        borrower_name = input("Enter the name of person borrowing land: ")  #Asking the customer's name
        borrow_date = datetime.datetime.now()                               #Displaying the date and time when land was rented

        try:                                                                #exception handling
            months_rented = int(input("Enter the number of months for which the land is rented: "))
        except ValueError:
            print("Invalid input!!! Please only provide integer value.")
            continue

        # Calculating total rent
        price_per_month = int(land_details[kitta_number][3])  # Assuming the price is in the 4th position of land details
        total_rent = months_rented * price_per_month
        #For bill generation
        print("-----------------------------------------------------------------------------")
        print("-----------------------Rent bill generation---------------------------------")
        print("-----------------------------------------------------------------------------")
        print("Kitta Number: ", kitta_number)
        print("Location: ", land_details[kitta_number][0])
        print("Direction of land: ", land_details[kitta_number][1])
        print("Anna Details of land: ", land_details[kitta_number][2])
        print("Monthly price details of land: ", price_per_month)
        print("Duration of Rent: ", months_rented)
        print("Total Rent: ", total_rent)
        print("Date and time of rent: ", borrow_date)

        # Generating rent invoice
        generate_invoice(borrower_name, kitta_number, land_details[kitta_number], total_rent, borrow_date)
        #If the user wants to continue renting land 
        another_rent = input("Do you want to rent another land? (yes/no): ").lower()
        if another_rent != "yes":
            break
#defining the function named return_land to start the procedure of renting land
def return_land(land_availability, land_details, table_data):
    while True:
        print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid")) #displaying the table

        kitta_number = input("Enter kitta number of the land you want to return: ") #asking user for input

        if kitta_number not in land_availability:                                  #If user provides invalid kitta number, the following code executes
            print("Please provide a valid kitta number")
            continue

        if land_availability[kitta_number] != "Not Available":                  #If user enters kitta number whose availability status is  available, the following code executes
            print("Kitta Number: ", kitta_number)
            print("Land is not out to be returned")
            continue

        land_availability[kitta_number] = "Available"                           #Changing the availability status to ' available'
        returner_name = input("Enter the name of person returning land: ")      #Asking the customer's name
        return_date = datetime.datetime.now()                                   #Displaying the date and time when land was rented

        try:                                                                    #exception handling
            months_rented = int(input("Enter the number of months for which the land was rented: "))
            delayed_months = int(input("Enter the number of months of delayed in returning the land: "))
        except ValueError:
            print("Invalid input!!! Please only provide integer values.")
            continue

        # Calculating total rent and fine
        price_per_month = int(land_details[kitta_number][3])  # Assuming the price is in the 4th position of land details
        total_rent = months_rented * price_per_month
        fine = 0
        if delayed_months > 0: #If the user delays the return of land, crossing the due date, fine is charged
            fine = 0.1 * (delayed_months * price_per_month)
        #For bill generation
        print("-----------------------------------------------------------------------------")
        print("-----------------------Return bill generation---------------------------------")
        print("-----------------------------------------------------------------------------")
        print("Kitta Number: ", kitta_number)
        print("Location: ", land_details[kitta_number][0])
        print("Direction of land: ", land_details[kitta_number][1])
        print("Anna Details of land: ", land_details[kitta_number][2])
        print("Monthly price details of land: ", price_per_month)
        print("Duration of Rent: ", months_rented)
        print("Total Rent: ", total_rent)
        print("Fine: ", fine)
        print("Grand Total Amount: ", total_rent + fine)
        print("Date and time of return: ", return_date)

        # Generate return invoice
        generate_invoice(returner_name, kitta_number, land_details[kitta_number], total_rent + fine, return_date)
        #If the user wants to continue renting land 
        another_return = input("Do you want to return another land? (yes/no): ").lower()
        if another_return != "yes":
            break

def generate_invoice(person_name, kitta_number, land_info, total_amount, transaction_date):
    invoice_filename = f"Invoice_{person_name}_{kitta_number}_{transaction_date.strftime('%Y%m%d_%H%M%S')}.txt"
    with open(invoice_filename, "w") as invoice_file:
        invoice_file.write("Invoice Details:\n")
        invoice_file.write(f"Person Name: {person_name}\n")
        invoice_file.write(f"Kitta Number: {kitta_number}\n")
        invoice_file.write(f"Location: {land_info[0]}\n")
        invoice_file.write(f"Direction: {land_info[1]}\n")
        invoice_file.write(f"Anna Details: {land_info[2]}\n")
        invoice_file.write(f"Price per Month: {land_info[3]}\n")
        invoice_file.write(f"Transaction Date: {transaction_date}\n")
        invoice_file.write(f"Total Amount: {total_amount}\n")


def main():
    land_details = read_land_details()
    land_availability = {kitta_number: "Available" for kitta_number in land_details}
    table_data = update_table(land_details, land_availability)

    while True:
        print("Enter '1' to Rent Land")
        print("Enter '2' to Return land")
        print("Enter '3' to exit")
        value = input("Please enter a value: ")

        if value == '3':
            print("+++++++++++++++++++++++++++++++++++++++++++++")
            print("Thank you for using our land management system")
            print("+++++++++++++++++++++++++++++++++++++++++++++")
            break
        elif value == '1':
            print("You will now rent the land")
           
            rent_land(land_availability, land_details, table_data)
        elif value == '2':
            print("You will now rent the land")
            return_land(land_availability, land_details, table_data)
        else:
            print("+++++++++++++++++++++++++++++++++++++++++++++")
            print("Invalid input!! Please provide value as 1, 2, or 3")
            print("+++++++++++++++++++++++++++++++++++++++++++++")

if __name__ == "__main__":
    main()
