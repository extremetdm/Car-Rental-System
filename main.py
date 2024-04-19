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

def updateProfile(user:Staff):
  user.updateStaff(user.id,input("new name: "),input("new password: "))
  
def registerStaff(user:Staff):
  user.newStaff(input("New Staff ID: "), input("New Staff Name: " ), input("New Staff Role: "))
  
def deleteStaff_Record(user:Staff):
  user.delete_staff(id = input('Delete Staff record with ID: '))

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


def managerMenu(user:Staff):
  while True:
    print('1.\tUpdate own profile')
    print('2.\tRegister new staff')
    print('3.\tUpdate existing staff record')
    print('4.\tDelete staff record')
    print('5.\tUpdate car renting rate') # who has the say? why default 250 n then manager can set other default? then car service staff can change???
    print('6.\tView monthly revenue report')
    print('7.\tExit program')
    while (operation := input('\nEnter operation number: ')) not in ('1','2','3','4','5','6','7'):
      print('\nInvalid operation number!')
    match operation:
      case '1':
        updateProfile(user)

      case '2':
        registerStaff(user)

      case '3':
        pass

      case '4':
        deleteStaff_Record(user)

      case '5':
        pass

      case '6':
        pass

      case '7':
        return

def customer1Menu(user:Staff):
  while True:
    print('1.\tUpdate own profile')
    print('2.\tRegister new customer')
    print('3.\tView registered customers')
    print('4.\tUpdate existing customer record')
    print('5.\tDelete customer record')
    print('6.\tExit program')
    while (operation := input('\nEnter operation number: ')) not in ('1','2','3','4','5','6'):
      print('\nInvalid operation number!')
    match operation:
      case '1':
        updateProfile(user)

      case '2':
        registerCustomer()

      case '3':
        pass

      case '4':
        pass

      case '5':
        pass

      case '6':
        return

def customer2Menu(user:Staff):
  # may subject to change because it is kinda unclear what is expected from the program here
  while True:
    print('1.\tUpdate own profile')
    print('2.\tRecord new rental request')
    print('3.\tGenerate bill')
    print('4.\tView rental transactions')
    print('5.\tDelete rental record')
    print('6.\tExit program')
    while (operation := input('\nEnter operation number: ')) not in ('1','2','3','4','5','6'):
      print('\nInvalid operation number!')
    match operation:
      case '1':
        updateProfile(user)

      case '2':
        pass

      case '3':
        pass

      case '4':
        pass

      case '5':
        pass

      case '6':
        return

def carMenu(user:Staff):
  while True:
    print('1.\tUpdate own profile')
    print('2.\tRegister new car')
    print('3.\tView car record')
    print('4.\tUpdate existing car record')
    print('5.\tDelete car record')
    print('6.\tExit program')
    while (operation := input('\nEnter operation number: ')) not in ('1','2','3','4','5','6'):
      print('\nInvalid operation number!')
    match operation:
      case '1':
        updateProfile(user)

      case '2':
        pass

      case '3':
        pass

      case '4':
        pass

      case '5':
        pass

      case '6':
        return

if __name__ == '__main__':
  
  Staff.readRecord()
  Customer.readRecord()
  Car.readRecord()
  Rental.readRecord()

  user:Staff = login()
  print(f'\nWelcome, {user.name}\n')
  match user.role:
    case 'Manager':
      managerMenu(user)
    case 'Customer Service Staff I':
      customer1Menu(user)
    case 'Customer Service Staff II':
      customer2Menu(user)
    case 'Car Service Staff':
      carMenu(user)
    case 'N/A':
      print('An error has occured. Please contact a manager.')

  Staff.updateRecord()
  Customer.updateRecord()
  Car.updateRecord()
  Rental.updateRecord()