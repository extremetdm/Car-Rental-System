from DataStructures import *
from function import *

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
        updateStaff(user)

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