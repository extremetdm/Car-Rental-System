from DataStructures import *

# Returns user information if login successful
def loginMenu():

  print('\nLogin\n')

  while isinstance((loginStatus := Staff.login(input('Username: '),input('Password: '))),int):
    if loginStatus == 0:
      print('\nInvalid StaffID!\n')
    elif loginStatus < 3:
      print(f'\nWrong Password! {3-loginStatus} attempt(s) remaining.')
    elif loginStatus == 3:
      print(f'\nWrong Password! Program will now exit.')
      exit()
  
  return loginStatus

if __name__ == '__main__':
  
  testcase = Staff('mohdali','Mohammad Ali','Manager','123','01-01-2024','Available')
  
  user = loginMenu()
  print(f'\nWelcome, {user.name}\n')