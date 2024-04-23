from DataStructures import *
from function import *

def managerMenu(user:Staff):
  while True:
    print('1.\tUpdate own profile')
    print('2.\tRegister new staff')
    print('3.\tUpdate existing staff record')
    print('4.\tDelete staff record')
    print('5.\tUpdate car renting rate')
    print('6.\tView monthly revenue report')
    print('7.\tExit program')
    
    operation = getValidInput('\nEnter operation number: ',lambda x:x in '1234567','\nInvalid operation number!')

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