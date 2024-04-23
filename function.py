from DataStructures import *
import os

# for all roles
ROLES = 'Manager','Customer Service Staff I','Customer Service Staff II','Car Service Staff'

def getValidInput(inputMsg:str,validCondition,errorMsg:str = 'Invalid Input!'):
  while not validCondition(enteredinput := input(inputMsg)):
    print(errorMsg)
  return enteredinput

# Login menu
def login() -> Staff:
# Returns user information if login successful.
 
    user:Staff = print('\nLogin\n')

    # Taking and checking input
    while user == None:

        # Input StaffID and get the corresponding info
        user = Staff.getStaff(getValidInput('StaffID: ',lambda x:Staff.getStaff(x) != None,'\nInvalid StaffID!\n'))

        # Block access to accounts with too many login attempts
        if user.attempts == 3:
            user = print('\nThis account has been locked! Please contact a manager.\n')  
        
        else:
            # Check password & keeping track of login attempts
            while (user.attempts < 3) & ((password := input('Password: ')) != user.password):
                print(f'\nWrong Password! {3-user.attempts} attempt(s) remaining.\n')
                user.attempts += 1

            # Lock account when too many login attempts
            if user.attempts == 3:
                user = print(f'\nWrong Password! You account has been locked.\n')

            # Reset login attempt counter when login successful
            else:
                user.attempts = 1
    return user

"""For Staff"""

def updateProfile(user:Staff):
    os.system('cls')
    updateMsg = [f'Staff ID\t: {user.id}',f'Staff Name\t: {user.name}',f'Staff Role\t: {user.role}',f'Register Date\t: {user.registration_date.date()}']
    print(f'Current Staff Record'.center((max(len(s) for s in updateMsg)) + 2, '-'),'\n','\n'.join(updateMsg))
    while True:
        print('\nWhich data would you like to edit?', '\n-> '.join(['\n-> ID', 'Name', 'Password']))
        dataChange = getValidInput('\nEnter your choice: ',lambda x:((x != '')),'\nchoice cannot be empty!')
        if dataChange.capitalize() in ('Id','Name','Password'):
            break
        else:
            print('invalid choice input\n')
            
    match dataChange.capitalize():
        case 'Id':
            user.id = getValidInput('\nEnter your new Staff ID: ',lambda x:((x != '')),'\nStaff ID cannot be empty!')
        case 'Name':
            user.name = getValidInput('\nEnter your new Name: ',lambda x:((x != '')),'\nStaff name cannot be empty!')
        case 'Password':
            user.password = getValidInput('\nEnter your new Password: ',lambda x:((x != '')),'\nPassword cannot be empty!')
        case _:
            print(dataChange.capitalize(), ' is not in match list')

def registerStaff(user:Staff):
    while True:
        id = getValidInput('\nEnter Staff id: ',lambda x:((x != '') and (' ' not in x )),'\nStaff id cannot be empty or having space!')
        if id in ROLES:
            print('Staff ID already exist')
            continue
        else:
            break
    while True:
        print(ROLES)
        role = getValidInput('\nEnter Staff role: ',lambda x:x != '','\nStaff role cannot be empty or not in role!')
        if role in ROLES:
            break
        else:
            print('Unexpected role given')
            continue
    name = getValidInput('\nEnter Staff name: ',lambda x:x != '','\nStaff name cannot be empty!')
    
    Staff(id, name, role, id, registration_date = datetime.now())
    print("New Staff has been added")
  
def deleteStaff_Record(user:Staff):
    for staff in user.getStaff(staff):
        print(staff)
    while True:
        #print('\n'.join((user._staffList[i][0]) for i in range(len(user._staffList))))
        id = getValidInput('\nEnter Staff Id to delete record: ',lambda x:x != '','\nStaff Id cannot be empty!')
        if id in user._staffList:
            print(f'Staff id with <{id}> found')
            run = getValidInput('\nDo you want to delete this record? (Y/N): ',lambda x:x.upper() in ('Y','N'))
            if run == 'Y':
                del user._staffList[id]
                print(f"\nStaff ID <{id}> has been deleted.")
            else:
                print(f'Deletion process for Staff id <{id}> has cancel')
        else:
            print(f"\nNo staff found with ID <{id}>.")
        run = getValidInput('\nDo you still want to delete staff record? (Y/N): ',lambda x:x.upper() in ('Y','N'))
        if run == 'N':
            break

"""for Customer"""
def registerCustomer():
    name = getValidInput('\nEnter customer name: ',lambda x:x != '','\nCustomer name cannot be empty!')
    localness = getValidInput('\nIs customer a local? (Y/N): ',lambda x:x.upper() in ('Y','N'))
    if localness == 'Y':
        # if im bothered enough imma do further validation with date, state code and input with - but for now this is good enough 
        nric = getValidInput('\nEnter customer NRIC (without -): ',lambda x:x.isnumeric() & (len(x) == 12),'\nInvalid NRIC!')
        passport = None
    else:
        nric = None
        passport = getValidInput('\nEnter customer passport number: ',lambda x:x != '','\nPassport number cannot be empty!')
    licenseNo = getValidInput('\nEnter customer driving license card number: ',lambda x:x != '','\nDriving license card number cannot be empty!')
    address = getValidInput('\nEnter customer address: ',lambda x:x != '','\nAddress cannot be empty!')
    # if im bothered enough may actually validate phone number but for now this is fine
    phone = getValidInput('\nEnter customer phone number: ',lambda x:x != '','\nPhone number cannot be empty!')
    registrationDate = datetime.today()
    Customer(name,nric,passport,licenseNo,address,phone,registrationDate)
    print('\nCustomer has been successfully registered.\n')