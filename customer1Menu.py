from DataStructures import *
from function import *

def customer1Menu(user:Staff):
  while True:
    print('1.\tUpdate own profile')
    print('2.\tRegister new customer')
    print('3.\tView registered customers')
    print('4.\tUpdate existing customer')
    print('5.\tDelete inactive customer')
    print('6.\tExit program')

    operation = getValidInput('\nEnter operation number: ',lambda x:x in ('1','2','3','4','5','6'),'\nInvalid operation number!')

    match operation:
      case '1':
        updateProfile(user)

      case '2':
        registerCustomer()

      case '3':
        viewCustomer()

      case '4':
        pass

      case '5':
        pass

      case '6':
        return