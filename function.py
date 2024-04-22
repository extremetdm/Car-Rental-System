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

def updateStaff(user:Staff, id:str = None, name:str=None, role:str=None, password:str = None, code:str = None, edit:int = None):
        if id not in Staff._staffList and code == 'new':
            Staff(id, name, role, password = id, registration_date = datetime.now())
            return "New Staff has been added"
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
    while True:
        id = getValidInput('\nEnter Staff id: ',lambda x:((x != '') and (' ' not in x )),'\nStaff id cannot be empty or having space!')
        if id in ROLES:
            print('Staff ID already exist')
            continue
        else:
            break
    while True:
        role = getValidInput('\nEnter Staff role: ',lambda x:x != ''),'\nStaff role cannot be empty or not in role!')
        if role in ROLES:
            break
        else:
            print('unexpected role given')
            continue
    name = getValidInput('\nEnter Staff name: ',lambda x:x != '','\nStaff name cannot be empty!')
    
    Staff(id, name, role, id, registration_date = datetime.now())
    return "New Staff has been added"
  
def deleteStaff_Record(user:Staff):
  while True:
    print(user.updateStaff(id = input('Delete Staff record with ID: '), code = 'remove'))
    run = getValidInput('\nDo you still want to delete staff record? (Y/N): ',lambda x:x.upper() in ('Y','N'))
    if run == 'N':
      break
  
def registerCustomer():
    pass