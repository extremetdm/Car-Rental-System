from DataStructures import *
from function import *

def registerCar():
  pass

def update_carRecord():
  pass

def delete_CarRecord():
    while True:
        disposed_cars = list(filter(lambda car: car.availability == 'Disposed', Car._carList.values()))
        if not disposed_cars:
            print("There are none of the car to be <Disposed> already.")
            break
        viewCar(lambda car: car.availability == 'Disposed')
        
        if getValidInput('\nWould you like to remove any car that is disposed? (Y/N): ', 
                         (lambda x: x != '' and x.upper() in ['Y', 'N'], 'Insert cannot be empty or must be Y/N')).upper() != 'Y':
            break
          
        print("\nWhich car would you like to delete?")
        
        for i, car in enumerate(disposed_cars, start=1):
            print(f"{i}. {car.registration_no}")
        print(f"{len(disposed_cars) + 1}. All")
        deleteChoice = getValidInput('Enter your choice: ',
                                     (lambda x: x.isdigit() and 1 <= int(x) <= len(disposed_cars) + 1, 'Invalid choice. Please enter a number from the list.'))
        if deleteChoice == str(len(disposed_cars) + 1):
            for car in disposed_cars:
                del Car._carList[car.registration_no]
            print("All disposed cars have been removed.")
        else:
            car_to_delete = disposed_cars[int(deleteChoice) - 1]
            del Car._carList[car_to_delete.registration_no]
            print(f'Car <{car_to_delete.registration_no}> has been removed')
        Car.updateRecord()


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
        registerCar()

      case '3':
        viewCar()

      case '4':
        viewCar(lambda car:car.availability == 'Available')

      case '5':
        # need registration date also
        viewCar(lambda car:car.availability == 'Rented')

      case '6':
        update_carRecord()

      case '7':
        delete_CarRecord()

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