from DataStructures import *
from function import *

def customer2Menu(user:Staff):
  while True:
    print('1.\tUpdate own profile')
    print('2.\tCheck car availability')
    print('3.\tRecord new rental request')
    print('4.\tGenerate bill')
    print('5.\tView rental transactions')
    print('6.\tDelete rental record')
    print('7.\tExit program')
    
    operation = getValidInput('\nEnter operation number: ',lambda x:x in '1234567','\nInvalid operation number!')

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
        pass

      case '7':
        return