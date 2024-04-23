from DataStructures import *
import os
import getpass

# for all roles
ROLES = 'Manager','Customer Service Staff I','Customer Service Staff II','Car Service Staff'

def getValidInput(inputMsg:str,validCondition,errorMsg:str = 'Invalid Input!',hide_input:int = 0):
    if hide_input == 1:
        while not validCondition(enteredinput := getpass.getpass(inputMsg)):
            print(errorMsg)
    else:
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
            user = print('\nThis account has been blocked! Please contact a manager.\n')  
        
        else:
            # Check password & keeping track of login attempts
            while (password := getpass.getpass('Password: ')) != user.password:
                user.attempts += 1
                if user.attempts == 3:
                    break
                print(f"\nWrong Password! {3-user.attempts} attempt{'' if user.attempts == 2 else 's'} remaining.\n")
            
            # Lock account when too many login attempts
            if user.attempts == 3:
                user = print(f'\nWrong Password! You account has been locked.\n')

            # Reset login attempt counter when login successful
            else:
                user.attempts = 0
    return user

"""For Staff"""

def updateProfile(user:Staff):
    os.system('cls')
    updateMsg = [f'Staff ID\t: {user.id}',f'Staff Name\t: {user.name}',f'Staff Role\t: {user.role}',f'Register Date\t: {user.registration_date.date()}']
    print(f'Current Staff Record'.center((max(len(s) for s in updateMsg)) + 2, '-'),'\n\b','\n'.join(updateMsg))
    while True:
        print('\nWhich data would you like to edit?', '\n-> '.join(['\n-> ID', 'Name', 'Password','Exit']))
        dataChange = getValidInput('\nEnter your choice: ',lambda x:((x != '')),'\nchoice cannot be empty!')
        dataChange = dataChange.replace(' ','')
        if dataChange.capitalize() in ('Id','Name','Password','Exit'):
            break
        else:
            print('invalid choice input\n')
            
    match dataChange.capitalize():
        case 'Id':
            user.id = getValidInput('\nEnter your new Staff ID: ',lambda x:((x != '')),'\nStaff ID cannot be empty!')
        case 'Name':
            user.name = getValidInput('\nEnter your new Name: ',lambda x:((x != '')),'\nStaff name cannot be empty!')
        case 'Password':
            while True:
                password1 = getValidInput('\nEnter your new Password: ',lambda x:((x != '')),'\nPassword cannot be empty!',1)
                password2 = getValidInput('\nPlease comfirm your Password: ',lambda x:((x != '')),'\nPassword Incorrect!',1)
                if password1 == password2:
                    break
            user.password = password1
        case 'Exit':
            print('\nUpdate profile has been cancel.\n')
        case _:
            print(dataChange.capitalize(), ' is not in match list')
    if dataChange.capitalize() != 'Exit':
        print('\nProfile has been update','\n')

def registerStaff(user:Staff):
    while True:
        id = getValidInput('\nEnter new Staff id: ',lambda x:((x != '') and (' ' not in x )),'\nStaff id cannot be empty or having space!')
        if id in ROLES:
            print('Staff ID already exist')
            continue
        else:
            break
    name = getValidInput('\nEnter Staff name: ',lambda x:x != '','\nStaff name cannot be empty!')
    while True:
        print('\n','Role'.center((max(len(s) for s in ROLES)) + 2, '-'))
        print('\n'.join(f'{i+1}) {ROLES[i]}' for i in range(4)))
        role = getValidInput('\nEnter Staff role (\'1\',\'2\',\'3\',\'4\'): ',lambda x:x != '','\nStaff role cannot be empty or not in role!')
        if role in ('1','2','3','4'):
            break
        else:
            print('Unexpected role given')
            continue
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
    print("\nNew Staff detail:\n")
    header = f"|{'Staff ID':^20}|{'Name':^20}|{'Staff Role':^30}|{'Register Date':^20}|"
    print(header,'\n','-' * (len(header) - 2))
    print(user.getStaff(id),'\n')
    
def updateExitingStaff(user:Staff):
    header = f"|{'Name':^20}|{'Staff ID':^20}|{'Staff Role':^30}|{'Status':^20}|"
    os.system('cls')
    print(header, '\n', '-' * len(header))
    
    for staff in Staff.getStaffList():
        accountStatus = 'Block' if staff.attempts == 3 else 'Active'
        print(f"|{staff.name:^20}|{staff.id:^20}|{staff.role:^30}|{accountStatus:^20}|")

    check = getValidInput('\nDo you want to block or unblock an account? (Y/N): ',lambda x:x.upper() in ('Y','N'))
    if check.upper() == 'Y':
        staff_id = getValidInput('\nEnter Staff ID: ',lambda x:x != '','\nStaff ID cannot be empty!')
        staffDetail = Staff.getStaff(staff_id)
        if staffDetail:
            action = getValidInput('\nWhich action whould you like to take? (block/unblock): ', lambda x:x.lower() in ('block','unblock'))
            if action.lower() == 'block':
                staffDetail.attempts = 3
                print(f"\nStaff account with ID <{staff_id}> has been blocked.\n")
            else:
                staffDetail.attempts = 0
                print(f"\nStaff account with ID <{staff_id}> has been unblocked.\n")
        else:
            print(f"\nNo staff found with <{staff_id}>.\n")


def deleteStaff_Record(user:Staff):
    header = f"|{'Name':^20}|{'Staff ID':^20}|{'Staff Role':^30}|"
    
    os.system('cls')
    print(header,'\n','-' * (len(header) - 2))
    for staff in Staff.getStaffList():
        print(f"|{staff.name:^20}|{staff.id:^20}|{staff.role:^30}|")
    while True:
        #print('\n'.join((user._staffList[i][0]) for i in range(len(user._staffList))))
        id = getValidInput('\nEnter Staff Id to delete record: ',lambda x:x != '','\nStaff Id cannot be empty!')
        if id in user._staffList:
            print(f'Staff id with <{id}> found')
            run = getValidInput('\nDo you want to delete this record? (Y/N): ',lambda x:x.upper() in ('Y','N'))
            if run.upper() == 'Y':
                del user._staffList[id]
                print(f"\nStaff ID <{id}> has been deleted.")
            else:
                print(f'Deletion process for Staff id <{id}> has cancel')
        else:
            print(f"\nNo staff found with ID <{id}>.")
        run = getValidInput('\nDo you still want to delete staff record? (Y/N): ',lambda x:x.upper() in ('Y','N'))
        if run.upper() == 'N':
            break
    print('\n')

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