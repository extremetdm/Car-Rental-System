from DataStructures import *
import os

"""for all roles"""
ROLES = 'Manager','Customer Service Staff I','Customer Service Staff II','Car Service Staff'

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
    os.system('cls')
    updateMsg = [f'Staff ID\t: {user.id}',f'Staff Name\t: {user.name}',f'Staff Role\t: {user.role}',f'Register Date\t: {user.registration_date.date()}']
    print(f'Current Staff Record'.center((max(len(s) for s in updateMsg)) + 2, '-'))
    print('\n'.join(updateMsg))

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