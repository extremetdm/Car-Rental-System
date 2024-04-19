from DataStructures import *

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

def updateStaff(cls, id:str = None, name:str=None, role:str=None, password:str = None, code:str = None, edit:int = None):
        if id not in cls._staffList and code == 'new':
            Staff(id, name, role, password = id, registration_date = datetime.now())
            return "New Staff has been added"
        match code:
            case 'update':
                if id in cls._staffList:
                    staff = cls._staffList[id]
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
                if id in cls._staffList:
                    del cls._staffList[id]
                    return f"\nStaff with ID \'{id}\' has been deleted."
                else:
                    return f"\nNo staff found with ID {id}."