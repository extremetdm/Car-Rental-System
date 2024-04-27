from DataStructures import *
import os

def getValidInput(inputMsg:str,*validConditionAndErrorMsg:tuple[any,str]) -> str:
    
    invalidInput = True
    while invalidInput:
        invalidInput = False
        enteredinput = input(inputMsg).strip()
        for validCondition, errorMsg in validConditionAndErrorMsg:
            if not validCondition(enteredinput):
                invalidInput = True
                print(errorMsg)
                break
            
    return enteredinput

# Login menu
def login() -> Staff:
# Returns user information if login successful.
 
    user:Staff = print('\nLogin\n')

    # Taking and checking input
    while user == None:

        # Input StaffID and get the corresponding info
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
    return user

def viewCar(constraint = lambda x:True):
  print('\n' + 217*'-')
  print(f"|{'Plate No.':^20}|{'Manufacturer':^15}|{'Model':^15}|{'Manufacture Year':^20}|{'Capacity':^20}|{'Last Service Date':^20}|{'Insurance No.':^20}|{'Insurance Exp. Date':^20}|{'Road Tax Exp. Date':^20}|{'Rental Rate':^20}|{'Availability':^15}|")
  print(217*'-')
  for car in Car.getCarList():
    if constraint(car):
      print(car)
  print(217*'-'+'\n')

"""For Staff"""

# for all roles
ROLES = 'Manager','Customer Service Staff I','Customer Service Staff II','Car Service Staff'

def updateProfile(user:Staff):
    header = f"|{'Name':^20}|{'Staff ID':^20}|{'Staff Role':^30}|{'Register Date':^20}|"
    os.system('cls')
    
    print('Current Staff Record'.center(len(header)),'\n','-' * (len(header) - 2))
    print(header+'\n','-' * (len(header) - 2))
    print(f"|{user.name:^20}|{user.id:^20}|{user.role:^30}|{str(user.registration_date.date()):^20}|")
    
    print('\nWhich data would you like to edit?', '\n-> '.join(['\n-> ID', 'Name', 'Password','Exit']))
    dataChange = getValidInput('\nEnter your choice: ',(lambda x:(x != ''), '\nchoice cannot be empty!'), (lambda x:x.capitalize() in ('Id','Name','Password','Exit','1','2','3','4'), '\nInvalid choice input'))
    dataChange = dataChange.replace(' ','')
        
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
            
    match dataChange.capitalize():
        case 'Id':
            user.id = getValidInput('\nEnter your new Staff ID: ',(lambda x:((x != '')),'\nStaff ID cannot be empty!'))
        case 'Name':
            user.name = getValidInput('\nEnter your new Name: ',(lambda x:((x != '')),'\nStaff name cannot be empty!'))
        case 'Password':
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
    if dataChange.capitalize() != 'Exit':
        print('\nProfile has been update','\n')

"""Staff function end"""

