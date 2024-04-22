from DataStructures import *

"""for all roles"""
ROLES = ['Manager','Customer Service Staff I','Customer Service Staff II','Car Service Staff']

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


"""For Staff"""
def updateProfile(user:Staff):
    pass

def registerStaff(user:Staff):
    while True:
        id = getValidInput('\nEnter Staff id: ',lambda x:((x != '') and (' ' not in x )),'\nStaff id cannot be empty or having space!')
        if id in ROLES:
            print('Staff ID already exist')
            continue
        else:
            break
    while True:
        role = getValidInput('\nEnter Staff role: ',lambda x:x != '','\nStaff role cannot be empty or not in role!')
        if role in ROLES:
            break
        else:
            print('Unexpected role given')
            continue
    name = getValidInput('\nEnter Staff name: ',lambda x:x != '','\nStaff name cannot be empty!')
    
    Staff(id, name, role, id, registration_date = datetime.now())
    return "New Staff has been added"
  
def deleteStaff_Record(user:Staff):
    while True:
        id = getValidInput('\nEnter Staff Id to delete record: ',lambda x:x != '','\nStaff Id cannot be empty!')
        if id in user._staffList:
            print('Staff id with <{id}> found')
            run = getValidInput('\nDo you want to delete this record? (Y/N): ',lambda x:x.upper() in ('Y','N'))
            del user._staffList[id]
            print(f"\nStaff with ID \'{id}\' has been deleted.")
        else:
            print(f"\nNo staff found with ID {id}.")
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
    registrationDate = datetime.today()
    Customer(name,nric,passport,licenseNo,address,phone,registrationDate)
    print('\nCustomer has been successfully registered.\n')