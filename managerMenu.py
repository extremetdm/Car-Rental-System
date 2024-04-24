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
    
    operation = getValidInput('\nEnter operation number: ',(lambda x:x in ('1','2','3','4','5','6','7'),'\nInvalid operation number!'))

    match operation:
      case '1':
        updateProfile(user)

      case '2':
        registerStaff(user)

      case '3':
        updateExitingStaff(user)

      case '4':
        deleteStaff_Record(user)

      case '5':
        Update_rentingRate()

      case '6':
        monthlyRevenue()

      case '7':
        return