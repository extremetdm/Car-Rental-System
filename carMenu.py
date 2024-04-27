from DataStructures import *
from function import *

def carMenu(user:Staff):
  while True:
    print('1.\tUpdate own profile')
    print('2.\tRegister new car')
    print('3.\tView registered cars')
    print('4.\tView available cars')
    print('5.\tView rented cars')
    print('6.\tUpdate existing car record')
    print('7.\tDelete car record')
    print('8.\tExit program')
  
    operation = getValidInput('\nEnter operation number: ',(lambda x:x in ('1','2','3','4','5','6','7','8'),'\nInvalid operation number!'))

    match operation:
      case '1':
        updateProfile(user)

      case '2':
        pass

      case '3':
        viewCar()

      case '4':
        viewCar(lambda car:car.availability == 'Available')

      case '5':
        # need registration date also
        viewCar(lambda car:car.availability == 'Rented')

      case '6':
        pass

      case '7':
        pass

      case '8':
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