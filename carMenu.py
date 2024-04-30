from DataStructures import *
from function import *

#registration_no:str
#manufacturer:str
#model:str
#manufacture_year:int
#capacity:int
#last_service_date:datetime
#insurance_policy_number:str
#insurance_expiry:datetime
#road_tax_expiry:datetime

#This is use to check is the car plate match the rule that provide by JBJ
"""def is_valid_malaysian_plate(plate: str) -> bool:
  return re.fullmatch(r'[A-Z]{1,3}\s?\d{1,4}\s?[A-Z]{1,3}', plate) is not None"""
def is_valid_malaysian_plate(plate: str) -> bool:
  import re
  return re.fullmatch(r'[A-Z]{1,3}\d{1,4}[A-Z]{0,1}', plate) is not None

def registerCar():
  while True:
    if getValidInput('Do you want to register a new car for rental? (Y/N): ',
                    (lambda x: x != '' and x.upper() in ['Y', 'N'], 'Insert cannot be empty or must be Y/N')).upper() != 'Y':
      break
    else:
      print('\nInformation for staff:\nplease take note that if got car plate like <SELANGOR 1>, please contact to Manager to have a manual input')
      print('New Car detail:\n')
      registration_no = getValidInput('\n-> Car plate: ', 
                                      (lambda x:x != '', '\nInput cannot be empty!'), 
                                      (lambda plate:is_valid_malaysian_plate(plate.upper()), '\nCar Plate does not follow the Malaysia JBJ rules')).upper()
      
      manufacturer = getValidInput('\n-> Manufacturer: ', 
                                   (lambda x:x != '', '\nInput cannot be empty!'))
      
      model = getValidInput('\n-> Model: ', 
                                   (lambda x:x != '', '\nInput cannot be empty!'))
      
      manufacture_year = int(getValidInput('\n-> Manufacture year: ', 
                                   (lambda x:x != '', '\nInput cannot be empty!'),
                                   (lambda x:x.isdigit(),'\nManufacture year must be number')))
      
      capacity = int(getValidInput('\n-> capacity: ', 
                     (lambda x:x != '', '\nInput cannot be empty!'),
                     (lambda x:x.isdigit(), '\nCapacity must be in number'),
                     (lambda x:x in (2, 4, 5, 6, 7, 8, 9), '\nCapacity is not recognise')))
      
      last_service_date = getValidInput('\nWhat is the class last service date? ', 
                                        (lambda x:x != '', '\nLast service date cannot be empty'),
                                        (lambda x:x.validDate()))

      #for checking
      print(registration_no)
      print(manufacturer)

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
    # Menu selection
    print('1.\tUpdate own profile')
    print('2.\tRegister new car')
    print('3.\tView registered cars')
    print('4.\tView available cars')
    print('5.\tView rented cars')
    print('6.\tUpdate existing car record')
    print('7.\tDelete car record')
    print('8.\tExit program')
  
    # Determining operation
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