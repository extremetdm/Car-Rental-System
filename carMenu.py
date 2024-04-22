from DataStructures import *
from function import *

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