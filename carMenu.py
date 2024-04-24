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
  
    operation = getValidInput('\nEnter operation number: ',(lambda x:x in '1','2','3','4','5','6','\nInvalid operation number!'))

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
      
# For debugging purposes only
if __name__ == '__main__':
  Staff.readRecord()
  Customer.readRecord()
  Car.readRecord()
  Rental.readRecord()

  carMenu(Staff.getStaff('Eric'))

  Staff.updateRecord()
  Customer.updateRecord()
  Car.updateRecord()
  Rental.updateRecord()