from DataStructures import *
from function import *

def login():
# Login menu
# Returns user information if login successful. Exits program otherwise.
    print('\nLogin\n')

  # Taking and checking input
    while isinstance((loginStatus := Staff.login(input('Username: '),input('Password: '))),int):
        if loginStatus == 0:
            print('\nInvalid StaffID!\n')
        elif loginStatus < 3:
            print(f'\nWrong Password! {3-loginStatus} attempt(s) remaining.')
        elif loginStatus == 3:
            print(f'\nWrong Password! Program will now exit.')
        exit()
  
    return loginStatus

def getValidInput(inputMsg:str,validCondition,errorMsg:str = 'Invalid Input!'):
    while not validCondition(enteredinput := input(inputMsg)):
        print(errorMsg)
    return enteredinput

def updateStaff(user:Staff, edit:int = None, code:str = None):
        match code:
            case 'update':
                if id in Staff._staffList:
                    staff = Staff._staffList[id]
                    match edit:
                        case 1:
                            if id is not None:
                                staff.id = id
                        case 2:
                            if name is not None:
                                staff.name = name
                        case 3:
                            if password is not None:
                                staff.password = password
                        case 4:
                            return 0
                        case _:
                            return 'invalid input'
            case 'remove':
                if id in Staff._staffList:
                    del Staff._staffList[id]
                    return f"\nStaff with ID \'{id}\' has been deleted."
                else:
                    return f"\nNo staff found with ID {id}."

def registerStaff(user:Staff):
    id = getValidInput('\nEnter Staff id: ',lambda x:((x != '') and (' ' not in x )),'\nStaff id cannot be empty!')
    role = getValidInput('\nEnter Staff name: ',lambda x:x != '','\nStaff name cannot be empty!')
    name = getValidInput('\nEnter Staff name: ',lambda x:x != '','\nStaff name cannot be empty!')
    
    
    if id not in Staff._staffList:
            Staff(id, Staff.name, Staff.role, id, registration_date = datetime.now())
            return "New Staff has been added"
  
def deleteStaff_Record(user:Staff):
    while True:
        print(updateStaff(id = input('Delete Staff record with ID: '), code = 'remove'))
        run = getValidInput('\nDo you still want to delete staff record? (Y/N): ',lambda x:x.upper() in ('Y','N'))
        if run == 'N':
            break
        
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
  Customer(name,nric,passport,licenseNo,address,phone,datetime.today())
  print('\nCustomer has been successfully registered.\n')