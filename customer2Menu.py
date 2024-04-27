from DataStructures import *
from function import *



def customer2Menu(user:Staff):
  while True:
    print('1.\tUpdate own profile')
    print('2.\tView available cars')
    print('3.\tRecord new rental request')
    print('4.\tGenerate bill')
    print('5.\tView rental transactions')
    print('6.\tDelete rental record')
    print('7.\tExit program')
    
    operation = getValidInput('\nEnter operation number: ',(lambda x:x in ('1','2','3','4','5','6','7'),'\nInvalid operation number!'))

    match operation:
      case '1':
        updateProfile(user)

      case '2':
        viewCar(lambda car:car.availability == 'Available')

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
      
# For debugging purposes only
if __name__ == '__main__':
  Staff.readRecord()
  Customer.readRecord()
  Car.readRecord()
  Rental.readRecord()

  customer2Menu(Staff.getStaff('iwanttodie'))

  Staff.updateRecord()
  Customer.updateRecord()
  Car.updateRecord()
  Rental.updateRecord()