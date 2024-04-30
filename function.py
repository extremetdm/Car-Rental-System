from DataStructures import *
import os

def getValidInput(inputMsg:str,*validConditionAndErrorMsg:tuple[any,str]) -> str:

    # Placeholder variable for checking input validity
    invalidInput:bool = True

    while invalidInput:

        invalidInput = False

        # Taking user input
        enteredinput:str = input(inputMsg).strip()

        # Checking whether entered input fulfills every condition
        for validCondition, errorMsg in validConditionAndErrorMsg:
            if not validCondition(enteredinput):

                # Output corresponding error message if any condition fails
                invalidInput = True
                print(errorMsg)
                break
            
    return enteredinput

def login() -> Staff:
 
    # Placeholder variable to store user information
    user:Staff|None = print('\nLogin\n')

    # Taking and checking input
    while user == None:

        # Input StaffID and get the corresponding staff info
        user = Staff.getStaff(getValidInput('StaffID: ',(Staff.staffInRecord,'\nInvalid StaffID!\n')))

        # Block access to accounts with too many login attempts
        if user.attempts == 3:
            user = print('\nThis account has been blocked! Please contact a manager.\n')  
        
        else:
            # Check password & keeping track of login attempts
            while input('Password: ') != user.password:
                user.attempts += 1
                Staff.updateRecord()
                if user.attempts == 3:
                    break
                print(f"\nWrong Password! {3-user.attempts} attempt{'' if user.attempts == 2 else 's'} remaining.\n")
            
            # Lock account when too many login attempts
            if user.attempts == 3:
                user = print(f'\nWrong Password! You account has been locked.\n')
                
            # Reset login attempt counter when login successful
            else:
                user.attempts = 0
                Staff.updateRecord()

    # Returns user information after succesful login.
    return user

def viewCar(constraint = lambda x:True):
    # Checking if any car fits the criteria
    if any(map(constraint,Car.getCarList())):

        # Header
        print()
        header = f"|{'Plate No.':^20}|{'Manufacturer':^15}|{'Model':^15}|{'Manufacture Year':^20}|{'Capacity':^20}|{'Last Service Date':^20}|{'Insurance No.':^20}|{'Insurance Exp. Date':^20}|{'Road Tax Exp. Date':^20}|{'Rental Rate':^20}|{'Availability':^15}|"
        print('Car Record'.center(len(header)),'\n','-' * (len(header)-2))
        print(header,'\n','-' * (len(header) - 2))
        
        # Car Info
        for car in Car.getCarList():
            if constraint(car):
                print(car)

        # Footer
        print(f' {"-" * (len(header) - 2)} ')
        
    else:
        print('\nNo car record found!\n')

def viewRental(constraint = lambda x:True):
    # Checking if any rental request fits the criteria
    if any(map(constraint,Rental.getRentalList())):

        # Header
        print('\n' + 148*'-')
        print(f"|{'Transaction ID':^20}|{'Car Plate No.':^20}|{'Customer ID':^20}|{'Rental Date':^20}|{'Return Date':^20}|{'Rental Fee':^20}|{'Status':^20}|")
        print(148*'-')

        # Rental info
        for rental in Rental.getRentalList():
            if constraint(rental):
              print(rental)

        # Footer
        print(148*'-'+'\n')

    else:
        print('\nNo rental record found!\n')

def validDate(dateInput):
  # Checking for valid date in the form YYYY-MM-DD
  try:
    datetime.strptime(dateInput,'%Y-%m-%d')
    return True
  except ValueError:
    return False

def updateProfile(user:Staff):
    # Define the header for the display table
    header = f"|{'Name':^20}|{'Staff ID':^20}|{'Staff Role':^30}|{'Register Date':^20}|"
    
    # Clear the console
    os.system('cls')
    
    # Print the current staff record
    print('Current Staff Record'.center(len(header)),'\n','-' * (len(header) - 2))
    print(header+'\n','-' * (len(header) - 2))
    print(f"|{user.name:^20}|{user.id:^20}|{user.role:^30}|{str(user.registration_date.date()):^20}|")
    
    # Ask the user which data they would like to edit
    print('\nWhich data would you like to edit?', '\n-> '.join(['\n-> ID', 'Name', 'Password','Exit']))
    
    # Get the user's choice
    dataChange = getValidInput('\nEnter your choice: ',(lambda x:(x != ''), '\nchoice cannot be empty!'), (lambda x:x.capitalize() in ('Id','Name','Password','Exit','1','2','3','4'), '\nInvalid choice input'))
    
    # Remove any spaces from the user's choice
    dataChange = dataChange.replace(' ','')
        
    # If the user's choice is a number, convert it to the corresponding string
    if dataChange in ('1','2','3','4'):
        match dataChange:
            case '1':
                dataChange = 'Id'
            case '2':
                dataChange = 'Name'
            case '3':
                dataChange = 'Password'
            case '4':
                dataChange = 'Exit'
            
    # Depending on the user's choice, update the corresponding attribute of the user
    match dataChange.capitalize():
        case 'Id':
            user.id = getValidInput('\nEnter your new Staff ID: ',(lambda x:((x != '')),'\nStaff ID cannot be empty!'))
        case 'Name':
            user.name = getValidInput('\nEnter your new Name: ',(lambda x:((x != '')),'\nStaff name cannot be empty!'))
        case 'Password':
            # Ask the user to enter their new password twice for confirmation
            while True:
                password1 = getValidInput('\nEnter your new Password: ',(lambda x:((x != '')),'\nPassword cannot be empty!'))
                password2 = getValidInput('\nPlease comfirm your Password: ',(lambda x:((x != '')),'\nPassword Incorrect!'))
                if password1 == password2:
                    break
            user.password = password1
        case 'Exit':
            print('\nUpdate profile has been cancel.\n')
        case _:
            print(dataChange.capitalize(), ' is not in match list')
    
    # If the user didn't choose to exit, print a confirmation message
    if dataChange.capitalize() != 'Exit':
        print('\nProfile has been update','\n')

