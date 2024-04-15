from DataStructures import *

# Returns user information if login successful
def loginMenu():

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

if __name__ == '__main__':

  Staff.readRecord()
  user = loginMenu()
  print(f'\nWelcome, {user.name}\n')
