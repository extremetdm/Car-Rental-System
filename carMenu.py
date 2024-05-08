from DataStructures import *
from function import *

# Function to check if a given string is a valid Malaysian car plate number
def is_valid_malaysian_plate(plate: str) -> bool:
  import re
  return re.fullmatch(r'[A-Z]{1,3}\d{1,4}[A-Z]{0,1}', plate) is not None

# Function to register a new car
def registerCar():
  while True:
    # Ask the user if they want to register a new car
    if getValidInput('\nDo you want to register a new car for rental? (Y/N): ',
                    (lambda x: x != '' and x.upper() in ['Y', 'N'], 'Insert cannot be empty or must be Y/N')).upper() != 'Y':
      break
    else:
      # Print some information for the staff
      print('\nInformation for staff:\nplease take note that if got car plate like <SELANGOR 1>, please contact to Manager to have a manual input')
      print('\nNew Car detail:\n')
      
      # Ask the user for the car plate, manufacturer, model, manufacture year, capacity, last service date, insurance policy number, insurance expiry date, and road tax expiry date
      # Validate each input as necessary
      registration_no = getValidInput('\n-> Car plate: ', 
                                      (lambda x:x != '', '\nInput cannot be empty!'), 
                                      (lambda plate:is_valid_malaysian_plate(plate.upper()), '\nCar Plate does not follow the Malaysia JPJ rules')).upper()
      
      manufacture = getValidInput('\n-> Manufacturer: ', 
                                   (lambda x:x != '', '\nInput cannot be empty!')).upper()
      
      model = getValidInput('\n-> Model: ', 
                                   (lambda x:x != '', '\nInput cannot be empty!')).upper()
      
      manufacture_year = int(getValidInput('\n-> Manufacture year: ', 
                                   (lambda x:x != '', '\nInput cannot be empty!'),
                                   (lambda x:x.isdigit(),'\nManufacture year must be in format (YYYY)'),
                                   (lambda x:len(x) == 4, '\nManufacture year must be a 4-digit number'),
                                   (lambda x:int(x) >= 1803,'\nThe time not even got an engine car yet'),
                                   (lambda x:int(x) <= (datetime.today().year), '\nManufacture year cannot exits current year')))
      
      capacity = int(getValidInput('\n-> capacity: ', 
                     (lambda x:x != '', '\nInput cannot be empty!'),
                     (lambda x:x.isdigit(), '\nCapacity must be in number'),
                     (lambda x:int(x) in (2, 4, 5, 6, 7, 8, 9), '\nCapacity is not recognise')))
      """
      # If the manufacture year is this year, skip asking for the last service date
      if manufacture_year != datetime.today().year:
        last_service_date = datetime.strptime(getValidInput('\nWhat is the car last service date? (YYYY-MM-DD): ', 
                                        (lambda x:x != '', '\nLast service date cannot be empty'),
                                        (lambda x:validDate(x) and int(x[:4]) >= 1804,'\nMust be in date format and year must be 1804 or later')), '%Y-%m-%d')
      else:
        last_service_date = ''
      """
      
      last_service_date = datetime.strptime(getValidInput('\nWhat is the car last service date? (YYYY-MM-DD): ', 
                                        (lambda x:x != '', '\nLast service date cannot be empty'),
                                        (lambda x:validDate(x) and int(x[:4]) >= 1804,'\nMust be in date format and year must be 1804 or later')), '%Y-%m-%d')

      insurance_policy_number = getValidInput('\nWhat is the car insurance policy number? ', 
                                        (lambda x:x != '', '\nInput cannot be empty!'),
                                        (lambda x:8 >= len(x) <= 13, '\nInsurance policy number must be 10 characters long'),
                                        (lambda x:x.isalnum(), '\nInsurance policy number must contain only alphanumeric characters')).upper()
      
      insurance_expiry = datetime.strptime(getValidInput('\nWhat is the car insurance expiry date? (YYYY-MM-DD): ', 
                                        (lambda x:x != '', '\nInsurance expiry date cannot be empty'),
                                        (lambda x:validDate(x),'\nMust be in date format'),
                                        (lambda x:datetime.strptime(x, '%Y-%m-%d') >= datetime.now(),'\nCar insurance cannot be expired, please inform customer to renew their insurance')), '%Y-%m-%d')
      
      road_tax_expiry = datetime.strptime(getValidInput('\nWhat is the car road tax expiry date? (YYYY-MM-DD): ', 
                                        (lambda x:x != '', '\nRoad tax expiry date cannot be empty'),
                                        (lambda x:validDate(x),'\nMust be in date format'),
                                        (lambda x:datetime.strptime(x, '%Y-%m-%d') >= datetime.now(),'\nRoad tax cannot be expired, please inform customer to renew their road tax'),
                                        (lambda x:datetime.strptime(x, '%Y-%m-%d').year <= datetime.now().year + 1,'\nRoad tax expiry date cannot be more than one year from the current date')), '%Y-%m-%d')
      
      # If all inputs are valid, create a new Car object and add it to the record
      if manufacture_year != datetime.today().year:
        Car(registration_no=registration_no,manufacture=manufacture,model=model,manufacture_year=manufacture_year,capacity=capacity,insurance_policy_number=insurance_policy_number,insurance_expiry=insurance_expiry,road_tax_expiry=road_tax_expiry)
      else:
        Car(registration_no,manufacture,model,manufacture_year,capacity,last_service_date,insurance_policy_number,insurance_expiry,road_tax_expiry)
      Car.updateRecord()
      
      # Print the new car record
      print()
      header = f"|{'Plate No.':^20}|{'Manufacturer':^15}|{'Model':^15}|{'Manufacture Year':^20}|{'Capacity':^20}|{'Last Service Date':^20}|{'Insurance No.':^20}|{'Insurance Exp. Date':^20}|{'Road Tax Exp. Date':^20}|{'Rental Rate':^20}|{'Availability':^15}|"
      print('New Car Record'.center(len(header)),'\n','-' * (len(header)-2))
      print(header,'\n','-' * (len(header) - 2))
      print(Car.getCar(registration_no))


def displaySimplifiedCarList():
    # Get a list of all cars
    car_list = list(Car.getCarList())
    
    # Print a newline for formatting
    print()
    
    # Define the header for the table
    header = f"|{'No.':^5}|{'Registration No.':^20}|{'Manufacturer':^15}|{'Model':^15}|{'Last Service Date':^20}|{'Insurance No.':^20}|{'Insurance Exp. Date':^20}|{'Road Tax Exp. Date':^20}|{'Availability':^15}|"
    
    # Print the table title and header
    print('Car Record'.center(len(header)),'\n','-' * (len(header)-2))
    print(header,'\n','-' * (len(header) - 2))
      
    # For each car in the list, print its details in a new row of the table
    for i, car in enumerate(car_list, start=1):
        # Convert the dates to strings in the 'YYYY-MM-DD' format
        insurance_expiry = car.insurance_expiry.strftime('%Y-%m-%d')
        road_tax_expiry = car.road_tax_expiry.strftime('%Y-%m-%d')
        last_service_date = car.last_service_date.strftime('%Y-%m-%d')
        
        # Print the car's details
        print(f"|{i:^5}|{car.registration_no:^20}|{car.manufacturer:^15}|{car.model:^15}|{last_service_date:^20}|{car.insurance_policy_number:^20}|{insurance_expiry:^20}|{road_tax_expiry:^20}|{car.availability:^15}|")
    
    # Return the list of cars
    return car_list


def update_carRecord():
  
  # Define the options for updating the car record
  options = {
    '1': 'Insurance Policy Number',
    '2': 'Insurance Expiry Date',
    '3': 'Road Tax Expiry Date',
    '4': 'Rental Availability',
    '5': 'Last Service Date',
    '6': 'Exit'
  }
  
  # Print the options to the user
  print('\nWhich record would you like to update?')
  for key, value in options.items():
    print(f'{key}. {value}')
  
  # Get the user's choice
  option = getValidInput('\nYour choice: ',
                        (lambda x: x in options, '\nInvalid option! Please enter a number from 1 to 6.'),
                        (lambda x:x != '', '\nInput cannot be empty'))
  
  # If the user chose to exit, return immediately
  if option == '6':
    return
  
  # Display the simplified car list and get the list of cars
  car_list = displaySimplifiedCarList()
  if not car_list:
    return

  # Get the index of the car to update from the user
  car_index = getValidInput("\nEnter the number of the car you want to update: ",
                            (lambda x: x.isdigit() and 1 <= int(x) <= len(car_list), '\nInvalid option! Please enter a valid car number.'),
                            (lambda x:x != '', '\nInput cannot be empty'))
  
  # Get the car to update
  car = car_list[int(car_index) - 1]
  
  # Depending on the user's choice, update the corresponding attribute of the car
  match option:
    case '1':
      # Update the insurance policy number
      car.insurance_policy_number = getValidInput('\n-> New Insurance Policy Number: ', 
                                        (lambda x:x != '', '\nInput cannot be empty!'),
                                        (lambda x:8 >= len(x) <= 13, '\nInsurance policy number must be 10 characters long'),
                                        (lambda x:x.isalnum(), '\nInsurance policy number must contain only alphanumeric characters')).upper()
    case '2':
      # Update the insurance expiry date
      car.insurance_expiry = datetime.strptime(getValidInput('\n-> New Insurance Expiry Date(YYYY-MM_DD): ', 
                                        (lambda x:x != '', '\nInsurance expiry date cannot be empty'),
                                        (lambda x:validDate(x),'\nMust be in date format'),
                                        (lambda x:datetime.strptime(x, '%Y-%m-%d') >= datetime.now(),'\nPlease make sure the insurance is the latest'),
                                        (lambda x: datetime.strptime(x, '%Y-%m-%d') >= car.insurance_expiry,'\nDate must not be earlier than the previous expiry date')), '%Y-%m-%d')
    case '3':
      # Update the road tax expiry date
      car.road_tax_expiry = datetime.strptime(getValidInput('\n-> New Road Tax Expiry Date(YYYY-MM_DD): ', 
                                        (lambda x:x != '', '\nRoad tax expiry date cannot be empty'),
                                        (lambda x:validDate(x),'\nMust be in date format'),
                                        (lambda x:datetime.strptime(x, '%Y-%m-%d') >= datetime.now(),'\nPlease make sure the road tax is the latest'),
                                        (lambda x:datetime.strptime(x, '%Y-%m-%d').year <= datetime.now().year + 1,'\nRoad tax expiry date cannot be more than one year from the current date'),
                                        (lambda x: datetime.strptime(x, '%Y-%m-%d') >= car.road_tax_expiry,'\nDate must not be earlier than the previous expiry date')), '%Y-%m-%d')
    case '4':
      # Update the rental availability
      availability_options = {
        '1': 'Available',
        '2': 'Reserved',
        '3': 'Rented',
        '4': 'Under service',
        '5': 'Disposed'
      }
      
      print('\nChange the availability to:')
      for key, value in availability_options.items():
        print(f'{key}. {value}')
      availability = getValidInput('\n-> Your choice: ',
                                  (lambda x: x in availability_options, '\nInvalid option! Please enter a number from 1 to 5.'),
                                  (lambda x:x != '', '\nInput cannot be empty'))
      car.availability = availability_options[availability]
    case '5':
      # Update the last service date
      car.last_service_date = datetime.strptime(getValidInput('\n-> New Service Date(YYYY-MM_DD): ', 
                                        (lambda x:x != '', '\nLast service date cannot be empty'),
                                        (lambda x:validDate(x) and int(x[:4]) >= 1804,'\nMust be in date format and year must be 1804 or later'),
                                        (lambda x: datetime.strptime(x, '%Y-%m-%d') >= car.last_service_date,'\nDate must not be earlier than the previous service date')), '%Y-%m-%d')

  # Update the car record
  Car.updateRecord()
  print('\nUpdate has done')

  

def delete_CarRecord():
    # Start an infinite loop
    while True:
        # Filter out all cars that are disposed
        disposed_cars = list(filter(lambda car: car.availability == 'Disposed', Car._carList.values()))
        
        # If there are no disposed cars, print a message and break the loop
        if not disposed_cars:
            print("There are none of the car to be <Disposed> already.")
            break
        
        # Display all disposed cars
        viewCar(lambda car: car.availability == 'Disposed')
        
        # Ask the user if they want to remove any disposed car
        if getValidInput('\nWould you like to remove any car that is disposed? (Y/N): ', 
                         (lambda x: x != '' and x.upper() in ['Y', 'N'], 'Insert cannot be empty or must be Y/N')).upper() != 'Y':
            break
          
        print("\nWhich car would you like to delete?")
        
        # Display all disposed cars with an index
        for i, car in enumerate(disposed_cars, start=1):
            print(f"{i}. {car.registration_no}")
        print(f"{len(disposed_cars) + 1}. All")
        
        # Get the user's choice of car to delete
        deleteChoice = getValidInput('Enter your choice: ',
                                     (lambda x: x.isdigit() and 1 <= int(x) <= len(disposed_cars) + 1, 'Invalid choice. Please enter a number from the list.'))
        
        # If the user chooses to delete all cars
        if deleteChoice == str(len(disposed_cars) + 1):
            for car in disposed_cars:
                del Car._carList[car.registration_no]
            print("All disposed cars have been removed.")
        else:
            # If the user chooses to delete a specific car
            car_to_delete = disposed_cars[int(deleteChoice) - 1]
            del Car._carList[car_to_delete.registration_no]
            print(f'Car <{car_to_delete.registration_no}> has been removed')
        
        # Update the car record
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
