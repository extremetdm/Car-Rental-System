from DataStructures import *
from function import *

# define all roles
ROLES = 'Manager','Customer Service Staff I','Customer Service Staff II','Car Service Staff'

#For adding a new staff into the records
def registerStaff(user:Staff):
    # Define the roles
    ROLES = 'Manager','Customer Service Staff I','Customer Service Staff II','Car Service Staff'
    
    # Ask the user for the new staff ID
    id = getValidInput('\nEnter new Staff id: ',(lambda x:((x != '') and (' ' not in x )),'\nStaff id cannot be empty or having space!'), (lambda id:not Staff.staffInRecord(id), '\nStaff ID already exist'))
    
    # Ask the user for the new staff name
    name = getValidInput('\nEnter Staff name: ',(lambda x:x != '','\nStaff name cannot be empty!'))
    
    # Print the roles
    print('\n','Role'.center((max(len(s) for s in ROLES)) + 2, '-'))
    print('\n'.join(f'{i+1}) {ROLES[i]}' for i in range(4)))
    
    # Ask the user for the new staff role
    role = getValidInput('\nEnter Staff role (\'1\',\'2\',\'3\',\'4\'): ',
                            (lambda x:x != '','\nStaff role cannot be empty'),
                            (lambda x:x in ('1','2','3','4','Manager','Customer Service Staff I','Customer Service Staff II','Car Service Staff'), '\nUnexpected role given'),)

    # Convert the user's input to the corresponding role
    match role:
        case '1':
            role = ROLES[0]  # If the user input 1, change it to 'Manager'
        case '2':
            role = ROLES[1]  # If the user input 2, change it to 'Customer Service Staff I'
        case '3':
            role = ROLES[2]  # If the user input 3, change it to 'Customer Service Staff II'
        case '4':
            role = ROLES[3]  # If the user input 4, change it to 'Car Service Staff'
    
    # Add the new staff to the record
    Staff(id, name, role, id, registration_date = datetime.now())
    
    # Update the staff record
    Staff.updateRecord()
    
    # Print the updated table
    print("\n")
    header = f"|{'Staff ID':^20}|{'Name':^20}|{'Staff Role':^30}|{'Register Date':^20}|"
    print('New Staff detail'.center(len(header)),'\n','-' * (len(header) - 2))
    print(header,'\n','-' * (len(header) - 2))
    print(user.getStaff(id),'\n')


#update staff record like role and status
def updateExitingStaff(user:Staff):
    # Define the header for the table
    header = f"|{'Name':^20}|{'Staff ID':^20}|{'Staff Role':^30}|{'Status':^20}|"
    
    # Clear the console
    os.system('cls')
    
    # Print the table header
    print('Staff Record'.center(len(header)),'\n','-' * (len(header) - 2))
    print(header, '\n', '-' * len(header))
    
    # Print each staff's details in a new row of the table
    for staff in Staff.getStaffList():
        if staff != user:
            accountStatus = 'Block' if staff.attempts == 3 else 'Active'
            print(f"|{staff.name:^20}|{staff.id:^20}|{staff.role:^30}|{accountStatus:^20}|")

    # Ask the user which action they would like to perform
    action = getValidInput('\nWhich action you would like to use?\n\n->\tblock\n->\tunblock\n->\trole\n->\texit\n\naction: ', 
                           (lambda x:x.lower() in ('block','unblock','role','exit','1','2','3','4'), 'Invalid input!'))
    
    # Convert the user's input to the corresponding option
    match action:
        case '1':
            action = 'block'  # If the user input 1, change it to 'block'
        case '2':
            action = 'unblock'  # If the user input 2, change it to 'unblock'
        case '3':
            action = 'role'  # If the user input 3, change it to 'role'
        case '4':
            action = 'exit'  # If the user input 4, change it to 'exit'

    # If the user chose to block or unblock a staff member
    if action.lower() in ('block','unblock'):
        # Ask the user for the ID of the staff member to block/unblock
        staff_id = getValidInput('\nEnter Staff ID: ',
                        (lambda x:x != '', '\nStaff ID cannot be empty!'),
                        (lambda x:x != user, '\nStaff ID cannot be the current id'),
                        (lambda x:Staff.staffInRecord, '\nStaff id is not in record')
                        (lambda x:Staff.getStaff(x).role != 'Manager', '\nManager cannot change their own role'))

        # Get the staff member's details
        staffDetail = Staff.getStaff(staff_id)
        if staffDetail:
            # If the user chose to block the staff member, set the staff member's attempts to 3
            if action.lower() == 'block':
                staffDetail.attempts = 3
                print(f"\nStaff account with ID <{staff_id}> has been blocked.\n")
            
            # If the user chose to unblock the staff member, set the staff member's attempts to 0
            else:
                staffDetail.attempts = 0
                print(f"\nStaff account with ID <{staff_id}> has been unblocked.\n")
        else:
            # If no staff member was found with the given ID, inform the user
            print(f"\nNo staff found with <{staff_id}>.\n")

    # If the user chose to update a staff member's role
    elif action.lower() == 'role':
        # Ask the user for the ID of the staff member whose role they want to change
        staff_id = getValidInput('\nWhich staff role you whould like to change?\nInsert the staff ID to update his role\n\nStaff ID: ',
                            (lambda x:x != '', '\nStaff ID cannot be empty'), 
                            (lambda id:Staff.staffInRecord(id), '\nInvalid Staff ID'),
                            (lambda x:Staff.getStaff(x).role != 'Manager', '\nManager cannot change their own role'))
        # Get the staff member's details
        staff = Staff.getStaff(staff_id)
        
        # Print each role from the ROLES dictionary
        print("ROLES")
        for key, value in enumerate(ROLES, start=1):
            print(f"-> {key}. {value}")
    
        # Ask the user to enter a role
        role = getValidInput('\nEnter Staff role (\'1\',\'2\',\'3\',\'4\'): ',
                            (lambda x:x != '','\nStaff role cannot be empty!'),
                            (lambda x:str(x).isdigit() and 1 <= int(x) <= len(ROLES), '\nShould be enter the number provide'))

        
        # Convert the user's input to the corresponding role
        match role:
            case '1':
                staff.role = ROLES[0]  # If the user input 1, change it to 'Manager'
            case '2':
                staff.role = ROLES[1]  # If the user input 2, change it to 'Customer Service Staff I'
            case '3':
                staff.role = ROLES[2]  # If the user input 3, change it to 'Customer Service Staff II'
            case '4':
                staff.role = ROLES[3]  # If the user input 4, change it to 'Car Service Staff'
        
        # Update the staff records
        Staff.updateRecord()
        # Inform the user that the staff member's role has been updated
        print(f'\n<{staff_id}> has been updated')
        
        # Print the updated table
        print("\n")
        header = f"|{'Staff ID':^20}|{'Name':^20}|{'Staff Role':^30}|{'Register Date':^20}|"
        print('Staff detail'.center(len(header)),'\n','-' * (len(header) - 2))
        print(header,'\n','-' * (len(header) - 2))
        print(user.getStaff(staff_id),'\n')

    # If the user chose to exit, inform them that the update process has been cancelled
    elif action.lower() == 'exit':
        print('\nupdate existing staff record has been cancel\n')



#To delete staff which is in staff record
def deleteStaff_Record(user:Staff):
    # Define the header for the table
    header = f"|{'Name':^20}|{'Staff ID':^20}|{'Staff Role':^30}|"
    
    # Clear the console
    os.system('cls')
    
    # Print the table header
    print('Staff Record'.center(len(header)),'\n','-' * (len(header) - 2))
    print(header+'\n','-' * (len(header) - 2))
    
    # Print each staff's details in a new row of the table
    for staff in Staff.getStaffList():
        print(f"|{staff.name:^20}|{staff.id:^20}|{staff.role:^30}|")

    # Start a loop to delete staff records
    while True:
        # Ask the user for the ID of the staff record to delete
        id = getValidInput('\nEnter Staff Id to delete record: ',(lambda x:x != '','\nStaff Id cannot be empty!'))
        
        # If the staff ID is in the records
        if Staff.staffInRecord(id):
            #To prevent user delete his own or delete a Manager
            if user.id == id:
                print('\nYou cannot delete Manager or delete yourself')
                continue
            # Inform the user that the staff ID was found
            print(f'Staff id with <{id}> found')
            # Ask the user to confirm the deletion
            run = getValidInput('\nDo you want to delete this record? (Y/N): ',(lambda x:x.upper() in ('Y','N'),'Invalid input!'))
            # If the user confirmed the deletion
            if run.upper() == 'Y':
                # Delete the staff record
                Staff.getStaff(id).delete()
                # Update the staff records
                Staff.updateRecord()
                # Inform the user that the staff record was deleted
                print(f"\nStaff ID <{id}> has been deleted.")
            else:
                # If the user cancelled the deletion, inform them
                print(f'Deletion process for Staff id <{id}> has cancel')
        else:
            # If the staff ID is not in the records, inform the user
            print(f"\nNo staff found with ID <{id}>.")
        # Ask the user if they want to delete another staff record
        run = getValidInput('\nDo you still want to delete staff record? (Y/N): ',(lambda x:x.upper() in ('Y','N'),'Invalid input!'))
        
        # If the user does not want to delete another staff record, break the loop
        if run.upper() == 'N':
            break
    print('\n')

    
#Update the renting rate for each car, or update the base rate base on car capacity
def Update_rentingRate():
    # Define the header for the table
    header = f"|{'Car Plate':^20}|{'Manufacturer':^20}|{'Model':^20}|{'Capacity':^20}|{'Rental Rate':^20}|"
    
    # Clear the console
    os.system('cls')
    
    # Print the table header
    print('Current base rental rate per day'.center(len(header)),'\n','-' * (len(header) - 2))
    print(header,'\n','-' * (len(header) - 2))
    
    # Print each car's details in a new row of the table
    for car in Car.getCarList():
        print(f'|{car.registration_no:^20}|{car.manufacturer:^20}|{car.model:^20}|{car.capacity:^20}|{car.getRentalRate():^20}|')
    
    # Ask the user if they want to update the rental rate
    if getValidInput('\nDo you want to change the rental rate? (Y/N): ',(lambda x:x.upper() in ('Y','N'),'Invalid input!')).upper() == 'Y':
        
        # Ask the user how they want to update the rental rate
        updateCheck = getValidInput('\nHow would you like to be change? (capacity/model): ', (lambda x:(x != '') and (x.lower() in ('capacity','model','1','2')),'Invalid input!'))
        
        # Convert the user's input to the corresponding option
        match updateCheck:
            case '1':
                updateCheck = 'capacity'  # If the user input 1, change it to 'capacity'
            case '2':
                updateCheck = 'model'  # If the user input 2, change it to 'model'
        
        # If the user chose to update by capacity
        if updateCheck.lower() == 'capacity':
            
            # Ask the user which capacity's rental rate they want to change
            updateCapacity = int(getValidInput('\nWhich capacity rental rate you would like to change? ',
                                        (lambda x:x != '' ,'Capacity cannot be empty!'),
                                        (lambda x:x.isalnum(), 'Invalid input'),
                                        (lambda x:Car.carInRecord)
                                        (lambda x:x not in (2, 4, 5, 6, 7, 8, 9), '\nCapacity not found.')))

            # Ask the user for the new rental rate
            updateRate = float(getValidInput('\nThe latest rental rate: RM', (lambda x:x!= '','\nRental rate cannot be empty')))
                
            # Update the default rental rate for the specified capacity
            for car in Car.getCarList():
                if car.capacity == updateCapacity:
                    Car.updateDefaultRentalRate(updateCapacity, updateRate)
    
        # If the user chose to update by model
        elif updateCheck.lower() == 'model':
            
            # Ask the user which model's rental rate they want to change
            updateModel = getValidInput('\nWhich model rental rate you would like to change? ',
                            (lambda x:(x != ''),'\nType of model cannot be empty'),
                            (lambda x: any(car.model == x for car in Car.getCarList()), '\nModel not found.'))

            # Ask the user for the new rental rate
            updateRate = float(getValidInput('\nThe latest rental rate: RM', (lambda x:x!= '','\nRental rate cannot be empty')))
                
            # Update the rental rate for all cars of the specified model
            for car in Car.getCarList():
                if car.model == updateModel:
                    car.setSpecificRentalRate(f'{updateRate:.2f}')

    # Print the updated table
    print('After update'.center(len(header)),'\n','-' * (len(header) - 2))
    print(header,'\n','-' * (len(header) - 2))
    for car in Car.getCarList():
        print(f'|{car.registration_no:^20}|{car.manufacturer:^20}|{car.model:^20}|{car.capacity:^20}|{car.getRentalRate():^20}|')
    
    # Update the car records
    Car.updateRecord()
    print('\n')


#To see the revenue for each month
def monthlyRevenue():  
    from datetime import datetime
    rentals_by_month = {}
    
    # Loop through all rentals
    for rental in Rental._rentalList.values():
        # Only include rentals where the customer has paid
        if rental.status != 'Pending':  
            # Format the rental date to 'Month Year'
            month_year = rental.rental_date.strftime('%B %Y')
            # If the month_year is not already a key in the dictionary, add it
            if month_year not in rentals_by_month:
                rentals_by_month[month_year] = []
            # Append the rental to the list of rentals for the given month_year
            rentals_by_month[month_year].append(rental)

    # Get a list of all month_years and sort it
    all_month_years = list(rentals_by_month.keys())
    all_month_years = sorted(all_month_years, key=lambda x: datetime.strptime(x, '%B %Y'))

    # Prompt the user to select a month and year for the report
    print("Select the month and year for the report:")
    for i, month_year in enumerate(all_month_years, start=1):
        print(f"{i}. {month_year}")
    print(f"{len(all_month_years) + 1}. All months")

    # Get the user's choice
    month_year_input = getValidInput("Enter your choice: ", 
                                    (lambda x: x.isdigit() and 1 <= int(x) <= len(all_month_years) + 1, "Invalid choice. Please enter a number from the list."))

    # If the user chose 'All months', set month_year_input to 'all'
    month_year_input = all_month_years[int(month_year_input) - 1] if month_year_input != str(len(all_month_years) + 1) else 'all'

    # Loop through all rentals by month_year
    for month_year, rentals in rentals_by_month.items():
        # If the user didn't choose 'All months' and the current month_year is not the chosen one, skip this iteration
        if month_year_input.lower() != 'all' and month_year != month_year_input:
            continue

        # Print the header for the table
        header = f"|{'Customer ID':^15}|{'Model':^20}|{'Rental Start Date':^19}|{'Rental End Date':^19}|{'Rental Period(days)':^20}|{'Rental Fee(RM)':^16}|"
        decorative_line = '~' * len(month_year)
        print(f'\n{decorative_line.center(len(header))}')
        print(f'{month_year.center(len(header))}')
        print(f'{decorative_line.center(len(header))}')
        print('-' * (len(header)))
        print(header,'\n','-' * (len(header) - 2))

        # Initialize total_revenue to 0
        total_revenue = 0
        # Loop through all rentals for the current month_year
        for rental in rentals:
            # Calculate the rental period in days
            rental_period = (rental.return_date - rental.rental_date).days
            # Print the rental details
            print(f'|{rental.customer.id:^15}|{rental.car.model:^20}|{rental.rental_date.strftime("%Y-%m-%d"):^19}|{rental.return_date.strftime("%Y-%m-%d"):^19}|{rental_period:^20}|{rental.rental_fee:^16.2f}|')
            # Add the rental fee to the total revenue
            total_revenue += rental.rental_fee
        # Print the total revenue for the current month_year
        print('*' * len(header))
        print(f'Total Revenue -> RM{total_revenue:.2f}')

    print('\n')


def managerMenu(user:Staff):
  while True:
    # Menu selection
    print('1.\tUpdate own profile')
    print('2.\tRegister new staff')
    print('3.\tUpdate existing staff record')
    print('4.\tDelete staff record')
    print('5.\tUpdate car renting rate')
    print('6.\tView monthly revenue report')
    print('7.\tExit program')
    
    # Determining operation
    operation = getValidInput('\nEnter operation number: ',(lambda x:x in ('1','2','3','4','5','6','7'),'\nInvalid operation number!'))
    match operation:
      case '1':
        updateProfile(user)

      case '2':
        registerStaff(user)

      case '3':
        updateExitingStaff(user)

      case '4':
        deleteStaff_Record(user)

      case '5':
        Update_rentingRate()

      case '6':
        monthlyRevenue()

      case '7':
        return
