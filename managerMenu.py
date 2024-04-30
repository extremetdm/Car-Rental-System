from DataStructures import *
from function import *

# for all roles
ROLES = 'Manager','Customer Service Staff I','Customer Service Staff II','Car Service Staff'

def registerStaff(user:Staff):
    ROLES = 'Manager','Customer Service Staff I','Customer Service Staff II','Car Service Staff'
    id = getValidInput('\nEnter new Staff id: ',(lambda x:((x != '') and (' ' not in x )),'\nStaff id cannot be empty or having space!'), (lambda id:not Staff.staffInRecord(id), '\nStaff ID already exist'))
    name = getValidInput('\nEnter Staff name: ',(lambda x:x != '','\nStaff name cannot be empty!'))
    
    print('\n','Role'.center((max(len(s) for s in ROLES)) + 2, '-'))
    print('\n'.join(f'{i+1}) {ROLES[i]}' for i in range(4)))
    role = getValidInput('\nEnter Staff role (\'1\',\'2\',\'3\',\'4\'): ',
                            (lambda x:x != '','\nStaff role cannot be empty'),
                            (lambda x:x in ('1','2','3','4','Manager','Customer Service Staff I','Customer Service Staff II','Car Service Staff'), '\nUnexpected role given'),)

    match role:
        case '1':
            role = ROLES[0]
        case '2':
            role = ROLES[1]
        case '3':
            role = ROLES[2]
        case '4':
            role = ROLES[3]  
    
    Staff(id, name, role, id, registration_date = datetime.now())
    Staff.updateRecord()
    print("\n")
    header = f"|{'Staff ID':^20}|{'Name':^20}|{'Staff Role':^30}|{'Register Date':^20}|"
    print('New Staff detail'.center(len(header)),'\n','-' * (len(header) - 2))
    print(header,'\n','-' * (len(header) - 2))
    print(user.getStaff(id),'\n')
    
def updateExitingStaff(user:Staff):
    header = f"|{'Name':^20}|{'Staff ID':^20}|{'Staff Role':^30}|{'Status':^20}|"
    os.system('cls')
    
    print('Staff Record'.center(len(header)),'\n','-' * (len(header) - 2))
    print(header, '\n', '-' * len(header))
    
    for staff in Staff.getStaffList():
        if staff != user:
            accountStatus = 'Block' if staff.attempts == 3 else 'Active'
            print(f"|{staff.name:^20}|{staff.id:^20}|{staff.role:^30}|{accountStatus:^20}|")

    action = getValidInput('\nWhich action you would like to use?\n\n->\tblock\n->\tunblock\n->\trole\n->\texit\n\naction: ', 
                           (lambda x:x.lower() in ('block','unblock','role','exit','1','2','3','4'), 'Invalid input!'))
    match action:
        case '1':
            action = 'block'
        case '2':
            action = 'unblock'
        case '3':
            action = 'role'
        case '4':
            action = 'exit'

    if action.lower() in ('block','unblock'):
        staff_id = getValidInput('\nEnter Staff ID: ',
                        (lambda x:x != '', '\nStaff ID cannot be empty!'),
                        (lambda x:x != user, '\nStaff ID cannot be the current id'),
                        (lambda x:Staff.getStaff(x).role != 'Manager', '\nManager cannot change their own role'))

        staffDetail = Staff.getStaff(staff_id)
        if staffDetail:
            if action.lower() == 'block':
                staffDetail.attempts = 3
                print(f"\nStaff account with ID <{staff_id}> has been blocked.\n")
            else:
                staffDetail.attempts = 0
                print(f"\nStaff account with ID <{staff_id}> has been unblocked.\n")
        else:
            print(f"\nNo staff found with <{staff_id}>.\n")

    elif action.lower() == 'role':
        staff_id = getValidInput('\nWhich staff role you whould like to change?\nInsert the staff ID to update his role\n\nStaff ID: ',
                            (lambda x:x != '', '\nStaff ID cannot be empty'), 
                            (lambda id:Staff.staffInRecord(id), '\nInvalid Staff ID'),
                            (lambda x:Staff.getStaff(x).role != 'Manager', '\nManager cannot change their own role'))
        staff = Staff.getStaff(staff_id)
        staff.role = getValidInput('\nEnter Staff role (\'1\',\'2\',\'3\',\'4\'): ',
                            (lambda x:x != '','\nStaff role cannot be empty!'),
                            (lambda x:x in ('1','2','3','4','Manager','Customer Service Staff I','Customer Service Staff II','Car Service Staff'), '\nUnexpected role given'))
        
        Staff.updateRecord()
        print(f'\n<{staff_id}> has been updated')
        print("\n")
        header = f"|{'Staff ID':^20}|{'Name':^20}|{'Staff Role':^30}|{'Register Date':^20}|"
        print('Staff detail'.center(len(header)),'\n','-' * (len(header) - 2))
        print(header,'\n','-' * (len(header) - 2))
        print(user.getStaff(id),'\n')

        
        
    elif action.lower() == 'exit':
        print('\nupdate existing staff record has been cancel\n')

def deleteStaff_Record(user:Staff):
    header = f"|{'Name':^20}|{'Staff ID':^20}|{'Staff Role':^30}|"
    
    os.system('cls')
    print('Staff Record'.center(len(header)),'\n','-' * (len(header) - 2))
    print(header+'\n','-' * (len(header) - 2))
    for staff in Staff.getStaffList():
        print(f"|{staff.name:^20}|{staff.id:^20}|{staff.role:^30}|")
    while True:
        id = getValidInput('\nEnter Staff Id to delete record: ',(lambda x:x != '','\nStaff Id cannot be empty!'))
        if Staff.staffInRecord(id):
            print(f'Staff id with <{id}> found')
            run = getValidInput('\nDo you want to delete this record? (Y/N): ',(lambda x:x.upper() in ('Y','N'),'Invalid input!'))
            if run.upper() == 'Y':
                Staff.getStaff(id).delete()
                Staff.updateRecord()
                print(f"\nStaff ID <{id}> has been deleted.")
            else:
                print(f'Deletion process for Staff id <{id}> has cancel')
        else:
            print(f"\nNo staff found with ID <{id}>.")
        run = getValidInput('\nDo you still want to delete staff record? (Y/N): ',(lambda x:x.upper() in ('Y','N'),'Invalid input!'))
        if run.upper() == 'N':
            break
    print('\n')
    
def Update_rentingRate():
    header = f"|{'Car Plate':^20}|{'Manufacturer':^20}|{'Model':^20}|{'Capacity':^20}|{'Rental Rate':^20}|"
    
    os.system('cls')
    print('Current base rental rate per day'.center(len(header)),'\n','-' * (len(header) - 2))
    print(header,'\n','-' * (len(header) - 2))
    
    for car in Car.getCarList():
        print(f'|{car.registration_no:^20}|{car.manufacturer:^20}|{car.model:^20}|{car.capacity:^20}|{car.getRentalRate():^20}|')
    
    if getValidInput('\nDo you want to change the rental rate? (Y/N): ',(lambda x:x.upper() in ('Y','N'),'Invalid input!')).upper() == 'Y':
        updateCheck = getValidInput('\nHow would you like to be change? (capacity/model): ', (lambda x:(x != '') and (x.lower() in ('capacity','model','1','2')),'Invalid input!'))
        
        match updateCheck:
            case '1':
                updateCheck = 'capacity'
            case '2':
                updateCheck = 'model'
        
        if updateCheck.lower() == 'capacity':
            updateCapacity = int(getValidInput('\nWhich capacity rental rate you would like to change? ',
                                        (lambda x:x != '' ,'Capacity cannot be empty!'),
                                        (lambda x:x.isalnum(), 'Invalid input'),
                                        (lambda x:x not in (2, 4, 5, 6, 7, 8, 9), '\nCapacity not found.')))

                
            updateRate = float(getValidInput('\nThe latest rental rate: RM', (lambda x:x!= '','\nRental rate cannot be empty')))
                
            for car in Car.getCarList():
                if car.capacity == updateCapacity:
                    Car.updateDefaultRentalRate(updateCapacity, updateRate)
    
        elif updateCheck.lower() == 'model':
            updateModel = getValidInput('\nWhich model rental rate you would like to change? ',
                            (lambda x:(x != ''),'\nType of model cannot be empty'),
                            (lambda x: any(car.model == x for car in Car.getCarList()), '\nModel not found.'))

                
            updateRate = float(getValidInput('\nThe latest rental rate: RM', (lambda x:x!= '','\nRental rate cannot be empty')))
        
            for car in Car.getCarList():
                if car.model == updateModel:
                    car.setSpecificRentalRate(f'{updateRate:.2f}')

                

    print('After update'.center(len(header)),'\n','-' * (len(header) - 2))
    print(header,'\n','-' * (len(header) - 2))
    for car in Car.getCarList():
        print(f'|{car.registration_no:^20}|{car.manufacturer:^20}|{car.model:^20}|{car.capacity:^20}|{car.getRentalRate():^20}|')
    
    Car.updateRecord()
    print('\n')

def monthlyRevenue():  
    from datetime import datetime
    rentals_by_month = {}

    for rental in Rental._rentalList.values():
        if rental.status != 'Pending':  # Only include rentals where the customer has paid
            month_year = rental.rental_date.strftime('%B %Y')
            if month_year not in rentals_by_month:
                rentals_by_month[month_year] = []
            rentals_by_month[month_year].append(rental)

    all_month_years = list(rentals_by_month.keys())
    all_month_years = sorted(all_month_years, key=lambda x: datetime.strptime(x, '%B %Y'))

    print("Select the month and year for the report:")
    for i, month_year in enumerate(all_month_years, start=1):
        print(f"{i}. {month_year}")
    print(f"{len(all_month_years) + 1}. All months")

    month_year_input = getValidInput("Enter your choice: ", 
                                    (lambda x: x.isdigit() and 1 <= int(x) <= len(all_month_years) + 1, "Invalid choice. Please enter a number from the list."))

    month_year_input = all_month_years[int(month_year_input) - 1] if month_year_input != str(len(all_month_years) + 1) else 'all'

    for month_year, rentals in rentals_by_month.items():
        if month_year_input.lower() != 'all' and month_year != month_year_input:
            continue

        header = f"|{'Customer ID':^15}|{'Model':^20}|{'Rental Start Date':^19}|{'Rental End Date':^19}|{'Rental Period(days)':^20}|{'Rental Fee(RM)':^16}|"
        decorative_line = '~' * len(month_year)
        print(f'\n{decorative_line.center(len(header))}')
        print(f'{month_year.center(len(header))}')
        print(f'{decorative_line.center(len(header))}')
        print('-' * (len(header)))
        print(header,'\n','-' * (len(header) - 2))

        total_revenue = 0
        for rental in rentals:
            rental_period = (rental.return_date - rental.rental_date).days
            print(f'|{rental.customer.id:^15}|{rental.car.model:^20}|{rental.rental_date.strftime("%Y-%m-%d"):^19}|{rental.return_date.strftime("%Y-%m-%d"):^19}|{rental_period:^20}|{rental.rental_fee:^16.2f}|')
            total_revenue += rental.rental_fee
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
      
# For debugging purposes only
if __name__ == '__main__':
  Staff.readRecord()
  Customer.readRecord()
  Car.readRecord()
  Rental.readRecord()

  managerMenu(Staff.getStaff('mohdali'))