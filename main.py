from DataStructures import *

def login():
# Login menu
# Returns user information if login successful
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

def managerMenu(user:Staff):
  pass

def customer1Menu(user:Staff):
  pass

def customer2Menu(user:Staff):
  pass

def carMenu(user:Staff):
  pass

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

  Staff.updateRecord()
  Customer.updateRecord()
  Car.updateRecord()
  Rental.updateRecord()